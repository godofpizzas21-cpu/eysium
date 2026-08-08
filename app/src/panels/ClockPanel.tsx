/**
 * The Elysian clock.
 *
 * Shows the civil date and time, and lets both be moved. Every unit here is
 * Elysian: 26 hours of 60 minutes, 8-day weeks, 12 months of 32 days, and
 * Thresholdday outside all of them.
 */
import { addDays, formatDate, formatTime, timeFromFraction, weekday } from "../lib/calendar.js";
import { daylightHours, subsolarPoint } from "../lib/sun.js";
import { useAtlas } from "../state/store.js";

export function ClockPanel() {
  const load = useAtlas((s) => s.load);
  const date = useAtlas((s) => s.date);
  const time = useAtlas((s) => s.time);
  const setDate = useAtlas((s) => s.setDate);
  const setTime = useAtlas((s) => s.setTime);
  const running = useAtlas((s) => s.running);
  const setRunning = useAtlas((s) => s.setRunning);

  if (load.status !== "ready") return null;

  const shape = load.canon.calendar;
  const tilt = load.canon.planet.planet.axialTiltDeg;
  const day = weekday(date, shape);
  const sun = subsolarPoint(date, time, shape, tilt);
  const minutesPerDay = shape.clock.hoursPerDay * shape.clock.minutesPerHour;
  const elapsed = time.hour * shape.clock.minutesPerHour + time.minute;

  return (
    <section className="clock" aria-label="Elysian date and time">
      <div className="clock__readout">
        <p className="clock__date">{formatDate(date, shape)}</p>
        <p className="clock__meta">
          {day ? day.name : "Outside the week"}
          {day?.rest ? " · rest day" : ""}
        </p>
      </div>

      <div className="clock__time">
        <span className="clock__hhmm">{formatTime(time)}</span>
        <span className="clock__of">of {shape.clock.hoursPerDay}</span>
      </div>

      <label className="clock__control">
        <span className="clock__label">Time of day</span>
        <input
          type="range"
          min={0}
          max={minutesPerDay - 1}
          step={1}
          value={elapsed}
          onChange={(event) =>
            setTime(timeFromFraction(Number(event.target.value) / minutesPerDay, shape))
          }
        />
      </label>

      <div className="clock__buttons">
        <button type="button" onClick={() => setDate(addDays(date, -1, shape))}>
          Previous day
        </button>
        <button type="button" aria-pressed={running} onClick={() => setRunning(!running)}>
          {running ? "Pause" : "Run"}
        </button>
        <button type="button" onClick={() => setDate(addDays(date, 1, shape))}>
          Next day
        </button>
      </div>

      <dl className="clock__figures">
        <div>
          <dt>Subsolar point</dt>
          <dd>
            {sun.lat.toFixed(1)}°, {sun.lon.toFixed(1)}°
          </dd>
        </div>
        <div>
          <dt>Daylight at 45° N</dt>
          <dd>{daylightHours(45, sun.lat, shape).toFixed(1)} h</dd>
        </div>
      </dl>
    </section>
  );
}
