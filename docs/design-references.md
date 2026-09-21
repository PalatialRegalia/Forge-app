# AK-47 Ethos — UI/UX Reference Library for Forge Kinetic

**Status:** research / exploration. No app code was changed by this document.
**Branch:** `cline/m7atzh4c`
**Question answered:** which *existing* projects have excellent UI/UX **and** exhibit "AK-47 ethos", as inputs to polishing Forge Kinetic with imagery and icons.

---

## 0. TL;DR

- "AK-47 ethos" is decoded below into **8 testable principles** (§1) plus a **6-test spec sheet** that can be run against any polish proposal (§2).
- Forge is *already* unusually close to that ethos: one 38 KB file, zero dependencies, no build step, system fonts, tabular numerals, 44 px controls, offline-first. **This is a strength to defend, not a starting point to modernize away.** (§3.1)
- So the opportunity is not "add more stuff". It is: (a) fix the **measured** legibility failures, (b) collapse three drifting accent colours into **one signal system**, (c) replace platform emoji with a **hand-made inline SVG glyph set**, and (d) add imagery only where it survives the offline test. (§3.2, §3.3, §5)
- **Best-fit references by category:**
  - *Principles canon:* GOV.UK Government Design Principles; Dieter Rams' ten principles; WCAG's numeric criteria; the suckless philosophy.
  - *Products that literally are the ethos:* **Gymboss** interval timer, **Concept2 PM5**, **Garmin/Suunto** field watches, **Teenage Engineering OP-1**.
  - *Icon systems:* **Health Icons (CC0)** and **Game Icons (CC BY 3.0)** match the "field-grade, monochrome, stencil-able" brief, and are free.
  - *Imagery with real heritage content and zero licensing exposure:* **The Met Open Access (CC0, 470k+)**, **Smithsonian Open Access (CC0, 11M+ records)**.
- **Anti-references:** Unsplash, remote CDNs, and `fonts.googleapis.com`. Their own terms *require* hotlinking and attribution, which is a network dependency inside an offline-first app — i.e. a jam you built on purpose. (§4G)

---

## 1. Decoding the "AK-47 ethos"

The AK-47 is invoked in engineering culture as shorthand for *crude but unstoppable*. The transferable traits, as commonly characterized in design and engineering commentary:

| # | Principle (rifle framing) | Applied to Forge Kinetic |
|---|---|---|
| **P1** | **Irreducible mechanism** — few parts; nothing can be removed without breaking it | One HTML file. Every rule and element earns its place. No dead CSS, no unused glyphs |
| **P2** | **Tolerant of abuse** — runs dirty, cold, fouled | Works offline, on slow 3G, in bright sun, on a 5-year-old Android, behind a cracked screen |
| **P3** | **Legible under stress** — sights usable when you're cold, tired, rushed | One glance from arm's length mid-set answers: which exercise, how many reps, how long left |
| **P4** | **Coarse-input operable** — glove-sized, no fine motor control | ≥48 px targets, nothing hover-only, no precision gestures, thumb-reachable |
| **P5** | **Mass-producible and cheap** — simple processes, common materials | No framework, no build, no npm, no runtime downloads, no API keys, no accounts |
| **P6** | **Inspectable and repairable** — you can see how it works, and fix it | Readable, commented, hand-editable source; data as plain JS objects; user data exportable |
| **P7** | **Self-evident operation** — the safety lever doubles as the dust cover | Each control does one obvious thing; state is always visible; no mode you can get lost in |
| **P8** | **Honest and durable** — no ornament pretending to be function | No decorative motion, no fake glow/depth; aesthetics that still look right in 2035 |

**Two caveats, stated plainly.**

1. **The legend is partly myth.** The AK's loose tolerances were born of wartime manufacturing necessity as much as genius; its "runs dirty" reputation is real but oversold, and accuracy was never its point. The useful reading is not "sloppy is good" — it is **"design so the failure modes are cheap and the working condition is the common case."**
2. **This is an engineering metaphor, not iconography.** Forge trains the body and borrows with respect from Persian, Indian, Japanese, Chinese, Nordic and Native American movement traditions. Borrow the ethos — rugged, honest, serviceable. Do **not** borrow military or weapon-stencil imagery; it would contradict the app's own tone and sit badly beside the heritage content.

---

## 2. The AK-47 test

Run these against any proposed redesign, feature, or asset. If a change fails one for cosmetic gain, it is the wrong change.

| Test | Procedure | Pass condition |
|---|---|---|
| **JAM** | Airplane mode on; cold-boot from the home screen | Every screen, glyph and timer works. Zero blank image boxes, zero fallback-font reflow |
| **SUN** | View outdoors at ~50% brightness | Numerals and labels readable. Body text ≥ 4.5:1; big numerals target ≥ 7:1 |
| **GLOVE** | Operate with gloves, one thumb, sweaty hands | Every control ≥ 48 px, no adjacent-hit errors, no drag/slider required |
| **MUD** | Load on throttled slow-3G + mid-range phone | First paint under 1 s; total transfer < ~150 KB, and all of it text |
| **COLD** | Open the source after six months away | Exercise data, palette and glyphs found in under a minute |
| **ABUSE** | Wipe storage, then repair your own logbook from the CSV export | Nothing is trapped in a place the user can't reach |

---

## 3. Where Forge stands today (measured, not vibes)

### 3.1 Already AK-47 — defend these

