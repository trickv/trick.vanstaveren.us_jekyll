---
title: Projects/Open Source/Banshee/MTP
permalink: wiki/Projects/Open_Source/Banshee/MTP/
layout: wiki
---

Subpages:
[Compatibility](/wiki/Projects/Open_Source/Banshee/MTP/Compatibility "wikilink")
[FAQ](/wiki/Projects/Open_Source/Banshee/MTP/FAQ "wikilink")
[Icons](/wiki/Projects/Open_Source/Banshee/MTP/Icons "wikilink") [Known
Bugs](/wiki/Projects/Open_Source/Banshee/MTP/Known_Bugs "wikilink")
[Patches](/wiki/Projects/Open_Source/Banshee/MTP/Patches "wikilink")
[Playlists](/wiki/Projects/Open_Source/Banshee/MTP/Playlists "wikilink") [To
Do](/wiki/Projects/Open_Source/Banshee/MTP/To_Do "wikilink")

About MTP
---------

Check out the [Media Transfer
Protocol](http://en.wikipedia.org/wiki/Media_Transfer_Protocol) page on
[Wikipedia](http://www.wikipedia.org).

MTP stands for the Media Transfer Protocol. While it is a standard
created and used almost solely by Microsoft, it is becoming a popular
interface for newer Digital Audio Players. Seeing this growth in MTP
players, the need for an open-source implementation became necessary.
Thus, a handful of projects were born to try to communicate with these
devices. libgphoto2 made some pokes & prods at MTP devices, and the
libmtp project was established by some of the libnjb/gnomad2 developers
in the desire to support these newer devices. Since then, libmtp and
libgphoto2 have joined forces and collaborated to help each other out.
As of right now, they are basically the same base of code with two
different interfaces, and were originally forked from the same base of
code (libptp2).

Banshee.Dap.Mtp uses [libgphoto2](http://www.gphoto.org).

Supported Devices
-----------------

Check out the
[compatibility](/wiki/Projects/Open_Source/Banshee/MTP/Compatibility "wikilink")
page. [Contact](/wiki/Contact "wikilink") me if there are changes to be made
to this list!

How to install
--------------

Sometimes I keep some patches against Banshee CVS for MTP. If so, you
can find them on the [MTP
Patches](/wiki/Projects/Open_Source/Banshee/MTP/Patches "wikilink") page.

### Remove old packages

First, be sure that you have removed any distribution packaged software
such as libgphoto2, gphoto2, and banshee. If you fail to do this, the
installation will most likely have problems.

### Grabbing the latest libgphoto2

libgphoto2-sharp is now installed directly out of the libgphoto2
subversion tree. In the future (2.2.2 hopefully) libgphoto2 will
distribute with the -sharp binding, but for now you will need to work
with a svn version.

Snag yourself a copy of libgphoto2 from subversion:

`  svn co `[`https://svn.sourceforge.net/svnroot/gphoto/trunk/libgphoto2`](https://svn.sourceforge.net/svnroot/gphoto/trunk/libgphoto2)

and build it, like normal:

` ./autogen.sh`

If you get an error like
[this](/wiki/Projects/Open_Source/Banshee/MTP/FAQ#Q:_What_does_this_mess_mean_when_I_run_autogen.sh_in_libgphoto2.3F "wikilink"),
be sure to have libltdl installed.

` ./configure`

Watch the output of ./configure to make sure that the csharp bindings
are enabled. It should have a line in it something like:

` Bindings:             csharp`

then, just do the usual:

` make && sudo make install && sudo ldconfig`

To get around an ugly bug that we have with libgphoto2\_port's disk
driver, be sure to remove it:

` sudo rm /usr/local/lib/libgphoto2_port/0.6.1/disk.*`

Libgphoto2 and it's C\# bindings should now be installed!

### Installing gphoto2 to test libgphoto2

The `gphoto2` command line tool is the easiest way to test that
libgphoto2 can find and access your MTP device. It's contained in the
gphoto svn repository. You know the drill -- grab and install it as
follows:

` svn co `[`https://svn.sourceforge.net/svnroot/gphoto/trunk/gphoto2`](https://svn.sourceforge.net/svnroot/gphoto/trunk/gphoto2)  
` cd gphoto2`  
` ./autogen.sh`  
` ./configure`  
` make`  
` sudo make install`

Once it's installed, test to see if gphoto2 can find your MTP device:

` gphoto2 -L`

It should list all the files & folders on your device. If you get any
errors as this point, you can safely assume that you will have trouble
and that the Banshee DAP interface will not be happy. Regardless, you
can trudge on!

If you have any issues at this point, post a debug output to
[pastebin.us](http://www.pastebin.us) and hit up irc.gnome.org/\#banshee
and ask trick for help. Optionally, if it looks more like an issue with
the MTP (PTP2) driver, you can ask on irc.freenode.net/\#gphoto, but ask
nicely as this driver is new and the developers are busy folks.

If it's working great, lets try it in Banshee!

### Installing Banshee from CVS

Grab the latest CVS version of Banshee:

` cvs -z3 -d:pserver:anonymous@anoncvs.gnome.org:/cvs/gnome co -P banshee`

**NOTE: this will change as Gnome is moving to Subversion
(eventually).** If you're getting errors with this command, check out
the [status of the subversion
migration](http://live.gnome.org/Subversion). Ask in \#banshee or
\#gnome for help!

Finally, run autogen. Pass `--enable-mtp`:

` ./autogen.sh --enable-mtp --whatever-other-flags-you-usually-use`

If you've never built Banshee from source before, and are using a
standard gstreamer installation...use:

` ./autogen.sh --enable-mtp`

That should do the trick. Finally, make Banshee and install it:

` make && sudo make install`

Moving further
--------------

### Testing it out

First, check out the [Known
Bugs](/wiki/Projects/Open_Source/Banshee/MTP/Known_Bugs "wikilink") page.
PLEASE, read this page!

It's not that hard to run Banshee. Execute banshee (preferrably from a
terminal, with the **--debug** flag, in case you get an error).

Once Banshee has started up, plug your MTP device in. As long as all is
well, the interface will show a little loading message as it reads the
track information from the device. Once the message disappears, you
should be ready to go! Drag 'n drop some tracks on the device, and run a
Synchronize to see if it works. Not only can you drag mp3's, but also
ogg and flac (and possibly even other formats) to the device and they
will be transcoded and then transferred to the device. In my experience
this has been flawless.

Removing tracks from the device is easy. Just right click the file and
hit Remove, and then run Synchronize.

Editing of Metadata is possible, but has been disabled because of some
strange conflicts and crashes with the CVS updates. This will most
likely be sorted out in the future.

Playback does not work at all. It might someday, but not for now.

### Playlists

Playlists don't work. Not yet. But, they're in the
works...[playlist](/wiki/Projects/Open_Source/Banshee/MTP/Playlists "wikilink")
support is coming...

### Reporting Bugs

Please, by all means, report bugs. There are so many possible bugs in
this code that I just won't discover myself, and this can be a good
piece of software if you help me out. File bugs on the [Gnome Bugzilla,
product banshee, component
MTP](http://bugzilla.gnome.org/enter_bug.cgi?product=banshee&component=MTP).

### Sending Patches

As with reporting bugs, patches are more than welcome. I've been
experiencing a few troubles, particularly with shutting down banshee
after making a transfer. I'm pretty sure that they're native-code
related, but I have no clue where (as of yet). Please post patches to
bugzilla!

Also, check out [Known
Bugs](/wiki/Projects/Open_Source/Banshee/MTP/Known_Bugs "wikilink") and the
[To Do](/wiki/Projects/Open_Source/Banshee/MTP/To_Do "wikilink") list.

### Icons

I'm working on some icons
[here](/wiki/Projects/Open_Source/Banshee/MTP/Icons "wikilink").
