/**
 * Hover label positioning.
 *
 * The label lives in the DOM, outside the canvas, so it is real text at real
 * font sizes rather than a texture. The scene projects the hovered point each
 * frame and moves it.
 *
 * React context does not cross the react-three-fiber reconciler boundary, so
 * the two halves meet through this module rather than through a provider. The
 * alternative — pushing screen coordinates into the store at 60 fps — would
 * re-render the tree every frame.
 */

let element: HTMLElement | null = null;

export function registerLabelElement(node: HTMLElement | null) {
  element = node;
}

/** Move the label to a screen position, or hide it when `null`. */
export function positionLabel(screen: { x: number; y: number } | null, text?: string) {
  if (!element) return;
  if (!screen) {
    element.dataset.visible = "false";
    return;
  }
  if (text !== undefined && element.textContent !== text) element.textContent = text;
  element.dataset.visible = "true";
  element.style.transform = `translate3d(${screen.x}px, ${screen.y}px, 0)`;
}