| Trait | Evidence in the repo | Principle |
|---|---|---|
| Single-file app, no build | `index.html` is the whole app; no bundler, no `package.json` | P1, P5 |
| Zero runtime dependencies | No `<script src>`, no CDN, no font download | P5, JAM |
| Tiny payload | `index.html` ≈ 38 KB total | MUD |
| Offline-capable | `manifest.json` + installable PWA, no external requests | P2, JAM |
| Numerals done right | `font-variant-numeric: tabular-nums` on every timer/counter | P3 |
| Coarse-input targets | `.adj-btn` is a 44×44 px box; `touch-action: manipulation` | P4 |
| Stress feedback | `:active { transform: scale(.97) }` — instant, no hover needed | P3, P4 |
| Plain, portable data | Exercise library as a plain JS object; CSV export for the logbook | P6, ABUSE |
| System font stack | `-apple-system, Segoe UI, Roboto…` — 0 KB, always present | P5, JAM |

That is a genuinely strong base. Most "polish" passes would destroy several of these.

### 3.2 Measured legibility failures

Computed contrast ratios (WCAG relative luminance) for the current tokens:

| Pair | Ratio | AA text (4.5:1) | AAA (7:1) | Where it appears |
|---|---|---|---|---|
| `#f4f4f5` on `#0a0a0a` | **18.0:1** | pass | pass | primary text, body |
| `#f4f4f5` on `#1c1c1e` | **15.5:1** | pass | pass | text inside cards ✅ |
| `#a1a1aa` on `#0a0a0a` | **7.7:1** | pass | pass | muted text on page bg ✅ |
| `#a1a1aa` on `#1c1c1e` | **6.6:1** | pass | fail | cue text, labels |
| `#e63946` on `#0a0a0a` | **4.75:1** | pass | fail | `.preview-title` |
| **`#e63946` on `#1c1c1e`** | **4.08:1** | **FAIL** | fail | adjusted values on card bg |
| **`#ffffff` on `#e63946`** | **4.17:1** | **FAIL**¹ | fail | "START SESSION", "Complete" |
| **`#ffffff` on `#2a9d8f`** | **3.32:1** | **FAIL** | fail | "Export All Data to CSV" |
| **`#27272a` on `#1c1c1e`** | **1.14:1** | **FAIL**² | fail | every card border |

¹ Passes only because that button text is large/bold; it fails for normal-size text.
² Borders and control boundaries need 3:1 under the non-text-contrast criterion to be perceivable at all. At 1.14:1 they are invisible in daylight — precisely the condition a field tool is judged on.

**Candidate fixes, verified:** brightening the red to `#ff5a67` gives **6.5:1** on page bg and **5.6:1** on card surfaces (both AA-pass). White on a deeper red `#c1121f` gives **6.2:1**. Lifting muted text to `#c3c3cb` gives **9.7:1**. Pure `#ffffff` numerals on `#1c1c1e` hit **17.0:1** — that is the "PM5 big number" territory described in §4C.

### 3.3 Drift and inconsistency

Ranked by how much each hurts the professional impression:

1. **Emoji as the primary iconography.** Every exercise's `origin` field is a platform emoji (`🇯🇵`, `⛓️`, `💪`, `🇮🇷`, `🪶`, `❄️`, `🌊`, `🧬`, `🪽`…). They render differently on iOS, Android, Windows and Linux; several are multi-codepoint sequences that degrade to tofu on older Android; and none share stroke weight, palette or optical size with the rest of the UI. **This is the single largest gap between the app and "professional."**
2. **Three unrelated accent colours.** `#e63946` (red), `#ffb703` (amber, optional badges), `#2a9d8f` (teal, export button). The teal shares nothing with the palette; it reads as an imported component.
3. **Two sources of truth for the brand mark.** The header icon is an inline `data:image/svg+xml` copy of the lightning bolt, *and* `icon.svg` exists as a separate file. They will drift on the next edit.
4. **Soft-consumer-phone styling.** Mixed radii (8/10/12/16 px) plus `box-shadow: 0 4px 15px rgba(230,57,70,.3)` glows. That is the aesthetic of a consumer app, not a tool. A rugged direction uses tighter radii and hard 1 px borders instead of glow.
5. **`user-select: none` on `<body>`.** Blocks copying a cue line or a session summary, and it is a blunt global used to solve a one-element problem.
6. **`maximum-scale=1.0, user-scalable=no` in the viewport meta.** Pinch-zoom is disabled. That fails the "Resize text" criterion and is backwards for tired eyes mid-workout or a user with low vision.

---

## 4. The reference library

Each entry: what it is → why the UI/UX is genuinely excellent → which principle(s) it demonstrates → what Forge should take from it.

### 4A. Principles canon — the "spec sheet" sources

**1. GOV.UK Design System + Government Design Principles** — the design system and 11 stated principles behind the UK's government services, used by thousands of services on any device, any bandwidth, any ability.
- *Excellent because:* it treats accessibility and low-end devices as the *default* design target rather than an accommodation, and its principles are operational, not decorative: "Do less", "Do the hard work to make it simple", "This is for everyone", "Be consistent, not uniform", "Design with data".
- *AK-47 mapping:* P1 (nothing extra), P2 (works for everyone, everywhere), P5 (plain patterns anyone can reuse), P7 (self-evident forms).
- *Forge takeaway:* "Do less" is a licence to *remove*. Adopt "be consistent, not uniform" as the rule for the heritage days: one system with many colour motifs — not one bespoke layout per culture.

**2. U.S. Web Design System (USWDS)** — the U.S. federal design system: components, patterns and **design tokens**, in service of "accessible, mobile-friendly government websites".
- *Excellent because:* everything is expressed as named tokens (colour, spacing units, typesetting, shadow, opacity), so no screen can invent its own one-off value. Nearly 200 federal sites share it.
- *AK-47 mapping:* P1, P7 (one vocabulary), P6 (inspectable, documented).
- *Forge takeaway:* Forge's `:root` custom properties are already a mini token set — but `#2a9d8f` and `#ffb703` were added outside it. **Make every colour a token, and forbid colour literals inside component rules.**

