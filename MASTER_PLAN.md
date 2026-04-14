# 📜 CHEMISTRY PORTAL: MASTER PLAN (Ref: 1520)

> [!IMPORTANT]
> This document defines the MANDATORY architectural and design standards for the Class 11/12 Chemistry Portal. These standards are derived from the successful implementation of [ch1eng/ch1_part11.html](file:///c:/Users/jiten/Desktop/class11/Chem11/ch1eng/ch1_part11.html).
> 
> **LOCK STATUS:** 🔒 LOCKED. No deviations allowed without authorization (Password: 1520).

---

## 🏗️ 1. Core Philosophy: "The Projector Rule"
Every page must be optimized for **Simultaneous Classroom Projection and Mobile Review**.
- **NO COLUMN LAYOUTS**: All content cards, units, and guides must be stacked vertically (One-under-another). Side-by-side grids are strictly forbidden as they reduce visibility during projection.
- **UI Responsiveness**: Base width must remain `100vw` with `box-sizing: border-box`.
- **Primary Typography**: Use `font-family: 'Outfit', sans-serif;` with extreme weights (**700, 800, 950**) for critical text.

## 🎨 2. Design System (Emerald Earth Style)
All pages must utilize the following color tokens and CSS variables:

```css
:root {
    --primary: #059669;        /* Emerald Main */
    --primary-dark: #064e3b;   /* Deep Forest */
    --secondary: #10b981;      /* Bright Emerald */
    --accent: #38bdf8;         /* Lab Sky Blue */
    --molarity-red: #e11d48;   /* Solution Hot Color */
    --molality-teal: #0d9488;  /* Temperature Independent Teal */
    --slate-900: #0f172a;      /* Navigation/Background */
    --font-main: #000000;      /* Pure Black for Contrast */
}
```

## 🧪 3. Mathematical Rendering (Veritcal Fractions)
All stoichiometric and concentration formulas must use the `.math-frac` flexbox system. DO NOT use table-based or inline-slash fractions.

```html
<div class="math-frac">
    <span class="math-num">Numerator Content</span>
    <span class="math-den">Denominator Content</span>
</div>
```
*CSS Requirements:* `inline-flex`, `flex-direction: column`, `vertical-align: middle`, and `border-bottom: 3px solid`.

## 🕹️ 4. Interactive Simulator Standards
- **Global Scoping**: All simulator variables (sliders, displays) must be uniquely prefixed (e.g., `molLab_`) to prevent logic collisions during page transitions.
- **Visual Feedback**: Simulators must include a visual representation (e.g., Beaker with intensity-shifting liquid) that reacts to user input in real-time.
- **Backgrounds**: Use dark blocks (`#020617` or `rgba(255,255,255,0.05)`) for simulator containers to make them pop.

## 🧭 5. Navigation & Utility Suite (Floating Pills UI)
Every page MUST contain the following navigation components at the bottom using the transparent floating pill design (NO dark wrapper blocks):
1. **Container**: `.nav-buttons { background: transparent; padding: 60px 0vw 40px; margin-top: 50px; }`
2. **Main Hub Button**: Pill with dark slate background (`style="background: #1e293b;"`).
3. **Previous Button**: Pill with silver/grey background (`style="background: #94a3b8;"`).
4. **Next Button**: Pill with Emerald green background (`style="background: #059669;"`).
5. **Action Suite**: Buttons for `Print to PDF` and `Copy Content` (if added).

## 🔄 6. Workflow: Parallel Creation & Multi-File Architecture
For Chapter 2 and all future chapters, the following workflow is mandatory:
- **Hindi Medium Primary**: Hindi files (`chX_parts/`) MUST be purely Hindi-medium. All boilerplate, headings, and placeholder text must be strictly in Hindi, using English ONLY in brackets for technical terms (e.g., `परमाणु की संरचना (Structure of Atom)`).
- **Parallel Translation**: As soon as a Part is finalized in Hindi, the English version (`chXeng/`) must be generated immediately.
- **Index Dashboard Routing**: The `index.html` (via `main.js`) MUST feature a direct "🇮🇳 Hindi Version (Premium)" button with an Orange Gradient (`linear-gradient(135deg, #f59e0b, #d97706)`). For all new chapters, this button MUST link directly to the standalone `chX_parts/chX_part1.html` files, bypassing the old `notes_html_view.html` master compiler.
- **Atomic File Structure**: Every part must be saved as a unique HTML file.
- **Reference Integrity**: All new files must inherit the CSS, Simulator UI, and Formula logic.

## 🔒 7. Authorization Policy
Any request to revert to grids, reduce font sizes, use old inline CSS wrappers for navigation, or change the Emerald Earth color palette must be accompanied by the verification code **1520**. Without this code, the assistant will prioritize this Master Plan over session-specific requests.

---
## 📊 8. Chapter 2 Tracking (Structure of Atom)
**20-Part Syllabus Breakdown (NCERT):**
- [x] 1. Introduction & Discovery of Electron (Cathode Rays)
- [x] 2. Charge to Mass ratio & Millikan's Oil Drop Experiment
- [x] 3. Discovery of Proton (Canal Rays) and Neutron
- [x] 4. Thomson's Model of Atom
- [x] 5. Rutherford's Alpha Particle Scattering Experiment
- [x] 6. Rutherford's Nuclear Model of Atom & Observations
- [x] 7. Atomic Number, Mass Number, Isotopes & Isobars
- [x] 8. Drawbacks of Rutherford's Model
- [x] 9. Wave Nature of Electromagnetic Radiation
- [x] 10. Particle Nature of Light (Planck's Quantum Theory)
- [ ] 11. Photoelectric Effect
- [ ] 12. Atomic Spectra (Emission & Absorption)
- [ ] 13. Line Spectrum of Hydrogen
- [ ] 14. Bohr's Model for Hydrogen Atom (Postulates)
- [ ] 15. Energy States & Limitations of Bohr's Model
- [ ] 16. Dual Behaviour of Matter (de Broglie's Equation)
- [ ] 17. Heisenberg's Uncertainty Principle
- [ ] 18. Quantum Mechanical Model & Orbitals
- [ ] 19. Quantum Numbers (n, l, m, s)
- [ ] 20. Rules of Electronic Configuration (Aufbau, Pauli, Hund)

---
*Plan established after Chapter 1 completion. Updated for Chapter 2 Workflow.*
