# Forge Kinetic

A progressive web app for structured movement workouts — a curated library of exercises, a daily planner, a session timer with audible cues, and a local logbook that tracks your sessions across time. Runs offline after the first load.

<div align="center">

![Forge Kinetic icon](icon.svg)

**Forge Kinetic**

</div>

---

## What it is

Forge Kinetic is a single-file progressive web app for training. It gives you:

- **Exercise library** — a built-in set of movements, each with a title, a glyph, cues, and a default prescription (sets × reps or timed intervals).
- **Daily planner** — pick a day, see the planned exercises for it, and optionally mark an exercise as optional.
- **Session timer** — start a workout, advance through exercises, track elapsed time per exercise and total session time. The seconds are the largest thing on screen, and an interval boundary fires **both** a sound cue and a vibration (a beep is missed over gym noise, a buzz is missed through a case). Sound can be muted from the header and the choice is remembered.
- **Completion summary** — when a session ends, you get a recap of what you did and for how long.
- **Workout logbook** — every completed session is saved to `localStorage` and viewable in a history panel, so you can see your volume over time.
- **Wake Lock** — the screen stays on during a session when the browser supports it.
- **PWA / installable** — manifest, icons and a service worker (`sw.js`) let you add it to your home screen and reopen it offline. Page loads prefer the network and fall back to the cache, so it stays fresh when online and still opens without a connection.
- **Zero dependencies** — plain HTML, CSS, and JavaScript. No framework, no build step, no npm.

## Tech stack

| Layer | Details |
|---|---|
| Markup | HTML5, offline-first |
| Styling | Vanilla CSS custom properties, flexbox, responsive design |
| Logic | Vanilla JavaScript (ES6+), no frameworks |
| Storage | `localStorage` for the workout logbook (client-side only) |
| PWA | Web App Manifest (`manifest.json`), SVG icon (`icon.svg`), installable on mobile |
| Hosting | Static — any static host or CDN (GitHub Pages, Netlify, Vercel, S3, etc.) |

## Project structure

```
forge-app/
├── index.html      # Single-page app: markup, styles, and logic
├── manifest.json   # PWA manifest (name, icons, display, theme colors)
├── icon.svg        # PWA / favicon / apple-touch-icon (SVG)
├── sw.js           # Service worker: offline shell, network-first pages
├── docs/
│   └── design-references.md   # UI/UX reference library and polish shortlist
├── tools/
│   ├── glyph-preview.py       # Regenerates the icon contact sheet (no deps)
│   └── glyph-preview.html     # Generated: every glyph at 16/24/32 px
├── .gitignore
├── LICENSE         # MIT
├── CONTRIBUTING.md
└── README.md       # This file
```

The application — markup, styles and logic — is entirely in `index.html`. `sw.js` is the only separate script, because a service worker cannot be inline. There is no build step and no server-side component.

## Running it locally

Because there is no build step, you can open `index.html` directly from disk for casual testing. For a full PWA experience (service worker, install prompt, offline behavior), serve it over HTTPS (or `http://localhost`) with a static server:

```bash
# Python 3
python -m http.server 8000

# or Node (npx)
npx serve .

# or any static host / CDN
```

Then open `http://localhost:8000` and install from the browser prompt or the "Add to Home Screen" menu.

## Using the app

1. Open the app in a browser.
2. Use the day selector to choose which day's plan you want to run.
3. Review the planned exercises for that day. Optional exercises are marked as such.
4. Start the session timer and work through the exercises.
5. When the session is complete, the summary is recorded in your logbook.
6. Open the history panel anytime to see past sessions.

### Notes

- Exercise data (titles, cues, defaults) lives in `index.html` as a JavaScript object.
- The logbook is stored in the browser's `localStorage` under the key `forgeLogbook`. It is tied to the origin, not exported anywhere by default.
- Wake Lock is requested at session start when available and released on session end or page unload.

## Customizing exercises

Exercise data is defined in `index.html` as a JavaScript object. Each exercise has fields like:

```js
{
  id: "exercise_id",
  title: "Display title",
  glyph: "hinge",    // id from the GLYPHS set in index.html (see "Icons" below)
  cues: "Cue text shown during the set",
  sets: 3,
  reps: 10,
  weight: null,      // optional
  isOptional: false  // optional
}
```

To add or modify exercises, edit the exercise definitions directly in `index.html`. To change the daily plans, edit the day→exercise mappings in the same object. To change the icon or colors, edit `icon.svg` and `manifest.json`.

