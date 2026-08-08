import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    target: "es2022",
    rollupOptions: {
      output: {
        // Three.js is large and stable; splitting it lets the app shell cache
        // independently of the renderer. See eng.design-system section 6.
        manualChunks(id: string) {
          if (id.includes("node_modules")) {
            if (/three|@react-three/.test(id)) return "three";
            return "vendor";
          }
          return undefined;
        },
      },
    },
  },
});
