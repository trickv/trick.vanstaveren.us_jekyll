---
name: publish-post
description: >-
  Interactive checklist for announcing a new WordPress blog post: update the
  "Recent entries" list in index.md, rebuild the Jekyll site, draft a BCC email
  blast to subscribers via Gmail, and write/iterate Twitter + LinkedIn copy.
  Use after publishing a post on trick.vanstaveren.us/wp.
---

# publish-post

A guided, interactive workflow to handle the annoying manual tasks after a new
blog post goes live on the WordPress blog (`https://trick.vanstaveren.us/wp/`).
This Jekyll repo is the landing page; the blog itself is WordPress.

Run the steps **in order**, pausing for the user's approval at each gate marked
**[CONFIRM]**. Don't batch the gates — show proposed content, get the OK (or
edits), then act. The whole point is to let the user tweak copy interactively.

---

## Step 0 — Identify the post

Goal: get the post **title**, **canonical URL**, **publish date** (YYYY-MM-DD),
and a 1–3 sentence **summary / key points** to base copy on.

1. If the user gave a URL or title, use it. Otherwise, **auto-detect the newest
   post** by fetching the RSS feed:
   - `WebFetch https://trick.vanstaveren.us/wp/feed/` — extract the latest
     `<item>`: `<title>`, `<link>`, `<pubDate>` (convert to YYYY-MM-DD), and
     `<description>`/`<content:encoded>` for a summary.
2. `WebFetch` the post URL itself to read the actual content so the email and
   social copy are accurate and specific — don't write generic copy.
3. URL format is `https://trick.vanstaveren.us/wp/YYYY/MM/DD/slug/`.
4. **[CONFIRM]** Echo back the title, URL, date, and your one-line summary.

**Voice:** Match the user's style. Many posts are a "Chasing AI:" series; tone is
personal, technical, dry-witted, first-person, not markety. Read a couple of
recent post titles in `index.md` if you need a calibration.

---

## Step 1 — Update index.md

The "Recent entries" list lives under the line
`**Recent entries to [Web Log](http://trick.vanstaveren.us/wp):**` in
`index.md`. Newest is at the **top**.

1. Insert a new bullet as the first list item, immediately after that heading
   line, matching the existing format exactly:
   ```
   * [TITLE](URL) - YYYY-MM-DD
   ```
   - Use the full `https://trick.vanstaveren.us/wp/...` URL (most entries do).
   - Preserve any special characters in the title (em dashes, CJK, etc.).
2. The list currently holds ~16 entries and isn't auto-trimmed. **[CONFIRM]**
   ask whether to drop the oldest bullet to keep the count steady (default: just
   add, don't trim).
3. Make the edit with the Edit tool. Show the user the new line.

---

## Step 2 — Commit source, THEN rebuild the Jekyll site

`_site/` **is committed to this repo** (see CLAUDE.md), so the generated output
must be regenerated, not left stale.

**Order matters — commit the source edit BEFORE building.** The
`jekyll-last-modified-at` plugin is configured with `git-authordate: True`, so it
derives each page's last-modified date from git commit times. If `index.md` is
still uncommitted at build time, the generated page gets the wrong (or missing)
last-modified date. So the sequence is:

1. **[CONFIRM]** Commit the source change first, on its own:
   ```bash
   git add index.md && git commit -m "add <post title> to recent entries"
   ```
2. Then run a production build (not the dev server, to avoid baking in dev
   headers). **Prefer the `./build` Docker oneshot** — the native
   `bundle exec jekyll build` may fail on a bundler version mismatch
   (Gemfile.lock pins a bundler the system Ruby doesn't have):
   ```bash
   ./build
   ```
   (Native fallback, only if Docker is unavailable: `bundle exec jekyll build`.)
3. Expect diffs under `_site/`, especially `_site/index.html`. That's normal.
   Commit the generated output as a **second** commit:
   ```bash
   git add _site && git commit -m "regen"
   ```
4. **Do not push** unless the user asks. To publish:
   - `./push` (dry-run preview) → `./push --real` (actually rsync).
   - Escape hatch if the build picked up unwanted changes:
     `git checkout -- _site` / `./revert-generated`.

(If the user prefers, the two commits can be staged but the commit/push left to
them — but never build on top of an uncommitted source edit.)

---

## Step 3 — Draft the subscriber email (Gmail BCC blast)

The subscriber list's source of truth is a **Gmail group/label**. The Gmail
draft tool (`mcp__claude_ai_Gmail__create_draft`) only **creates a draft** (it
never sends — the user reviews and hits send) and it requires **plain email
addresses** in `bcc` (it cannot expand a Gmail group name, and there's no
Contacts API available here).

Resolve the BCC recipients in this priority order:

1. **Cached export (best UX — fully populated draft):** check for
   `~/.config/blog-publish/subscribers.txt` (one address per line, `#` comments
   allowed). This lives outside the repo so addresses are never committed. If it
   exists, read it and use those addresses as `bcc`. Mention how many recipients.
   - If the user wants to refresh it, they export the Gmail group's members to
     that file (e.g. Google Contacts → the group → export, then keep the email
     column).
2. **Fallback (no cache):** create the draft with `bcc` **empty** and tell the
   user: in the Gmail draft, type the **group name** in the BCC field — Gmail's
   web UI auto-expands it. This keeps Gmail as the single source of truth.

Then:

1. Draft the email:
   - `to`: `["trick@vanstaveren.us"]` (so it lands in the user's own inbox; real
     recipients are BCC'd for privacy).
   - `bcc`: resolved addresses (or empty per fallback).
   - `subject`: usually the post title (offer a tweak).
   - `body`: a short, personal plain-text note — a sentence or two of context in
     the user's voice + the post link + a light sign-off. Not a press release.
   - Optionally also supply `htmlBody` with the same content as a simple HTML
     version (link as an `<a>`).
2. **[CONFIRM]** Show the full draft (subject, body, recipient count, BCC
   strategy) and iterate until approved.
3. Call `mcp__claude_ai_Gmail__create_draft`. Report the returned draft ID and
   remind the user it's a **draft** — they open Gmail, sanity-check, and send.

---

## Step 4 — Twitter + LinkedIn copy (generate only)

No Twitter/LinkedIn connectors are available, so this step **produces approved
copy** for the user to post themselves. Don't claim to post it.

1. Draft both, tuned per platform:
   - **Twitter/X:** ≤ 280 chars including the URL. Punchy, one hook, the link,
     maybe 1–2 relevant hashtags only if natural. Count the characters and show
     the count.
   - **LinkedIn:** a few short paragraphs, professional but still in the user's
     voice; lead with the interesting bit, end with the link. Hashtags optional.
2. **[CONFIRM]** Present both, iterate on wording as long as the user wants.
3. On approval, output the final copy clearly in chat. Offer to also:
   - save to files (e.g. `/tmp/post-twitter.txt`, `/tmp/post-linkedin.txt`), and
   - `pbcopy` one to the clipboard for immediate pasting (macOS).
   Only do these if the user says yes.

---

## Wrap-up

Summarize what was done and what's left for the user to click:
- [x] index.md updated + site rebuilt (note if commit/push still pending)
- [ ] Gmail draft created — **user sends it**
- [ ] Social copy approved — **user posts it**

Keep it short. Don't auto-push or auto-send anything that wasn't explicitly
approved.