## Icons

Every exercise points at a glyph id from the `GLYPHS` object in `index.html`. The
set is drawn by hand on a 24×24 grid with a 2 px stroke and `currentColor`, so a
glyph inherits the colour of whatever badge contains it, scales without blurring,
and renders identically on every platform. There are 17 ids:

| Movement patterns | Traditions | Elements | Interface |
|---|---|---|---|
| `mobility`, `hinge`, `pull`, `rotation`, `raise`, `carry`, `lunge` | `persia`, `india`, `japan`, `china`, `russia`, `north`, `plains` | `cold` | `soundOn`, `soundOff` |

To see the whole set at 16/24/32 px:

```bash
python3 tools/glyph-preview.py     # rewrites tools/glyph-preview.html
```

Then open `tools/glyph-preview.html` in a browser. The script reads the glyph
definitions out of `index.html`, so there is one source of truth for the icon set.

Adding a glyph means adding one entry to `GLYPHS` and one to `GLYPH_LABELS` in
`index.html`. Keep to the grid: 2 px stroke, round caps and joins, `currentColor`,
no fills, and check it still reads at 16 px.

## PWA / manifest

`manifest.json` declares the app name, short name, standalone display mode, background and theme colors, and the SVG icon. The icon is also referenced as the favicon and apple-touch-icon in the HTML `<head>`.

## Deployment

This is a static site. Deploy the files as-is to any static host:

- **GitHub Pages** — push to the repo and enable Pages, or use a `gh-pages` branch / `/docs` folder.
- **Netlify / Vercel** — connect the repo; they serve the root on push.
- **S3 / CloudFront** — upload the files and set cache headers.

No server-side code, no build, no environment variables.

### After changing a cached file

`sw.js` precaches `index.html`, `manifest.json` and `icon.svg` under a versioned cache name. **Bump `CACHE` in `sw.js` whenever you ship a change to one of those files**, or the stale copy stays in the cache. Page loads are network-first, so an online visitor always gets the new build regardless; the version bump is what refreshes the offline copy.

## Design notes

Research on the visual and icon direction lives in [`docs/design-references.md`](docs/design-references.md): the "AK-47 ethos" decoded into testable principles, a reference library of projects that combine excellent UI/UX with that ethos (GOV.UK, Rams, Gymboss, Concept2 PM5, Health Icons, Game Icons, Met/Smithsonian Open Access), measured contrast ratios for the colour tokens, and the polish shortlist.

All seven moves on that shortlist are now implemented:

- **Tokens.** 25 named tokens in `:root` covering colour, radius and type, and **no colour or size literal appears anywhere else in the stylesheet**. Sixteen ad-hoc font sizes collapsed to a seven-step scale plus one display size; radii collapsed from six values to three.
- **Contrast.** Every measured failure fixed — muted text 6.6:1 → 8.3:1, red as ink 4.08:1 → 5.1:1, white on the primary fill 4.17:1 → 6.2:1, control edges 1.14:1 → 3.2:1, the teal export button 3.32:1 → 15.5:1.
- **One signal system.** Four unrelated hues became one red in two roles (ink and fill) plus a single amber for "optional". Wipe Logbook is red *ink* on a neutral body, so the red *fill* means exactly one thing.
- **Glyphs.** 17 hand-drawn icons on a 24×24 grid, 4.7 KB for the whole set, replacing platform emoji entirely — zero emoji codepoints remain in the file.
- **Ergonomics.** Pinch-zoom restored, `user-select: none` narrowed to controls only, every touch target at least 48 px, and the destructive action separated below a rule.
- **Depth removed.** Zero `box-shadow` in the stylesheet; edges and fills carry the hierarchy instead.
- **Imagery.** A measured vector layer: a low-contrast hatch on the header, the day's signature glyph as a large ghost in the session summary, and the brand mark in the empty logbook state. No raster images, so there is nothing to fail offline and nothing to license.

Two defects found while working that were not on the shortlist are also fixed: the Skip button had never rendered its border (a CSS specificity bug), and the README claimed offline support "via service worker" while the repo contained no service worker at all — `sw.js` now makes that claim true.

## Author

Built by **[palatialregalia](https://github.com/palatialregalia)**.

## License

MIT — see `LICENSE`.

## Contributing

See `CONTRIBUTING.md` for how to propose changes, run the app, and submit work.