**3. Dieter Rams — Ten Principles for Good Design** (as published by Vitsœ) — the canonical statement of functional industrial design, and the lineage of "Less, but better".
- *Excellent because:* it frames design as a service to the user, not self-expression: *"good design makes a product useful… disregarding anything that could possibly detract from it"*; *"products fulfilling a purpose are like tools… neither decorative objects nor works of art"*; *"good design is long-lasting… it avoids being fashionable and therefore never appears antiquated"*; *"good design is as little design as possible… back to purity, back to simplicity"*.
- *AK-47 mapping:* essentially all eight; P8 especially.
- *Forge takeaway:* the best articulation of what "professional" means here. "Unobtrusive" and "long-lasting" argue directly *against* the current red glow shadows and large radii. The amber badge and teal button are precisely the "impenetrable confusion of forms, colours and noises" Rams was complaining about.

**4. WCAG 2.x numeric criteria** — the standard whose contrast and target-size rules are the codified version of the SUN and GLOVE tests.
- *Excellent because:* it replaces taste with thresholds: 4.5:1 normal text, 3:1 large text, 3:1 for UI component boundaries and non-text indicators, plus minimum target sizes.
- *AK-47 mapping:* P2, P3, P4.
- *Forge takeaway:* §3.2 is this criterion applied to Forge's actual tokens. Cheap to fix, immediately visible.

**5. suckless.org** — a small-systems movement, home of `dwm`, `dmenu` and `st`; a deliberate counter-position to "complex, error-prone and slow software".
- *Excellent because:* it states the doctrine Forge already lives by: *"a focus on simplicity, clarity and frugality… keeping things simple, minimal and usable"*, and *"simplicity is the heart of the Unix philosophy. The more code lines you have removed, the more progress you have made."*
- *AK-47 mapping:* P1, P5, P6.
- *Forge takeaway:* a sanity check for every asset added — **does this subtract something, or only add?** A glyph set that replaces emoji *subtracts* platform inconsistency.

**6. "Motherfucking Website" and the website-obesity critique it dramatizes** — the famous reductio of over-designed pages, closing on Rams' *"Good design is as little design as possible."*
- *Excellent because:* it names the causal chain Forge should avoid — *"lightweight and loads fast / fits on all your shitty screens / looks the same in all your shitty browsers / accessible… legible"* — and ends on *"all the problems we have with websites are ones we create ourselves."*
- *AK-47 mapping:* P1, P2, P5; the MUD and JAM tests.
- *Forge takeaway:* use it as the adversarial reviewer. Any imagery or icon proposal must answer its central insult: *what 80 KB did this add, and to whom is it invisible?*

**7. Platform touch-target guidance (Apple HIG / Material)** — vendor-blessed minimum hit sizes that make the GLOVE test concrete.
- *Excellent because:* it is empirical ergonomics — a control smaller than roughly a fingertip cannot be reliably hit under load.
- *AK-47 mapping:* P4.
- *Forge takeaway:* the 44 px `.adj-btn` already sits at the boundary. Anything new must be ≥ 48 px, and never adjacent to a destructive action without separation.

### 4B. Software that *is* the ethos

| Project | Ethos evidence | Forge lesson |
|---|---|---|
| **Hacker News** | A few KB of near-plain HTML, no images, instant on anything, essentially unchanged for ~15 years | Timeless ≠ dated. A minimal layout can *be* the brand |
| **Craigslist** | Ruthlessly functional, near-zero decoration, runs on ancient hardware, serves enormous traffic | Utility at scale looks boring on purpose |
| **Berkshire Hathaway's site** | Deliberately plain, hand-maintained, fast and reliable for decades; a credibility signal, not an oversight | Plainness reads as *confidence* in a domain where everyone else is loud |
| **GOV.UK itself** | High contrast, plain language, fast, works on old devices and with screen readers; one typographic scale everywhere | A single locked type scale plus strong contrast *is* the professional look |
| **Wikipedia** | Content-first, near-zero JS for reading, survives low bandwidth and old devices worldwide | Imagery must never be load-bearing for comprehension |
| **suckless `dwm` / `dmenu`** | Configured by editing source; no config file; minimal, keyboard-driven | Config-as-source is an honest choice for a single-author tool |
| **`vim` / `tmux` / `mutt`** | Keyboard-only, no chrome, run over SSH on terrible connections, decades of muscle memory | Instant response to coarse input beats rich input affordances |
| **`mpv` / `curl` / `sqlite` / `ffmpeg`** | Few dependencies, scriptable, boringly reliable, ubiquitous | Boring and dependable is the goal state; novelty is a cost |
| **Pinboard** | Deliberately unglamorous, fast, one-time fee, explicitly anti-venture in its ethos | Stated principles are part of the product's UX |

### 4C. Field-grade hardware & fitness UI — the most directly transferable group

**1. Gymboss interval timer** — a small physical interval timer sold since 2001 out of Michigan; a genuinely useful, genuinely cheap piece of gym equipment.
- *Excellent because:* the interface is two intervals and two buttons; marketed as "small, easy to use", "sweat and impact resistant", powered by a single AAA battery, and it notifies with **an audible beep *and* vibration**, with configurable alarm duration. It is used for HIIT, CrossFit, strength work, kettlebells, boxing and martial arts.
- *AK-47 mapping:* P1, P2, P3, P4, P5, P7 — nearly perfect.
- *Forge takeaway:* the closest existing product to what Forge's session screen should feel like. Two lessons: **(a) a timer's job is to be *noticed*, not read** — so audio + vibration + huge numerals, in that priority order; **(b) duplicated feedback channels** (beep **and** buzz) is an AK-47 move: if one fails in this environment, the other still works. Forge's timer currently has no haptic or audio cue at the interval boundary at all.

