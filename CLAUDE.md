# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal website/blog originally created in MediaWiki in 2006, migrated to Jekyll in 2018 using peterjc/mediawiki_to_git_md. The site contains historical content including wiki pages, computer documentation, and personal projects.

## Development Commands

### Setup

**Native setup:**
```bash
sudo apt install ruby-bundler ruby-dev make
bundle config set --local path 'vendor/bundle'
bundle install

# Apply required patch to jekyll-last-modified-at plugin
cd vendor/bundle/ruby/*/gems/jekyll-last-modified-at-1*/lib/jekyll-last-modified-at
curl https://github.com/trickv/jekyll-last-modified-at/commit/ae8f326499c59c485b47833991a1bc849f70e6ae.patch | patch -p3
```

**Docker setup:**
```bash
docker run --name jekyll_builder --volume="$PWD:/srv/jekyll:Z" -it jekyll/jekyll:3 bash
# Ctrl+D to exit
docker start jekyll_builder
```

### Development Server

**Native:**
```bash
bundle exec jekyll serve --livereload [--incremental]
```

**Docker (using helper script):**
```bash
./develop
# Runs on ports 4000 (site) and 4001 (livereload) with incremental builds
```

**Docker (manual):**
```bash
docker exec -it jekyll_builder jekyll serve --livereload --incremental
# OR for build-only with watch:
docker exec -it jekyll_builder jekyll build --incremental -w
```

### Build & Publish

**Build:**
```bash
./build  # Uses oneshot Docker container with Jekyll 3
# OR native:
bundle exec jekyll build
```

**Publish:**
```bash
./push           # Dry run - preview changes
./push --real    # Actually push to remote server (hg.v9n.us)
```

**Important:** Before pushing with `--real`, run `bundle exec jekyll build` (not the development server) to avoid pushing local dev headers live.

## Architecture

### Content Organization

- **Root markdown files:** `index.md`, `about.md`, `Contact.md` - top-level pages
- **wiki/**: Legacy MediaWiki content converted to markdown, uses `layout: wiki`
- **Computers/**: Computer/server documentation organized by hostname
- **_site/**: Generated output (excluded from git)

### Layouts

- `_layouts/wiki.html` - For wiki pages, displays tags and links to category pages
- `_layouts/tagpage.html` - For tag/category pages
- Custom headers/footers in `_includes/`

### Jekyll Configuration

- Theme: minima (~> 2.0)
- Jekyll version: 3.9.3
- Markdown: kramdown with GitHub Flavored Markdown parser
- Custom plugin: `jekyll-last-modified-at` (forked version from trickv/jekyll-last-modified-at)
  - Configured with `git-authordate: True`
  - **Requires manual patching after bundle install** (see Setup)

### Deployment

The site is deployed to a remote server via rsync. The `push` script:
- Syncs `_site/` to `hg.v9n.us:/var/www/trick.vanstaveren.us/`
- Excludes the `wp` directory
- Defaults to dry-run mode for safety
- Uses `--delete-after` to remove stale files

## Key Technical Details

- Jekyll 3 is pinned (not 4) - uses Docker image `jekyll/jekyll:3`
- The jekyll-last-modified-at plugin fork contains patches that must be manually applied
- The site predates modern Jekyll conventions and retains MediaWiki URL structure (`/wiki/Category%3A...`)
- Tag links in wiki pages use URL encoding for category pages
