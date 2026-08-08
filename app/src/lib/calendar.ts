/**
 * The Elysian calendar.
 *
 * Implements `hist.calendar` directly. **No JavaScript `Date` object appears
 * anywhere in this application** — using one would silently import Earth's
 * calendar into a planet that does not have it (`eng.data-pipeline` section 7).
 *
 * Structure, all from canon:
 *   384 civil days = 12 months of 32 = 48 weeks of 8
 *   Thresholdday is intercalary, outside every week and month, every 4th year
 *     except centennial years
 *   The civil day divides into 26 hours of 60 minutes of 60 beats, and those
 *     are fractions of the solar day rather than SI units
 */

export interface CalendarShape {
  clock: {
    solarDaySeconds: number;
    hoursPerDay: number;
    minutesPerHour: number;
    beatsPerMinute: number;
  };
  year: {
    solarYearDays: number;
    civilYearDays: number;
    monthsPerYear: number;
    daysPerMonth: number;
    daysPerWeek: number;
    leapRule: { everyNYears: number; exceptDivisibleBy: number };
  };
  months: { index: number; name: string }[];
  weekdays: { index: number; name: string; rest: boolean }[];
  referenceDate: { year: number; month: number; day: number };
}

/** A civil date. `thresholdday` is the intercalary day, outside all months. */
export interface ElysianDate {
  year: number;
  month: number;
  day: number;
  thresholdday?: boolean;
}

/** Civil time of day. */
export interface ElysianTime {
  hour: number;
  minute: number;
  beat: number;
}

export function isLeapYear(year: number, shape: CalendarShape): boolean {
  const { everyNYears, exceptDivisibleBy } = shape.year.leapRule;
  return year % everyNYears === 0 && year % exceptDivisibleBy !== 0;
}

export function daysInYear(year: number, shape: CalendarShape): number {
  return shape.year.civilYearDays + (isLeapYear(year, shape) ? 1 : 0);
}

/** Ordinal day of the year, counting from 0 at Verane 1. */
export function dayOfYear(date: ElysianDate, shape: CalendarShape): number {
  if (date.thresholdday) return shape.year.civilYearDays;
  return (date.month - 1) * shape.year.daysPerMonth + (date.day - 1);
}

/**
 * The weekday. The calendar is perpetual: 384 divides evenly into eight-day
 * weeks, so every date falls on the same weekday in every year, forever.
 * Thresholdday belongs to no week, which is what preserves the alignment.
 */
export function weekday(date: ElysianDate, shape: CalendarShape) {
  if (date.thresholdday) return null;
  const index = dayOfYear(date, shape) % shape.year.daysPerWeek;
  return shape.weekdays[index] ?? null;
}

export function monthName(month: number, shape: CalendarShape): string {
  return shape.months.find((entry) => entry.index === month)?.name ?? String(month);
}

/** `EY 412, Calenth 16` — the prose form from `charter.canonical-units`. */
export function formatDate(date: ElysianDate, shape: CalendarShape): string {
  if (date.thresholdday) return `EY ${date.year}, Thresholdday`;
  return `EY ${date.year}, ${monthName(date.month, shape)} ${date.day}`;
}

/** `EY-0412-M08-D16` — the sortable form used in data. */
export function formatDateSortable(date: ElysianDate): string {
  const year = String(date.year).padStart(4, "0");
  if (date.thresholdday) return `EY-${year}-TH`;
  return `EY-${year}-M${String(date.month).padStart(2, "0")}-D${String(date.day).padStart(2, "0")}`;
}

/** `13:24` — H:MM on a 26-hour cycle, midnight 0:00, midday 13:00. */
export function formatTime(time: ElysianTime): string {
  return `${time.hour}:${String(time.minute).padStart(2, "0")}`;
}

/** Convert a fraction of the solar day into civil hours, minutes, and beats. */
export function timeFromFraction(fraction: number, shape: CalendarShape): ElysianTime {
  const wrapped = ((fraction % 1) + 1) % 1;
  const totalMinutes = wrapped * shape.clock.hoursPerDay * shape.clock.minutesPerHour;
  const hour = Math.floor(totalMinutes / shape.clock.minutesPerHour);
  const minute = Math.floor(totalMinutes % shape.clock.minutesPerHour);
  const beat = Math.floor((totalMinutes % 1) * shape.clock.beatsPerMinute);
  return { hour, minute, beat };
}

/** Fraction of the solar day elapsed, from civil time. */
export function fractionFromTime(time: ElysianTime, shape: CalendarShape): number {
  const minutes =
    time.hour * shape.clock.minutesPerHour + time.minute + time.beat / shape.clock.beatsPerMinute;
  return minutes / (shape.clock.hoursPerDay * shape.clock.minutesPerHour);
}

/** Step a date forward by whole days, crossing Thresholdday and year ends. */
export function addDays(date: ElysianDate, days: number, shape: CalendarShape): ElysianDate {
  let ordinal = dayOfYear(date, shape) + days;
  let year = date.year;

  for (;;) {
    const length = daysInYear(year, shape);
    if (ordinal >= length) {
      ordinal -= length;
      year += 1;
    } else if (ordinal < 0) {
      year -= 1;
      ordinal += daysInYear(year, shape);
    } else {
      break;
    }
  }

  if (ordinal === shape.year.civilYearDays) return { year, month: 1, day: 1, thresholdday: true };
  return {
    year,
    month: Math.floor(ordinal / shape.year.daysPerMonth) + 1,
    day: (ordinal % shape.year.daysPerMonth) + 1,
  };
}
