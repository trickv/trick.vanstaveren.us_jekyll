---
title: Projects/Open Source/Banshee/MTP
permalink: wiki/Projects/Open_Source/Banshee/MTP/
layout: wiki
---

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

### Testing your device with gphoto2

To get a quick test of whether your device works with your installation
of libgphoto2, plug it in and open a terminal, and run:

` gphoto2 -L`

It should list all the files & folders on your device. If you get any
errors as this point, you can safely assume that you will have trouble
getting Banshee to work with your device. You can ask for help with
these errors on irc.freenode.net/\#gphoto or on the [gphoto2-devel
mailing list](http://sourceforge.net/mail/?group_id=8874). Be sure to
mention this is a MTP device; the library here is actually a camera
library.

If it's working properly, lets try it in Banshee!

How to install
--------------

MTP support got really good in libgphoto2 around v2.2.2; so if you have
a package for your distribution of 2.2.2 or 2.3.0, you are much better
off using that. I am tailoring these instructions against this case.

### Remove old packages

Be sure that you have removed any old files from a Banshee install. To
make sure your system is clean, make sure /usr/lib/banshee and
/usr/local/lib/banshee are both nonexistent - if not, find and remove
packages or manually wipe out the directories.

### Packages to have / Prerequisites

Please be sure that you have all companion -dev/-devel packages
installed. Configure scripts will fail if you are missing them - and
they will act like you are missing the library itself.

-   Mono
    -   On Ubuntu Dapper, this is: libmono0, libmono-dev, mono,
        mono-common, mono-devel, mono-mcs
-   libltdl
-   libusb (Warning: libusb 0.1.12 was known to cause troubles when
    first released...do inform me if these issues persist)
-   libexif
-   libgphoto2 and libgphoto2-dev
-   libgphoto2-sharp from a release or installed from source as
    described here

### Grabbing the latest libgphoto2-sharp

libgphoto2-sharp 2.3.0 is the latest release, dated 2006-12-10. If you
cannot find a package for your distribution, you will have to build it
from source:

First grab the tarball off the [gPhoto SourceForge downloads
page](http://sourceforge.net/project/showfiles.php?group_id=8874&package_id=214288).

Prepare the build like normal:

` ./configure`

Make sure there's no errors, and then do the usual:

` make && sudo make install`

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
PLEASE, read it!

Launch Banshee like normal.

Once Banshee has started up, plug your MTP device in. As long as all is
well, the interface will show a little loading message as it reads the
track information from the device. Be patient, it can take quite some
time to load up - on my system, it can process about ten tracks per
second. This is a protocol limitation that hopefully we can get past :)

If you do not see anything, try running Banshee in debug mode (run
`banshee --debug` at a terminal), go to the Help menu, and click View
Debugging Messages. You should see some messages from the MTP driver
trying to find your device; copy all this information down and [submit a
bug
report](http://bugzilla.gnome.org/enter_bug.cgi?product=banshee&component=MTP).

Once the message disappears, you should be ready to go! Drag 'n drop
some tracks on the device, and run a Synchronize to see if it works. Not
only can you drag mp3's, but also ogg and flac (and possibly even other
formats) to the device and they will be transcoded and then transferred
to the device. In my experience this has been flawless.

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
