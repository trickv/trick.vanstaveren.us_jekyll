---
title: Projects/Open Source/Lirc-sharp
permalink: wiki/Projects/Open_Source/Lirc-sharp/
layout: wiki
---

These bindings aren't perfect, but will make for a great starting point
for anyone who wants to capture LIRC button presses in a C\# program.

This was designed and tested on lirc 0.8.0 only. It should be backwards
compatible for anyone running older libraries - the API hasn't changed
in years.

I have written a [simple proof-of-concept
plugin](/wiki/Projects/Open_Source/Banshee/Plugins/Lirc "wikilink") for the
[Banshee Music Player](http://www.banshee-project.org).

It uses some icky C glue...if anyone's a real interop pro and
understands how to keep a C file descriptor alive between function
calls, let me know. Maybe we can get rid of the C glue :)

Right now I'm keeping the code in my personal svn repository. You can
check out a copy by issuing the following command:

`   svn co `[`svn://sting.vanstaveren.us/trunk/lirc-sharp`](svn://sting.vanstaveren.us/trunk/lirc-sharp)

You can also [view the source
online](http://sting.vanstaveren.us:8000/trunk/lirc-sharp).