**2. Concept2 PM5 performance monitor** — the monochrome monitor bolted to rowing and SkiErg machines in gyms worldwide.
- *Excellent because:* it shows a handful of numbers — pace/500 m, watts, time, distance, stroke rate — in enormous fixed-position fields, readable from a metre away, at an angle, while the machine moves under you. It runs for a very long time on disposable batteries and is treated as abuse-proof infrastructure.
- *AK-47 mapping:* P2, P3, P5 (common batteries, no charging ritual), P8.
- *Forge takeaway:* **the "big number" doctrine.** The primary number occupies the largest type on screen; supporting numbers are smaller and **stay in the same place all session**. Forge's `2rem` timer is well below "readable from a metre away with the phone on the floor".

**3. Garmin / Suunto field watches** — wrist instruments built for trail, water and cold, with always-on transflective displays and physical buttons.
- *Excellent because:* they are legible in direct sunlight *because* they don't depend on backlight brightness; they are operable with gloves through physical buttons and large bezels; and they degrade to a reduced but still-readable surface as the battery dies.
- *AK-47 mapping:* P2 (sunlight, cold, gloves), P3, P4, P8.
- *Forge takeaway:* two ideas worth stealing. **Sunlight legibility** = maximise luminance contrast between the two colours that matter (see §3.2 → 17:1 white-on-surface). **Graceful degradation** = decide now what Forge sheds first at 5% battery mid-session (animations, then shadows, then secondary labels — never the numerals).

**4. Teenage Engineering OP-1** — a deliberately small, tactile aluminium synthesizer whose screen graphics were rebuilt screen-by-screen for the "field" revision.
- *Excellent because:* its identity comes from a **complete, coherent, minimal icon and graphics system** rendered on a tiny display, paired with physical encoders. It is built around legibility and physical feedback rather than richness — explicitly "tailor made for professionals in the field", with hardened glass, an adjustable-brightness flush display and 24-hour battery life.
- *AK-47 mapping:* P3, P4, P7, P8.
- *Forge takeaway:* **this is the model for the iconography polish.** Not "add icons" but "commission one small, complete, self-consistent screen graphics language" — a fixed vocabulary covering exactly the states Forge has, drawn once, at one optical size.

### 4D. Icon systems, ranked by AK-47 fit

| Library | License | Scale | Style | Attribution | Fit |
|---|---|---|---|---|---|
| **Health Icons** | **CC0 1.0** | Hundreds, at 24 px and 48 px, filled + outline | Deliberately plain, utilitarian; categories include blood, body, **exercise**, devices, people, places, specialties, symbols | **None required** ("no need to give credit") | ★★★★★ Built for clinics in low-resource and field settings — that *is* the ethos. Has an exercise category and a "Gym" specialty icon |
| **Game Icons** | CC BY 3.0 | 4,180+ | Monochrome black/white silhouettes; explicitly pitched for stencils and infinite scaling | Required (Lorc, Delapouite & contributors) | ★★★★★ The vocabulary Forge actually needs — Weapon (174), Tool (120), Body (158). Silhouettes read as rugged rather than cute |
| **Tabler Icons** | MIT | 6,202 (5,148 outline) | 24 px grid, 2 px stroke, outline + filled, SVG sprite/webfont | None required | ★★★★☆ Pragmatic default for UI chrome (play, pause, chevrons, timer, download); has Sport and Health categories |
| **Lucide** | ISC | ~1,600 | 24 px grid, 2 px stroke, strict consistency rules; Sports and Medical categories | None required | ★★★★☆ The cleanest stroke discipline of the mainstream sets |
| **Material Symbols** | Apache-2.0 | Thousands; variable font + SVG | Outlined / Rounded / Sharp; axes `opsz` 20–48, `wght` 100–700, `GRAD` −50–200, `FILL` 0–100 | Not required | ★★★☆☆ Google-corporate in feel, but the `GRAD` axis has a genuinely useful documented trick: **−50 is suggested for reversed contrast, i.e. white icons on a black background** — exactly Forge's case |
| Bootstrap Icons / Heroicons / Phosphor | MIT *(confirm per-package before shipping)* | 1,500–2,000+ each | Plain, 16/20/24 px grids | None required | ★★★☆☆ Fine fallbacks |

**Reject outright: icon fonts.** They add a network fetch, a font parse, and a fallback-font flash, and are a documented accessibility trap (private-use codepoints are announced as gibberish). Ship **inlined SVG** or **one SVG sprite**.

### 4E. Emoji → glyph pipeline (the highest-leverage single fix)

Forge currently uses platform emoji for every exercise `origin`. This is the app's biggest "not professional yet" signal, and it has a hard technical cause: **emoji are drawn by the operating system, so Forge does not control its own iconography.** iOS, Android, Samsung, Windows and Linux all render them differently, and Windows does not render regional-indicator flag sequences as flags at all — `🇯🇵`, `🇮🇳`, `🇮🇷`, `🇷🇺`, `🇨🇳` become bare letter pairs. Forge uses exactly those flags, plus multi-codepoint sequences (`⛓️`, `🪽`), which are the fragile ones.

Three options, in order of fit:

