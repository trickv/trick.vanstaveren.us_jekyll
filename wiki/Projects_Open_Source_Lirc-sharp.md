---
title: Projects/Open Source/Lirc-sharp
permalink: wiki/Projects/Open_Source/Lirc-sharp/
layout: wiki
---

lirc-sharp is a set of Mono/.NET bindings for the LIRC Client Library.

The latest pre-release of lirc-sharp is version
[0.0.9](/wiki/Projects/Open_Source/Lirc-sharp/Releases/0.0.9 "wikilink"). This
is a development version and I do not expect it to work perfectly for
everyone. Send bug reports to me [via e-mail](/wiki/Contact "wikilink").

**News:**

<rss><http://trick.vanstaveren.us/wp/category/projects/lirc-sharp/feed%7Cdate%7Cmax=5%7Ccharset=UTF-8%7Clong%7Cfullcontent%7Cnotitle></rss>

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

Right now I'm keeping the code in my personal svn repository. You can
check out a copy by issuing the following command:

`   svn co `[`svn://sting.vanstaveren.us/trunk/lirc-sharp`](svn://sting.vanstaveren.us/trunk/lirc-sharp)

You can also [view the source
online](http://sting.vanstaveren.us:8000/trunk/lirc-sharp).
