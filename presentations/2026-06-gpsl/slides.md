---
theme: nord
title: "GPSL 2026 — Chasing Balloons with an AI Pair Programmer"
transition: slide-left
routerMode: hash
colorSchema: light
---

<div class="hero-branding" />

<div class="hero-content">

# Chasing Balloons with an AI Pair Programmer

Building radiosonde & HAB software with Claude Code

</div>

<div class="hero-byline">
  <span class="px-2 py-1 rounded bg-white bg-opacity-10">Patrick van Staveren · KD9PRC · Great Plains Super Launch 2026 · Pella, IA</span>
</div>

<style scoped>
.hero-content {
  position: relative;
  z-index: 1;
}
.hero-branding {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 4.5rem;
  height: 44%;
  background-image: url('/cover-branding.png');
  background-repeat: no-repeat;
  background-position: center bottom;
  background-size: contain;
  opacity: 0.9;
  pointer-events: none;
  z-index: 0;
}
.hero-byline {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 2rem;
  text-align: center;
  z-index: 1;
}
</style>

<!--
Open warm: welcome to GPSL. I'm not here to sell you on AI — I'm here to show
you what I actually built for OUR hobby over the last several months, almost
all of it with an AI coding assistant riding shotgun. Set expectation: this is
a builder's show-and-tell, ending with an open conversation.
-->

---

# Agenda

- **Who I am** — and how I got to the launch field
- **rdzSonde** — porting a radiosonde receiver app to iOS with Claude Code
- **More balloon hacks** — the little tools, plus an experimental chase-commentary app
- **Open questions** — where AI coding helps, where it doesn't, what you're seeing

<!--
Four beats. First three are show-and-tell; the last one flips it around and I
want to hear from the room. Roughly: 5 / 12 / 10 / open-ended.
-->

---
layout: section
---

# Who I am

---
layout: two-cols
---

<ParticleField />

# Patrick van Staveren <span class="callsign">KD9PRC</span>

- Independent tech consultant & solopreneur — **V9N Consulting**
- Grew up in Michigan, studied Computer Science, Western Michigan University
- Chicago → **Shanghai** → **London** → back to the Chicago suburbs
- Left a long career at Mintel in 2025 to go independent
- Photography, running, biking, **balloons and radios**

::right::

<div class="pl-6">

**Happiest when my radio is locked onto a balloon I'm about to launch.**

- Launching & chasing high-altitude balloons as a hobby
- Building my own trackers (Meshtastic, RTTY, LoRa, Wenet)
- Radiosonde recovery & reflashing (DFM17)


</div>

<style scoped>
.callsign {
  font-size: 0.5em;
  font-weight: 600;
  letter-spacing: 0.1em;
  vertical-align: middle;
  opacity: 0.75;
  margin-left: 0.4em;
}
</style>

<!--
Hi I'm Patrick, kd9prc. I got into ballooning by chance ten years ago, buying
an Uputronics GPS board to play with NTP, only to see the balloon silk-screened
on the PCB. I stumbled across UKHAS and went to a conference in 2017 and knew I
needed to build my own trackers and launch a balloon. A few years later I got
into tracking radiosondes, and I chase a few whenever I can between having three
young kids.

About a year ago I left my big-company job for a career break and ended up doing
contract IT work — using, and now teaching, Agentic Coding with Claude Code.
Most of what I'll talk about today somehow stems from my slippery slope into
becoming an SME on AI agents, and how I'm applying that to ballooning.

Then keep it tight — the room cares more about the balloons than the CV. The one
line that matters: I'm a hobbyist who started letting an AI write most of my
code about a year ago, and it changed how much I can ship for this hobby.
-->

---

# AI never really did it for me...

<div class="text-lg opacity-90 -mt-2 mb-4">...until I learned to <strong>write code</strong> with it. Then I knew this would change everything.</div>

<div class="cicada-buddy" />