1. **Hand-authored inline SVG glyph set (recommended).** 20–28 glyphs, one 24 px grid, one 2 px stroke, `currentColor`, ~200–400 bytes each. Draft the vocabulary directly from the existing `origin` values so nothing is lost: the five heritage traditions, hinge, push, pull, carry, squat, rotation (mace), isometric/hold, carry distance, cold exposure, breath, crawl.
   - *Why it wins:* it removes a dependency rather than adding one (P1), is byte-cheap (MUD), renders identically everywhere (JAM), and is drawn to match the craft of Health Icons / Game Icons. It is the *only* option that makes the iconography part of the product's identity.
2. **Twemoji as a stopgap.** Graphics are **CC BY 4.0**, code is MIT; v17.0, maintained as the community fork `@twemoji/api`. Attribution is explicitly accepted as a README or About mention.
   - *Cost:* ~4,495 emoji exist, but you'd vendor only the handful you use; each is a network fetch or an inlined data URI (≈1–3 KB each, so 20 glyphs ≈ 20–60 KB).
3. **OpenMoji — read the licence first.** 4,495 emoji, colour and black-outline variants, SVG/PNG/font, by HfG Schwäbisch Gmünd students and contributors. It is **CC BY-SA 4.0 — share-alike.** Dropping share-alike artwork into an MIT-licensed project creates a real obligation around the adapted artwork. Forge's permissive-licence posture makes this a poor fit despite the black-outline style being visually ideal.

### 4F. Imagery with clean rights — and where it should come from

**Core principle: an image that doesn't load is a jammed rifle.** No hotlinking, no third-party image hosts, no API keys inside a static offline app.

| Source | Content | Rights | Notes |
|---|---|---|---|
| **The Met Open Access** | 470,000+ artworks spanning 5,000 years worldwide — including Persian, Indian, Japanese, Chinese and First Nations material | **CC0** (dataset and public-domain images) | REST API, **no key required**, 80 req/s guidance. Directly matches the heritage days |
| **Smithsonian Open Access** | 11M+ metadata records across 20+ museums and archives (Anthropological Archives, Freer/Sackler, NMAI, Cooper Hewitt…) | **CC0 1.0** | Bulk dataset via the AWS Open Data registry, plus API |
| **Wikimedia Commons** | Enormous, including historical photography and public-domain art | PD / CC BY / CC BY-SA **per file** | Check each file; beware share-alike |
| **Old Book Illustrations** | Wood engravings, etchings and photogravures from nineteenth-century books | Public domain | Style matches a rugged, engraved-plate look |
| Library of Congress · NYPL Digital Collections · Rijksmuseum · Biodiversity Heritage Library · NASA | Historical photographs, plates, technical drawings, space imagery | Mostly PD/CC0 per item | Verify the item-level rights statement |
| The Public Domain Review | Curated public-domain works with context | PD | Good for finding the right *era* of image |

Two viable strategies:

- **(a) Thematic fidelity.** Retrieve actual period imagery for the Persian / Indian / Japanese / Chinese / Nordic / Native American days from the Met, Smithsonian or LoC. This makes the imagery *mean* something instead of decorating — which is the whole difference between "professional" and "clip-art".
- **(b) Self-generated vector texture.** SVG halftone/dither, stencil plates, blueprint line work, engraved hatching, paper grain. Zero rights exposure, zero network, infinitely scalable, and it never dates.

**Budget if an image ships:** ≤ 25–40 KB after conversion (WebP, or AVIF with a fallback); art-directed dark with a single accent; always with text alternatives; and it must survive the JAM test. If it can't, it doesn't ship.

### 4G. What *not* to use — with evidence

- **Unsplash / Pexels / remote image CDNs.** Unsplash's own API guidelines require that *"all API uses must use the hotlinked image URLs returned by the API"* — so images load from their servers at runtime — plus attribution to Unsplash and the photographer, a link with UTM parameters, a ping to a download endpoint, and no use of the Unsplash name or logo in your app name or app icon. That is a direct conflict with offline-first, zero-network, no-account design, and the branding rules would block using such a photo as Forge's icon anyway.
- **`fonts.googleapis.com` hotlinking.** An external runtime dependency: fails offline (JAM), costs a DNS + TLS + font round trip (MUD), causes flash-of-unstyled-text layout shift, and leaks every user's IP to a third party. If a display face is wanted, **self-host and subset it**.
- **Remote icon CDNs and icon fonts.** Same dependency class, plus the accessibility problems in §4D.
- **Generic stock "gym" photography.** Meaning-neutral, heavy, and it dates fast — the exact opposite of Rams' "long-lasting… avoids being fashionable". It also contradicts the app's own stated character.

### 4H. Typography and numerals

- **Keep the system font stack.** It is 0 KB, always available, and it is what services at GOV.UK scale rely on. That is a feature, not a shortcut — the AK-47 move is to *not* ship a font.
- **If a display face is added**, restrict it to headings/brand, self-host it, subset it to the glyphs used, and pick something with a signage or spec-sheet temperament. Reasonable free candidates: **Oswald**, **Archivo / Archivo Narrow**, **Barlow Condensed**, **IBM Plex Sans Condensed**. For the wordmark only, a stencil cut such as **Saira Stencil One**. IBM Plex is the most "engineering-honest" of these and pairs a condensed sans with a mono companion.
- **The numerals doctrine.** The timer and the rep counters *are* the product. Tabular numerals (already in place), the largest type on screen, pure `#ffffff` on the card surface (17:1), never sharing a line with decoration, and never re-flowing position mid-session.
- **Lock one type scale.** Forge currently uses roughly fifteen distinct sizes between 0.65 rem and 2 rem. The USWDS/GOV.UK discipline is five to seven steps. Fewer sizes read as more professional and cost nothing.
- **Keep the uppercase + letter-spacing labels.** They already create an "instrument panel" feel. Apply them consistently — today some labels use it and others don't, which is the visible seam.

