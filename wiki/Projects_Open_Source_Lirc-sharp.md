---
title: Projects/Open Source/Lirc-sharp
permalink: wiki/Projects/Open_Source/Lirc-sharp/
layout: wiki
---

lirc-sharp is a set of Mono/.NET bindings for the LIRC Client Library. I
haven't worked on this project since 2006.

The latest pre-release of lirc-sharp is version
[0.0.9](/wiki/Projects/Open_Source/Lirc-sharp/Releases/0.0.9 "wikilink"). This
is a development version and I do not expect it to work perfectly for
everyone. Send bug reports to me [via e-mail](/wiki/Contact "wikilink").

This was designed and tested on lirc 0.8.0 only. It should be backwards
compatible for anyone running older libraries - the API hasn't changed
in years.

I have written a [simple proof-of-concept
plugin](/wiki/Projects/Open_Source/Banshee/Plugins/Lirc "wikilink") for the
[Banshee Music Player](http://www.banshee-project.org).

I am also working on another project called
[lirc-dbus-relayer](/wiki/Projects/Open_Source/Lirc-dbus-relayer "wikilink")
which will relay specified LIRC commands to D-Bus enabled applications.

It uses some C glue...if anyone's a real interop pro and understands how
to keep a C file descriptor alive between function calls, let me know.
Maybe we can get rid of the C glue :)

This project's code can be found at
<http://svn.vanstaveren.us/lirc-sharp>
