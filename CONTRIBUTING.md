# Contributing to Forge Kinetic

Thanks for your interest in Forge Kinetic. This is a small, dependency-free PWA, so contributions are light-weight. Here's how to propose a change.

## Getting started

1. Fork the repo and clone it.
2. Open `index.html` in a browser, or serve it locally with a static server (see `README.md`).
3. Make your change. The whole app lives in `index.html` (markup, styles, and logic); the PWA bits are in `manifest.json` and `icon.svg`.

## What to work on

- New exercises or updates to existing exercise data (title, cues, defaults).
- New daily plans or changes to the day→exercise mappings.
- UI / UX improvements (layout, contrast, interaction, animations).
- Timer, logging, or Wake Lock behavior improvements.
- Bug fixes for session flow, history panel, or day selection.

## Style

- Keep it dependency-free. No new frameworks or build tools unless there's a clear payoff.
- Match the existing formatting: consistent indentation, same CSS variable naming, same comment style.
- Keep the single-file approach unless a change is large enough to justify splitting JS or CSS into separate files.

## Submitting a change

1. Create a branch from `main`.
2. Make your change and test it (including offline behavior if you touched the PWA bits).
3. Open a pull request with a short description of what changed and why.

## Reporting a bug

Open an issue with steps to reproduce, the browser/device, and whether it happens online, offline, or both. Include what you expected and what happened.