### 4I. Adjacent visual references

- **Super Normal** (Jasper Morrison & Naoto Fukasawa) — design "so ordinary it is excellent"; the explicit anti-spectacle position. The best single antidote to "polish means adding something".
- **Massimo Vignelli, *The Vignelli Canon*** — a short rulebook on legibility, grids, and restraint, from the NYC subway signage lineage.
- **Enzo Mari, *Autoprogettazione*** — furniture published as build-it-yourself plans. The purest expression of P6: simple enough that the owner can make and repair it.
- **Victor Papanek, *Design for the Real World*** — design as a resource-conscious, ethical act; the intellectual root of "minimise environmental impact" even entering the GOV.UK principles.
- **Field-watch legibility** (Rolex Explorer, Sinn, Garmin Instinct) — one glance, any light, no legend needed.
- **Repair-first outdoor brands** (Patagonia's repair ethos, Fjällräven) — durable goods that advertise their serviceability. Good tone reference for the heritage days.
- **Swiss / International Typographic Style** — grid, one family, one accent, no ornament.
- **Stencil-crate and blueprint drafting conventions** — the *visual grammar* of utility (stencilled labels, part numbers, callout lines, hatching) **without** borrowing weapons imagery.

**One caution when sourcing heritage imagery:** museum-held Indigenous and ceremonial material is sometimes restricted or requires community permission even when it is digitised and public-domain-flagged. Prefer the institutions' own published guidance (e.g. the National Museum of the American Indian's) and choose non-ceremonial, non-restricted images for the Apache/Sioux day specifically.

---

## 5. The shortlist — what I'd actually do to Forge

| # | Move | Reference | Effort | Risk | Improves |
|---|---|---|---|---|---|
| **1** | **Freeze the tokens.** One palette, one type scale (5–7 steps), one radius, one border treatment. Delete the teal; decide one meaning for red (act) and one for amber (optional). Forbid colour literals outside `:root`. | USWDS design tokens · Rams | S | none | P1, P7 |
| **2** | **Run the contrast pass from §3.2.** Brighten the red (or darken it behind white text), lift card borders to ≥3:1, lift muted text on cards toward 7:1. Give the numerals pure white. | WCAG | S | none (visual only) | SUN |
| **3** | **Replace platform emoji with a hand-drawn inline SVG glyph set** — ~24 glyphs, one 24 px grid, one 2 px stroke, `currentColor`. | Health Icons / Game Icons craft · OP-1's single screen language | M–L | art direction; keep glyphs non-militaristic | P1, P3, JAM |
| **4** | **Adopt the big-number timer doctrine.** Numerals ≥ 3.5–4 rem, fixed position all session, plus an **audio + haptic** cue at each interval boundary. | Concept2 PM5 · Gymboss | S–M | iOS needs a user gesture to unlock audio — unlock it on the "Start Session" tap | P3, GLOVE, SUN |
| **5** | **Unbreak the ergonomics.** Re-enable pinch-zoom, remove the global `user-select: none`, raise any control below 48 px, and separate "Wipe Logbook" from the primary actions. | WCAG · Apple/Material targets | S | none | GLOVE |
| **6** | **Harden the aesthetic.** Reduce radii to 4–8 px, drop the red glow shadows, replace depth with 1 px borders and a single red accent. | Rams ("unobtrusive", "long-lasting") | S | subjective — prototype both side by side | P8 |
| **7** | **Add imagery only two ways:** (a) an SVG texture/blueprint layer, or (b) one CC0 hero per heritage day at ≤40 KB, with an `ATTRIBUTIONS.md`. | Met / Smithsonian CC0 · Old Book Illustrations | M | weight; cultural sensitivity | P6, MUD |

**The smallest change with the biggest effect: #2 + #3 together.** The contrast pass and the glyph set are the two things a stranger notices in the first ten seconds, and neither adds a single byte of dependency. Everything else is refinement around them.

---

## 6. Where I'd want your call before moving

1. **How literal is "AK-47"?** My reading is *industrial-utility aesthetic, zero weapon imagery* — rugged, stencilled, instrument-panel, but nothing militaristic, especially given the heritage days (§1, caveat 2). Confirm or correct.
2. **Glyphs: bespoke or borrowed?** A hand-drawn set that is uniquely Forge's (best fit, more work), or adopt Health Icons + Tabler as-is (fast, less distinctive).
3. **Imagery: any at all?** Texture-only SVG (safest under the JAM test) versus real CC0 heritage photography per day (much stronger identity, more weight and sensitivity risk).
4. **How far to move the look?** Tighten toward a harsher "instrument panel" feel, or keep the current softer consumer-phone feel and only fix the measurable defects?
5. **Does the single-file rule hold?** If everything must stay inline, images and fonts have to be base64, which bloats the file and defeats the small-payload win. If a small `assets/` folder plus service-worker caching is acceptable, self-hosted subset fonts and small images become viable.

---

## 7. Sources (and what was actually verified)