<style scoped>
.cicada-buddy {
  position: absolute;
  right: 1.5rem;
  bottom: 1rem;
  width: 150px;
  height: 150px;
  z-index: 10;
  background-image: url('/cicada.svg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  filter: drop-shadow(0 6px 10px rgba(0,0,0,0.35));
  animation: cicada-bob 3.2s ease-in-out infinite;
}
@keyframes cicada-bob {
  0%, 100% { transform: rotate(-6deg) translateY(0); }
  50%      { transform: rotate(-3deg) translateY(-8px); }
}
</style>

<div class="grid grid-cols-3 gap-6 mt-2">

<div>

### What is "AI"?
A model that predicts the next bit of text. Chatbots, autocomplete. Genuinely clever — but on its own it just *talks*.

</div>

<div>

### What is an **agent**?
That same model put in a **loop with tools**: it reads files, runs commands, sees the result, and tries again. It doesn't just answer — it *does*.

</div>

<div>

### Why this works for code
Code is text the agent can write **and** instantly test. It runs or it doesn't. That tight, self-checking feedback loop is exactly what an agent is good at.

</div>

</div>

<!--
The personal arc — this is the slide where I get the non-coders on board.

For years AI never clicked for me. Chatbots were a fun party trick; I'd ask
something, get a plausible paragraph back, shrug, and move on. It didn't change
anything I actually did.

The turning point was the CICADA MIC project — [SPEAKER: tell the story —
what I was trying to build, how I was writing the code *with* the AI rather than
just chatting at it, and the moment it iterated to something that actually
worked]. That was when it flipped from "neat" to "this changes everything,"
because I wasn't reading its homework — I was watching it build, run, fail,
and fix in a loop.

Then walk the three boxes left-to-right, keep each to a sentence:
- AI = next-token predictor; on its own it only talks.
- Agent = that model in a loop with tools; it can act, observe, retry.
- Coding = the perfect playground: code is text it writes, and it's instantly
  testable, so the agent can check its own work without me in the loop.

Land on: that's why the rest of this talk is full of finished projects instead
of half-finished ideas.
-->

---
layout: statement
---

# Everything that follows was built
# *with* an AI coding assistant

Mostly **Claude Code** — an agentic CLI that reads my repo, writes code, runs it, and iterates.

<!--
Define the tool plainly for the non-coders: it's not autocomplete. It's an
agent that lives in my terminal, can see the whole project, makes changes,
runs them, reads the errors, and tries again. I'm the navigator; it drives.
-->

---
layout: section
---

# rdzSonde
### Porting a radiosonde receiver to iOS

---

# What is rdzSonde?

- An **iOS port** of [`rdzwx-go`](https://github.com/rdzSonde/rdzwx-go) — the receiver/companion app for the popular **TTGO / ESP32 LoRa radiosonde receiver**
- Talks to your TTGO over your **WiFi** (mDNS/Bonjour)
- On your phone you get:
  - A **live map** of every sonde the receiver is hearing
  - **Distance & bearing** from you to each sonde
  - **Landing predictions** via the Sondehub Tawhiri API
  - Push **your GPS** to the receiver so it can compute relative bearings
- **Privacy-first:** no accounts, no analytics, no backend — nothing leaves your devices

<!--
Many own and use a TTGO receiver, but the existing app story is thin.
There wasn't an iOS app, and the Android app required sideloading.
My goal: put the same map-and-chase workflow in everyone's pocket.
-->

---
layout: image-right
image: /rdzsonde.png
backgroundSize: contain
---

# In the chase car

- Glance-able map oriented around **you**
- Tap a sonde → distance, bearing, predicted landing
- Works alongside the TTGO already velcroed to your dash

<!--
This is the screen people will actually use with one hand while driving (or
better, while their navigator drives). Tell a recovery story here if time.
-->

---

# Building it with Claude Code

The interesting work wasn't the map — it was making a cross-platform app behave on iOS:

- **iOS Local Network permission** — Bonjour discovery silently fails without the right `Info.plist` entitlements; the agent diagnosed it from the symptoms
- **mDNS / Bonjour** discovery of `_jsonrdz._tcp` then a raw **TCP** read loop
- **App Store review** scaffolding — privacy manifest, a real **privacy policy**, screenshots, metadata
- Wrangling the **Go + web + native** wrapper toolchain into something that builds and signs

<div class="text-sm opacity-80 mt-4">

I drove the decisions; the agent did the grinding — reading errors, trying fixes, and explaining the iOS quirks I'd never have known.

</div>

<!--
This is the heart of the rdzSonde section. Honest take: the AI didn't "know"
how to ship an iOS app any more than I did, but it iterated through the iOS
networking + signing maze far faster than I would have solo. Mention the
privacy policy is published on my site as a concrete artifact.
-->

---
layout: section
---

# More balloon hacks
### Small tools, fast, because the AI does the typing

---

# A year of little balloon tools

<div class="grid grid-cols-2 gap-x-8 gap-y-3 mt-2">

<div>

**On the payload**
- `meshtastic-hab-bot-v2` — onboard app paired with a Meshtastic node
- `sondehub-meshtastic-mqtt-gateway` — bridge HAB beacons into Sondehub Amateur
- `radio_flyer` — Python payload tracker

</div>

<div>

**On the ground / in the car**
- `sonde-notifier` — follows my location in Home Assistant, pings me about nearby sondes
- `aircraft-balloon-proximity` — how close do sondes come to aircraft?
- TTGO / rdz tinkering

</div>

</div>

<div class="text-sm opacity-80 mt-6">

None of these would have gotten off my TODO list without an assistant doing the boilerplate.

</div>

<!--
Don't read every repo — pick two the room will react to (sonde-notifier and
aircraft-balloon-proximity tend to land). The point of the slide is volume:
these are all weekend-sized ideas that AI made actually finishable.
-->

---
layout: center
class: text-center
---

# Experimental: a live **chase-commentary** app
🎈🎙️

Turning live telemetry into spoken play-by-play during a chase

<div class="text-sm opacity-70 mt-6">[ live demo / screen recording ]</div>

<!--
SPEAKER: fill in the real specifics before the talk —
- what it ingests (Sondehub feed? TTGO? my own GPS?)
- what it produces (TTS audio? on-screen ticker? altitude/burst/descent callouts?)
- the fun failure modes
This is the "wow / laugh" slide — demo it live if the venue network cooperates,
otherwise play a recording. Keep it loose; it's explicitly experimental.
-->

---
layout: section
---

# Open questions
### Let's talk about this AI stuff

---

# What I'm still chewing on

- **Where does it actually help?** Boilerplate & unfamiliar platforms = huge. Novel algorithms = less so.
- **Do you trust code you didn't write?** How I review, test, and what I refuse to ship blind
- **Skill atrophy** vs. leverage — am I still learning, or just steering?
- **Cost & lock-in** — subscriptions, models changing under you, offline/privacy
- **For our hobby:** what *should* we be building now that the typing is cheap?

<div class="text-lg mt-6 opacity-90">What are <strong>you</strong> seeing? What should I try next?</div>

<!--
This slide is the real point of the section — open the floor. Have 2-3 of my
own opinions ready in case the room is quiet, but the goal is discussion, not
a lecture. Collect ideas; some will become next year's projects.
-->

---
layout: center
class: text-center
---

# Thanks! 🎈

Patrick van Staveren · KD9PRC

[trick.vanstaveren.us](https://trick.vanstaveren.us) · [github.com/trickv](https://github.com/trickv)

<div class="text-sm opacity-70 mt-4">rdzSonde: github.com/rdzSonde/rdzwx-go</div>
