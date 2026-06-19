---
theme: academic
title: "GPSL 2026 — Chasing Balloons with an AI Pair Programmer"
transition: slide-left
routerMode: hash
colorSchema: light
layout: default
class: cover-slide
---

<div class="cover-title">

# Chasing Balloons with an AI Pair Programmer

<div class="cover-sub">Building radiosonde &amp; HAB software with Claude Code</div>

</div>

<div class="hero-branding" />

<div class="hero-byline">Patrick van Staveren · KD9PRC · Great Plains Super Launch 2026 · Pella, IA</div>

<style scoped>
.cover-title {
  position: absolute;
  top: 3rem;
  left: 0;
  right: 0;
  padding: 0 3.5rem;
  z-index: 1;
}
.cover-title h1 {
  font-size: 3.2rem;
  line-height: 1.12;
  margin: 0;
}
.cover-sub {
  font-size: 1.35rem;
  opacity: 0.65;
  margin-top: 0.6rem;
}
.hero-branding {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 3.25rem;
  height: 46%;
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
  bottom: 1rem;
  text-align: center;
  font-size: 1.05rem;
  opacity: 0.85;
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

- **Who I am** - and how I got to the launch field
- **How I got into AI**
- **rdzSonde** - porting a radiosonde receiver companion app to iOS with Claude Code
- **Open discussion** - where AI coding helps, where it doesn't, what you're seeing

<!--
Four beats. First three are show-and-tell; the last one flips it around and I
want to hear from the room. Roughly: 5 / 12 / 10 / open-ended.
-->

<ParticleField />

---
layout: section
---

# Who I am

---
layout: image-right
image: /IMG_1601.JPG
class: who-am-i
---


# Patrick van Staveren <span class="callsign">KD9PRC</span>

- Independent tech consultant & solopreneur — **V9N Consulting**
- Grew up in Michigan, studied Computer Science, Western Michigan University
- Chicago → **Shanghai** → **London** → back to the Chicago suburbs
- Left a long career at Mintel in 2025 to go independent
- Photography, running, biking, **balloons and radios**


**Happiest when my radio is locked onto a balloon I'm about to launch.**

- Launching & chasing high-altitude balloons as a hobby
- Building my own trackers (Meshtastic, RTTY, LoRa, Wenet)
- Radiosonde recovery & reflashing (DFM17)


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

<style>
/* Give the text 70% and the photo ~30% so all the copy fits.
   Keyed off the slide's `class: who-am-i` so reordering slides is safe. */
.grid:has(> .who-am-i) {
  grid-template-columns: 70% 30% !important;
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

# How I got into AI

AI never really did it for me
<div class="text-lg opacity-90 -mt-2 mb-4">...until I learned to <strong>write code</strong> with it. Then I knew this would change things.</div>

<div class="cicada-buddy" />

<style scoped>
.cicada-buddy {
  position: absolute;
  right: 2rem;
  bottom: 1.5rem;
  width: 190px;
  height: 190px;
  z-index: 10;
  background-image: url('/cicada-outline.svg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  opacity: 0.9;
}
</style>


<!--

For years AI never clicked for me. Chatbots were a fun party trick; I'd ask
something, get a plausible paragraph back, shrug, and move on. It didn't change
anything I actually did.

The turning point was the CICADA MIC project — [SPEAKER: tell the story —
what I was trying to build, how I was writing the code *with* the AI rather than
just chatting at it, and the moment it iterated to something that actually
worked]. That was when it flipped from "neat" to "this changes everything,"
because I wasn't reading its homework — I was watching it build, run, fail,
and fix in a loop.

In 2025, about a year ago, I left my big company job for a career break, some time with
my kids (you certainly heard them yesterday.)  I ended up doing some contract work, 
had the time/energy to learn AI coding before it became valuable, and now I teach
classes on Claude Code.

-->

---
layout: section
---

# rdzSonde
### Porting a radiosonde receiver companion app to iOS

---

# What is rdzSonde?

- An **iOS or Android app** also called [`rdzwx-go`](https://github.com/rdzSonde/rdzwx-go) — the receiver/companion app for the popular **TTGO / ESP32 LoRa radiosonde receiver**
- Talks to your TTGO over your **WiFi** (mDNS/Bonjour)
- On your phone you get:
  - A **live map** of every sonde the receiver is hearing
  - **Distance & bearing** from you to each sonde
  - **Landing predictions** via the Sondehub Tawhiri API
  - Push **your GPS** to the receiver so it can compute relative bearings

<!--
Many own and use a TTGO receiver, but the existing app story is thin.
There wasn't an iOS app, and the Android app required sideloading.
My goal: put the same map-and-chase workflow in everyone's pocket.
-->

---
layout: image-right
image: /rdzSonde2.png
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

# Getting there with Claude Code

This started as an experiment: how far can I get a coding agent to go?

The end result: rdzSonde is available in testing on Apple/Google stores today.

Google: https://play.google.com/apps/internaltest/4701410666610803801

Apple: https://testflight.apple.com/join/5aQNkGnv

<!--

The answer to my question is: **quite far**

App development and porting is something that I can do technically, but probably 
would have never gotten the time for.

AI helped me navigate the app release pipeline too, configuring Github Actions to
publish to both stores automatically.

Today: I've been in touch with DL9RDZ Hansi Reiser to merge in changes and he's given me the thumbs up to publish.
It might be live on the Apple App Store today!
For Google I need another ten testers or so first.
-->

---
layout: center
class: text-center
---

# Experimental: a live **chase-commentary** app

Turning live telemetry into play-by-play during a chase

<div class="mt-8 text-xl">

Follow tomorrow's flight: [**@KD9PRC_balloon**](https://mastodon.social/@KD9PRC_balloon)

</div>

<!--
Ingests data from several receivers, including imagery, and runs them through an AI model.
Provides commentary. The idea is for those non-technical folks like my mom to have something to read during a flight.
I've gone so experimental that not only has AI written the code, but I have an AI Agent whose job it is to monitor the code telemetry during flight Saturday and has authorization to modify the code in-flight. (No, it's not on board!)
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
- **Open source communities** have mixed perspectives - understandably
- **Skill atrophy** vs. leverage - am I still learning, or just steering?
- **Cost & lock-in** - subscriptions, models changing under you, offline/privacy
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