| Source | Verified |
|---|---|
| `healthicons.org` | CC0; "no need to give credit"; 24 px and 48 px; filled + outline; an **exercise** category and a **Gym** specialty icon; site itself MIT |
| `openmoji.org` | CC BY-SA 4.0; 4,495 emoji; colour **and** black-outline; SVG/PNG/font; Unicode 17.0; by 80+ students and 2 professors, HfG Schwäbisch Gmünd |
| `tabler.io/icons` | MIT; 6,202 icons (5,148 outline); 24×24 grid; 2 px stroke; SVG sprite / webfont / PNG |
| `lucide.dev` | ISC licence; 24 px default; 2 px stroke; Sports and Medical categories |
| `github.com/google/material-design-icons` | Apache-2.0; axes `opsz` 20–48, `wght` 100–700, `GRAD` −50–200, `FILL` 0–100; **GRAD −50 suggested for white icons on black**; the classic set has been frozen since 2022 |
| `github.com/jdecked/twemoji` | Graphics CC BY 4.0, code MIT; v17.0 / Unicode 17.0; attribution satisfied by a README, About screen, or source mention; community-maintained fork |
| `game-icons.net` | CC BY 3.0 (Lorc, Delapouite & contributors); 4,180+ icons; monochrome SVG/PNG in four colour combinations; Weapon 174, Tool 120, Body 158; explicitly pitched for stencils |
| `gov.uk/guidance/government-design-principles` | 11 principles retrieved, incl. "Do less", "Do the hard work to make it simple", "This is for everyone", "Be consistent, not uniform", and the April 2025 addition "Minimise environmental impact" |
| `designsystem.digital.gov` | USWDS: components, patterns, **design tokens**, utilities, templates; "accessible, mobile-friendly"; ~200 government sites |
| `vitsoe.com/us/about/good-design` | All ten Rams principles retrieved verbatim, incl. "useful", "unobtrusive", "long-lasting", "as little design as possible" |
| `w3.org/WAI/…/contrast-minimum.html` | WCAG 1.4.3: **4.5:1** normal text, **3:1** large text; 18 pt or 14 pt bold counts as large |
| `suckless.org/philosophy` | "simplicity, clarity and frugality"; "simplicity is the heart of the Unix philosophy"; "the more code lines you have removed, the more progress you have made" |
| `motherfuckingwebsite.com` | The over-design argument and its closing Rams quotation |
| `metmuseum.github.io` | **470,000+** artworks; **CC0** datasets and public-domain images; REST API with **no key required**; 80 req/s guidance; bulk Open Access dataset |
| `github.com/Smithsonian/OpenAccess` | **CC0-1.0**; 11M+ metadata records; AWS Open Data registry; repo archived, data still served from S3 |
| `commons.wikimedia.org/wiki/Commons:Licensing` | Accepted-licence policy; PD / CC BY / CC BY-SA; share-alike implications |
| `help.unsplash.com` (API guidelines) | Hotlinked URLs **required**; attribution + UTM links required; download-endpoint ping; no Unsplash name/logo in app name or icon; no selling unaltered photos; no replicating the core experience |
| `gymboss.com` | Two intervals / two buttons; "small, easy to use"; "sweat and impact resistant"; one AAA battery; audible beep **and** vibration; HIIT, CrossFit, kettlebells, boxing, martial arts; family-run, Michigan, since 2001 |
| `teenage.engineering/products/op-1` | Graphics "meticulously reworked… screen by screen"; hardened glass flush display with adjustable brightness; aluminium body; 24 h battery; "tailor made for professionals in the field" |
| `oldbookillustrations.com` | Public-domain wood engravings, etchings and photogravures |

**Widely reported but not sourced here** — verify before relying on them: the Concept2 PM5's exact battery chemistry and runtime; Apple's specific 44 pt tap-target figure (the HIG pages require JavaScript to render).

### Attribution hygiene

If any attributed set is adopted, add a short `ATTRIBUTIONS.md` beside `LICENSE`, listing each source, its licence, and the exact credit line it requires. **Game Icons (CC BY 3.0)** and **Twemoji graphics (CC BY 4.0)** require a named credit; **Health Icons (CC0)**, **Tabler (MIT)** and **Lucide (ISC)** do not — though naming them is still good practice.

---

## 8. Implemented (first pass from the shortlist)

Scope taken: moves **#2 (contrast pass)** and **#3 (glyph set)** only. Moves #1, #4–#7 remain open, and two accessibility defects (§3.3 items 5–6) were deliberately left alone because they belong to move #5.

### 8.1 Contrast and tokens

`:root` now defines 16 named tokens, and **no colour literal appears anywhere else in the stylesheet** — verifiable: no `#hex` and no `rgba()` outside the `:root` block. Measured before → after:

| Role | Before | After |
|---|---|---|
| Muted text on card surface | `#a1a1aa` — 6.6:1 | `#b4b4bd` — **8.3:1** |
| Red as ink on card surface | `#e63946` — 4.08:1 ✗ | `#f2555f` — **5.1:1** |
| Red as ink on page bg | `#e63946` — 4.75:1 | `#f2555f` — **5.9:1** |
| White on the primary fill | `#fff` on `#e63946` — 4.17:1 ✗ | `#fff` on `#c1121f` — **6.2:1** |
| Control edges | `#27272a` — 1.14:1 (invisible in daylight) | `#6b6b75` — **3.2:1** |
| Container edges | `#27272a` — 1.14:1 | `#3f3f46` — 1.6:1, deliberately calmer than controls |
| Export button | `#fff` on `#2a9d8f` — 3.32:1 ✗ | neutral surface + body text — **15.5:1** |

Also fixed, found while editing: **Skip rendered borderless.** `button.action-btn { border: none }` outspecifies a bare `.btn-skip { border: … }`, so the Skip button never received the border its own rule asked for — dead CSS that had been invisible since it was written. It now uses a two-class selector so the control edge applies.

The palette went from four unrelated hues to **one red in two roles** — ink (`--accent`) and fill (`--action`) — plus a single amber for "optional". The two reds are not the drift this document complains about: a single value cannot be both a fill under white text *and* readable text on near-black. That is a measured constraint, and it is documented in the CSS next to the values. Wipe Logbook is now red *ink* on a neutral body, so the red *fill* means exactly one thing: the primary action.

