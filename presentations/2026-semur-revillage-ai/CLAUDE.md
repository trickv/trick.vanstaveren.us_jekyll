# AI coffee & chat — Semur-en-Auxois

A ~10-minute lightning talk deck for a Revillage coffee-chat session in
Semur-en-Auxois, September 2026, by Trick (Patrick) van Staveren. Talk
arc: what AI/agents are in 2026 → a live demo → how it reframes remote
work and family life → a couple of interactive/discussion beats → a
challenge to go build or learn something before the group disbands.

Originated in this Claude chat: https://claude.ai/share/0959e0bf-d8c8-448e-b96c-d0b753d2cbff

## Files

- `ai-coffee-chat.html` — the deck itself. Single self-contained file,
  no build step, no dependencies beyond two Google Fonts.
- `serve.py` — stdlib-only local server that also powers a phone remote.
- `remote.html` — the phone-remote page `serve.py` serves at `/remote`.

## `ai-coffee-chat.html` structure

Presenting: open the file directly in a browser (`file://`), or run
`serve.py` and open `http://localhost:8765/`.

- Each slide is a `<section class="slide">` inside `<main class="deck">`.
  Only one has `.active` (`display:flex`) at a time; all others are
  `display:none`. Slides are plain content — headline styles (`h1`,
  `h1.xl` for huge titles, `h1.q` for question-style prompts), body
  styles (`.sub`, `.small`, `.line`, `.beat` for the big pull-quote
  lines), and layout helpers (`.stack` for vertical rhythm, `.rule` for
  hairline dividers between stacked lines, `.two` for a two-column
  split, `.cloud` for the word-cloud slide).
- `.slide.wine` swaps to the dark/wine background for emphasis slides
  (color contrast is handled by the `.wine` variant rules for `.sub`,
  `.small`, `.rule`).
- `.frag` marks an element that's hidden until advanced to explicitly
  (a fragment/build reveal within a slide); `.frag.on` reveals it.
  Elements without `.frag` on a slide just show immediately when the
  slide becomes active. `next()`/`prev()` reveal or hide one fragment
  at a time before moving to the next/previous slide.
- Each slide can carry an `<aside class="notes">` — speaker notes,
  never shown on the slide itself, only in the bottom notes panel
  (toggled with `N`) and mirrored to the phone remote.
- Numbered HTML comments (`<!-- 1 -->`, `<!-- 2 -->`, …) above each
  `<section>` are just a bookkeeping aid for editors — they track slide
  order and must be kept sequential/renumbered by hand whenever a slide
  is inserted, removed, or reordered. They have no functional role.
- All deck logic (advance/rewind, fragment reveals, keyboard/touch/click
  navigation, fullscreen, notes panel, hash-based deep-linking) lives in
  the inline `<script>` at the bottom. No external JS.

Controls: arrow keys/space/click to advance, click left ~22% of screen
or swipe right to go back, `N` toggles speaker notes, `F` toggles
fullscreen, `Home`/`End` jump to first/last slide.

## `serve.py` / phone remote

`serve.py` is a stdlib-only `http.server` that does two things at once:

1. Serves the deck itself as static files (`/` → `ai-coffee-chat.html`,
   `/remote` → `remote.html`, everything else served from the directory
   normally).
2. Runs a tiny pub/sub relay so a phone can drive the laptop's deck:
   - The deck's own JS detects it's being served over `http://` (as
     opposed to opened as a local `file://`) and, on every slide/
     fragment change, `POST`s its current state (slide index, title,
     next slide's title, fragment progress, notes HTML) to `/state`.
   - Any client — the deck or the phone remote — can `POST` a JSON body
     to any path; the server doesn't care about the path, it just
     broadcasts the raw body to every connected listener and, if the
     body is a `type: "state"` message, remembers it as `last_state`
     (so a client connecting mid-talk immediately gets caught up).
   - All clients subscribe over Server-Sent Events at `/events` to
     receive that broadcast stream in real time.
   - `remote.html` renders the deck's current title/next-slide/notes
     from incoming `state` messages, and sends `{type:"cmd", action:
     "next"|"prev"|"goto"|"notes"}` messages that the deck's `EventSource`
     listener turns into calls to its own `next()`/`prev()`/`show()`/
     notes-toggle — i.e. the remote never touches the deck directly, it
     just asks the server to rebroadcast a command that the deck (also
     listening on `/events`) acts on itself.
   - `addresses()` prints the LAN and/or Tailscale IP on startup so you
     know what to type into the phone (`http://<ip>:8765/remote`).

Run with `python3 serve.py [port]` (default port `8765`). Anyone who can
reach the port can drive the deck, so keep it on a trusted network (a
Tailscale tailnet, in practice) rather than exposing it publicly.

## Conventions to preserve when editing

- Keep slides terse — this is a spoken talk, not a document. Long
  explanation belongs in `<aside class="notes">`, not on the slide face.
- New reveal-on-tap content gets `class="line frag"` (or `"beat frag"`);
  content that should just appear with the slide gets the class without
  `frag`.
- Match the existing palette/CSS custom properties (`--paper`, `--ink`,
  `--wine`, `--slate`, `--ochre`, `--rule`) rather than introducing new
  colors.
- Renumber the `<!-- N -->` comments after inserting, deleting, or
  reordering slides so they stay sequential.
