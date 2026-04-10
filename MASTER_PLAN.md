# Chemistry Portal 11 - Master Plan & Development Guidelines

This document establishes the structural, design, and deployment standards for all chapters (`copy_master_chX.html`) of the Class 11 Chemistry project. Future AI coding agents MUST strictly follow these guidelines when adding or generating new chapters.

## 1. Responsive Layout Standards (Mobile-Friendly)
- **Vertical Stacking for Content:** Use `grid-template-columns: 1fr;` (stacked vertically) instead of `1fr 1fr` (side-by-side) for theory, information boxes, solved examples, or definition cards. This prevents elements from overflowing across the screen borders on mobile devices.
- **Scrollable Tables:** EVERY HTML `<table>` MUST be wrapped inside a responsive container to prevent layout breaking on mobile:
  ```html
  <div style="overflow-x: auto; width: 100%; border-radius: 12px;">
      <table style="width: 100%; border-collapse: collapse; ...">
          ...
      </table>
  </div>
  ```
- **Unified Sequential Tables:** Do not split long sequences (such as SI Prefixes, Rules) into left/right columns within a table. Merge them into a single vertical sequence flowing from top to bottom underneath one set of headers.

## 2. Interactive Simulators (Desktop Layout Priority)
- **Side-by-Side Visuals:** Unlike text theory, Interactive Lab Simulators (e.g. Mixture Lab, Volume Simulator, Particle Viewer) SHOULD use side-by-side layouts (e.g., `grid-template-columns: 1.5fr 1fr;` or `2fr 1fr`). This allows the interactive buttons and controls to sit neatly next to the visual `canvas`.

## 3. JavaScript & Live Deployment Compatibility
- **Global Scope Execution:** The premium viewer (`notes_html_view.html`) fetches a chapter's HTML and automatically executes its Javascript globally via DOM `<script>` appending.
- **CRITICAL - Use `var` inside Chapter HTML:** Never use top-level `const` or `let` for variables or classes inside `<script>` blocks within `copy_master_chX.html`. Use `var` everywhere. If you use `const` and the user refreshes or changes views, it throws `SyntaxError: Identifier has already been declared`, breaking the entire page on live deployment.

## 4. Edge-to-Edge Premium Design
- **No Outer Constraints:** `notes_html_view.html` must always run **Edge-to-Edge** (`100vw`). The central viewer does NOT wrap content in a restricted `.container` with margins/paddings. This faithfully mimics the local `index.html` fullscreen rendering.
- **Cache-Busting Logic:** `fetch` requests inside dynamic loaders must append `?v=${timestamp}` to guarantee the CDN always serves the freshest pushed HTML file.
