---
title: Projects/Open Source/Banshee/Plugins/Lirc
permalink: wiki/Projects/Open_Source/Banshee/Plugins/Lirc/
layout: wiki
---

I haven't worked on this project since about 2006. But feel free to
enjoy the code.

This is a small plugin for the [Banshee Music
Player](http://www.banshee-project.org/) and it works great. This code
uses the [lirc-sharp](/wiki/Projects/Open_Source/Lirc-sharp "wikilink")
bindings that I have written. I use a background thread that calls
Lirc.NextCommand() which is a blocking call, and when it returns I pull
the command (which is one called from the system/user lircrc) and do as
it intends. The plugin itself is incredibly simple using this set of
bindings.

In the future I'm toying with the idea of writing a standalone
application that keeps a persistent connection with the lirc daemon, and
would interface with Banshee using it's D-Bus interface. This would also
allow Banshee to be launched remotely, and would isolate any problems
that may arise from the two programs. The only con of this approach is
that I might have to do some work to extend the Banshee D-Bus interface,
but that would be a good thing for Banshee in the long run :)

Ideas to work on:

-   **Target for first revision of plugin:**
    -   Toggling playback (play/pause) \[**toggle-playback**\]
        {*IMPLEMENTED*}
        -   individual play and pause commands too \[**play** and
            **pause**\] {*IMPLEMENTED*}
    -   Next / Previous track \[**next** and **previous**\]
    -   Fast-forward and rewind \[**fast-forward** and **rewind**\]
        {*IMPLEMENTED*}
    -   Changing Banshee's volume \[**volume-up** and **volume-down**\]
        {*IMPLEMENTED*}
    -   Mute (idea from Josiah Ritchie &lt;josiah.ritchie@gmail.com&gt;)
        \[**mute**\] {*IMPLEMENTED*}

<!-- -->

-   **Future ideas:**
    -   Changing sources
    -   Raising the window (great for when you're across the room and
        want to see the interface if it's on another workspace)
    -   Album cover enlarge (idea from Josiah Ritchie
        &lt;josiah.ritchie@gmail.com&gt;)
    -   Toggle shuffle and repeat modes (idea from Josiah Ritchie
        &lt;josiah.ritchie@gmail.com&gt;)

The source is hosted on my personal svn repository. Check out by
issuing:

`   svn co `[`http://svn.vanstaveren.us/banshee-lirc-plugin`](http://svn.vanstaveren.us/banshee-lirc-plugin)

------------------------------------------------------------------------

The compilation of this plugin isn't just plug 'n chug, but almost as
easy...

-   First, compile and install
    [lirc-sharp](/wiki/Projects/Open_Source/Lirc-sharp "wikilink").
-   Check out the source here, and install it. I recommend using the
    --enable-user-plugin flag so it installs to
    ~/.gnome2/banshee/plugins.
-   Before you start banshee you need to manually copy the lirc-sharp
    library files into your plugins dir. The Makefile does not
    automatically do this for you. Just run:

`   cp /usr/lib/lirc-sharp/* ~/.gnome2/banshee/plugins`

Then, start Banshee :) That should do the trick!

Feel free to report bugs to me [via e-mail](/wiki/Contact "wikilink")!
