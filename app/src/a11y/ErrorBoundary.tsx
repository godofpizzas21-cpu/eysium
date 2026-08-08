/**
 * Error boundary.
 *
 * If the renderer fails, the accessible interface must survive: it is the real
 * document, and losing WebGL should not lose the Atlas.
 */
import { Component, type ReactNode } from "react";

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
}

interface State {
  failed: boolean;
  message: string;
}

export class ErrorBoundary extends Component<Props, State> {
  override state: State = { failed: false, message: "" };

  static getDerivedStateFromError(error: Error): State {
    return { failed: true, message: error.message };
  }

  override render() {
    if (!this.state.failed) return this.props.children;
    return (
      this.props.fallback ?? (
        <div className="notice" role="alert">
          <p>
            The globe could not be drawn: {this.state.message}. Everything in the Atlas is
            still reachable from the list of places.
          </p>
        </div>
      )
    );
  }
}