### 8.2 Glyph set

15 hand-drawn glyphs on a 24×24 grid, 2 px stroke, `currentColor`, no fills — **4,133 bytes for the entire set**, about 275 bytes each, so the whole icon system costs less than a single emoji PNG.

The vocabulary: `mobility`, `hinge`, `pull`, `rotation`, `raise`, `carry`, `lunge` (movement patterns) and `persia`, `india`, `japan`, `china`, `russia`, `north`, `plains` (traditions), plus `cold`. Every exercise's `origin` emoji field became a `glyph` id.

Traditions are drawn as neutral architectural and landscape emblems — arch, ring, pine, waves, feather, kettlebell, triangle — which match the app's own names for those days ("The Sacred Ring", "The Courtyard", "The Frozen Field"). Specifically **no flags**: they were the most fragile sequences (bare letter pairs on Windows) and the least legible at small size. And no attempt to depict anyone's practice — the risk of pastiche was raised in §4F and avoided rather than guessed at.

Incidental accessibility win: emoji announced as "flag: Japan"; each glyph now carries `role="img"` and an `aria-label` such as "Japanese tradition" or "Hip hinge".

**How it was verified.** A throwaway stdlib renderer (SVG path → distance-field stroke → PNG) rasterized the glyphs at 24 px and 96 px so they could actually be looked at rather than guessed at. Four shapes failed to read on first render and were redrawn: a concentric-ring-with-ticks read as a *pause button*, a dumbbell read as the letter **H**, a diagonal staff read as a **prohibition slash**, and a chevron-plus-dot read as a **downward arrow**. `tools/glyph-preview.py` regenerates the contact sheet directly from `index.html`, so the check is repeatable without a browser, a build step, or a second copy of the data.

### 8.3 All seven moves now complete

| Move | Result |
|---|---|
| #1 One type scale, one radius scale | 16 font sizes collapsed to 7 steps plus a display size; 6 radii to 3. 25 tokens in `:root`, with no colour or size literal anywhere else in the stylesheet |
| #2 Contrast pass | done in the first pass (§8.1) |
| #3 Glyph set | done in the first pass (§8.2) |
| #4 Big-number timer and cues | timer numerals 2 rem → 3 rem and now the largest type in the app; an interval boundary fires a beep **and** a vibration; muting is a header control, persisted |
| #5 Ergonomics | pinch-zoom restored; `user-select: none` narrowed to controls; every touch target ≥ 48 px; wipe-logbook moved below a rule |
| #6 Depth removed | zero `box-shadow` in the stylesheet |
| #7 Imagery | measured vector layer; no raster assets |

### 8.4 What the second pass changed, and what it cost

**Timer.** The session seconds were 2 rem; they are now 3 rem and the largest type on screen, inside a fixed bar that never moves. §5 asked for 3.5–4 rem. 3 rem is the compromise that keeps the sticky bar under about 100 px on a 360×640 phone, which matters more than the last 8 px of numeral — reported rather than quietly rounded off.

**Cues.** `cue()` fires both channels on purpose: square-wave blips through WebAudio plus a vibration pattern. Square rather than sine because it cuts through gym noise, at the cost of sounding like a tool rather than an app. Audio is unlocked on the "Start Session" tap, since iOS requires a user gesture, and muting is remembered in `localStorage`. The harness asserts that a cue with sound on produces 2 oscillators and 1 vibration, and with sound off produces 0 and 1 — the duplication is the point, so it is tested.

**Imagery.** No raster images, for three reasons: this environment cannot fetch or process binaries, a photo is dead weight offline, and CC0 photography still carries attribution and cultural-sensitivity work that a vector layer does not. Three layers instead, each measured so it cannot erode legibility:

| Layer | Body text | Muted text | Verdict |
|---|---|---|---|
| Header hatch, 2.2% white | 14.6:1 | 7.8:1 | AAA |
| Card watermark, 5.5% white | 13.4:1 | 7.2:1 | AAA |
| Nothing at all (baseline) | 15.5:1 | 8.3:1 | AAA |

**The watermark rule.** The day's signature glyph is the *most used* glyph that is not the shared mobility reset, and on a tie a movement pattern beats a tradition mark. Without that tie-break, Day A would show the Japanese ring, inherited from the Shiko squat it shares with the Japan day — a ring watermark on a strength day would misdescribe the session.

**Cost.** `index.html` went 38 KB → 51 KB across both passes. That is a real increase against the smallest-payload principle, and the honest accounting is: 4.7 KB of glyphs, roughly 5 KB of explanatory comments (which are the point of an inspectable single-file app), and the rest is the audio engine, the service-worker registration and the imagery rules. Nothing added requires a network request, and the file remains smaller than a single mid-size photograph.

### 8.5 Two defects found that were not on the shortlist

1. **Skip had never been bordered.** `button.action-btn { border: none }` outspecifies a bare `.btn-skip`, so that rule's border had been dead since it was written. Fixed with a two-class selector.
2. **The README claimed offline support "via service worker" and no service worker existed.** The app's headline promise was unsupported: installed to a home screen, it would not reliably open without a connection. `sw.js` now precaches the three shell files, serves page loads network-first (so nobody is pinned to a stale build) and cache-first for the icon and manifest.

The first of those also means the previous commit message described the wipe button as "red ink on a neutral body" while it was still rendering neutral — the edit meant to change it had errored silently. Both are correct now, and both were caught by re-reading the file rather than trusting that an edit had applied.

