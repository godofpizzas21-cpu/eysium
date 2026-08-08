/**
 * A collapsible sidebar section.
 *
 * The side column was showing the clock, the layer switcher, the legend, and
 * every place in the Atlas simultaneously. Native <details> keeps it to one
 * thing at a time, stays keyboard accessible without any work, and needs no
 * state.
 */
import type { ReactNode } from "react";

export function Section({
  title,
  children,
  open = false,
  hint,
}: {
  title: string;
  children: ReactNode;
  open?: boolean;
  hint?: string;
}) {
  return (
    <details className="section" open={open}>
      <summary className="section__summary">
        <span>{title}</span>
        {hint && <span className="section__hint">{hint}</span>}
      </summary>
      <div className="section__body">{children}</div>
    </details>
  );
}
