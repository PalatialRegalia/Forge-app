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
- **Session timer** — start a workout, advance through exercises, track elapsed time per exercise and total session time.
- **Completion summary** — when a session ends, you get a recap of what you did and for how long.
- **Workout logbook** — every completed session is saved to `localStorage` and viewable in a history panel, so you can see your volume over time.
- **Wake Lock** — the screen stays on during a session when the browser supports it.
- **PWA / installable** — manifest, icons, and service worker let you add it to your home screen and use it offline.
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

Everything is in `index.html`. There is no separate JS or CSS file, no build, and no server-side component.

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
and renders identically on every platform. There are 15 ids:

| Movement patterns | Traditions | Elements |
|---|---|---|
| `mobility`, `hinge`, `pull`, `rotation`, `raise`, `carry`, `lunge` | `persia`, `india`, `japan`, `china`, `russia`, `north`, `plains` | `cold` |

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

## Design notes

Research on the visual and icon direction lives in [`docs/design-references.md`](docs/design-references.md): the "AK-47 ethos" decoded into testable principles, a reference library of projects that combine excellent UI/UX with that ethos (GOV.UK, Rams, Gymboss, Concept2 PM5, Health Icons, Game Icons, Met/Smithsonian Open Access), measured contrast ratios for the colour tokens, and the polish shortlist.

Implemented from that shortlist so far: every colour is a named token, the measured contrast failures are fixed (muted text 8.3:1 on cards, red as ink 5.1:1, control edges 3.2:1 where they were 1.1:1), the three drifting accents are reduced to one red in two roles plus a single amber, and the platform emoji are replaced by the hand-drawn glyph set described above.

## Author

Built by **[palatialregalia](https://github.com/palatialregalia)**.

## License

MIT — see `LICENSE`.

## Contributing

See `CONTRIBUTING.md` for how to propose changes, run the app, and submit work.
