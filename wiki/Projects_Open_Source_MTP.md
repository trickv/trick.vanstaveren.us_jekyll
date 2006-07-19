---
title: Projects/Open Source/MTP
permalink: wiki/Projects/Open_Source/MTP/
layout: wiki
---

MTP: [Media Transfer
Protocol](http://en.wikipedia.org/wiki/Media_transfer_protocol)

[libgphoto debugging temp](libgphoto_debugging_temp "wikilink")

This is an attempt to round up all the progress that has been made in
making MTP devices accessable in linux and other POSIX operating
systems. The idea here is to figure out what folks have done so we can
all work together and make MTP be “supported”

If you know a thing or two about MTP, libmtp, libgphoto2's MTP support,
f-spot's MTP support...I am on IRC at irc.gnome.org/\#banshee. Also, if
you have a MTP device and want to make sure that the USB Vendor & Device
ID are reported, you can come there too. Finally, if you're trying my
mtp-sharp and it's giving you hell (which it will), you can come here
and complain and I'll kindly tell you how alpha it is :)

My project: [mtp-sharp](mtp-sharp "wikilink"). I know there's already a
project called mtpsharp, but this one is a mono wrapper for libmtp,
intended for use with the [Banshee Music
Player](http://www.banshee-project.org/).

Open Source Projects using MTP:
-------------------------------

[libmtp](http://libmtp.sf.net/) - a fork from libptp2, adds the
extensions of mtp. Very good start - still has plenty of issues but is a
great start. It's enough to get your MTP device recognized and able to
send/recieve a few tracks.

-   I've used it; it works. I'm running CVS as of 2006-03-18 and it
    detects my Creative Zen Micro, lists its tracks. I haven't tested
    getting/recieveing/deleting tracks with the programs supplied in the
    **examples** directory of the package, but I'd assume they work.

[id34mtp](http://sourceforge.net/projects/id34mtp), a command line tool
that transfers files to MTP devices, reading metadata from the id3 tag.

-   uses libmtp
-   Tested on 2006-03-18: works great! Able to send tracks just fine. I
    haven't tested extensively, but worked right out of the box.
-   had some compilation issues. It requires two header files from
    libptp2 - **libptp-endian.h** and **libptp-stdint.h**. I first
    installed libptp2 only to find that it actually wants the files in
    the project's directory. But hey, it's a prerelease, I wouldn't
    expect anything else :)

[MTPdude](http://sourceforge.net/projects/mtpdude), a graphical, beta
MTP transfer program, written in GTK, using libmtp

-   tested on 2006-03-18 - compile fails, I'm not sure why really.
    Probably was based on libmtp's first release version, and I'm now
    running CVS.
-   CVS for MTPdude doesn't seem to exist (at least not yet). Probably
    more coming soon! Screenshots look promising and might yield a mini
    version of gnomad2, but for MTP.

mtpsharp, which can be obtained from
[mtpsharp](http://mtpsharp.sf.net/), [mtpsharp SF project
page](http://sourceforge.net/projects/mtpsharp), or [here, writer's
personal page](http://studwww.ugent.be/~phdrycke/mtpsharp/). Not sure
what the point of this application is.

-   says it's in c++ when it's in c\# ( i think)
-   looks to be a wrapper for win32 only - doesn't use libmtp or
    anything even posix at all - it claims to be a wrapper for win32 to
    provide mtp device access to .net languages.
-   probably won't work for us posix folks...but might be a decent
    starting ground for a mtp-sharp mono binding
-   I personally plan to work on a mtp-sharp mono port to plug into
    libmtp and eventually provide MTP support for Banshee.

[gnomad2](http://gnomad2.sourceforge.net/), the NJB client that is
(probably) most popular; working on libmtp to eventually work with
gnomad2.

-   According to website, has been working on MTP support, but I see
    nothing even in CVS.
-   One of the developers from gnomad2, however, is the lead for libmtp,
    so I'm sure gnomad2 will see MTP support in the coming weeks or
    months :)

libgphoto2 (and gphoto2) which have reportedly connected to some MTP
devices (as gphoto2 is based around PTP cameras, and MTP is an
extension, naturally making MTP work wasn't too hard)

-   might yield a better solution than libmtp? Not so sure anymore,
    after seeing that libmtp is a fork from libptp2 which has been
    around for a while.
-   so wait a sec - there's libmtp, and libgphoto2 which both have the
    same mtp functions? wtf...
    -   who knows, maybe i'll write a banshee wrapper around gphoto :)
        can't be that hard!

[mp32mtp](http://dmartin.org/~dmartin/downloads/mp32mtp), a command line
program using libmtp

-   I can't find this one anymore. I found the link on 2006-03-16, and
    on 2006-03-18, the link is dead. Apparently was a command line
    program that used libmtp's sendtr (send track) program to send
    tracks, but may have read id3 info or prompted the user for the
    info. Who knows!

[Gentoo Forums: HOWTO: Transfer files to MTP devices using CVS
libmtp](http://forums.gentoo.org/viewtopic-t-437069.html)
