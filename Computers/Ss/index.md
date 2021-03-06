---
title: Computers/Ss
permalink: Computers/Ss/
layout: wiki
---

In December 2008 I purchased a Lenovo IdeaPad U330.

I bought this specific model because quite a few modern laptops aren't
exactly portable anymore -- they're bulky widescreen overweight beasts.
The IdeaPad series is built to be lightweight (&lt;5 pounds) and low
power to make for good battery life. I bought it from my local
[MicroCenter](http://www.microcenter.com/) in Chicago for $1300. The
closest competitor in the store was a Sony for about $1800 which was
also an ultra-light model.

Upon purchase I didn't allow Vista to see the light of day and installed
GNU/Linux on it. I've been too tired too maintain Gentoo on my machines
in the past year, so I'm trying on Ubuntu for style.

I'm slightly regretting not installing Vista. I would never want to use
it, but it seems Lenovo's BIOS updates are run from Windows. So I'm
going to have to install Windows somewhere (probably on a spare hard
drive or a USB stick if I can manage it.)

Hardware Details
----------------

-   Intel Core2 Duo P7350 @ 2 GHz
-   3GB Memory
-   250GB disk
-   ATI Switchable Graphics with:
    -   ATI Radeon HD 3400
    -   Intel Something (haven't used yet)
-   Lenovo EasyCam 1.3M camera
-   Intel ICH9 HD audio
    -   ATI RV620 device (haven't used yet)
-   Intel PRO/Wireless 5100
-   USB, Firewire, SD card reader

I'm working on compatibility for a few things with GNU/Linux.

Out of the box
--------------

I did a network install of Ubuntu 8.10 which worked fine to get me a
text console. Then I learned a bit more about switchable graphics and
learned that I need to manually switch it in the BIOS as it requires
special (Vista-only) drivers to use it in switchable mode. In the BIOS I
have two options: “Switchable Graphics” or “Discrete Graphics”.
Selecting discrete mode makes the ATI card appear native, and the
xorg-radeon drivers work fine to get me a fully working desktop.
Network, wireless, USB, suspend all work out of the box on GNU/Linux.

Switchable Graphics
-------------------

Compatibility status: fail, workaround

Apparently this type of hardware has been around for a while now by both
nVidia and ATI. Google searches tell me that it requires special drivers
to work in switchable mode and that no one has written anything like
this for Linux \[yet.\] Supposedly some Sony laptops running nVidia
chips have a third option in the BIOS to select the integrated video
card which gives power savings over the nicer card. My laptop does not
have this option.

I've booted the laptop into switchable mode and probed a bit. lspci
shows both video cards. I tried specifying manual Device sections in an
xorg.conf to force a driver to find the card, but no luck (whatsoever.)
I'll put more info here sooner and raise this on the xorg development
lists and see if anyone else has worked on this.

In the mean time I'm running solely on the ATI card which unnecessarily
wastes a bit of power. I want to get the Intel graphics to work because
I rarely deal in anything other than 2D applications.

Web Cam (Lenovo EasyCam)
------------------------

Compatibility status: work in progress

At first, V4L programs like Ekiga did not detect the device. I fished in
further.

The camera is a USB Video Class device. A bit of research shows the
[Linux UVC project](http://linux-uvc.berlios.de/) should cover this. UVC
was committed to the mainstream kernel in 2.6.26 and Ubuntu 8.10 runs
2.6.27.x. The device is detected and shown in `dmesg`, but no
`/dev/video?` device is created. I later `rmmod` and `modprobe` the
`uvcvideo` module which then properly detects the device and creates the
`/dev/video0` device, but testing with `luvcvideo` program fails to work
and `dmesg` shows the error:

`uvcvideo: Failed to query (130) UVC control 1 (unit 0) : 2 (exp. 26).`

I continued pursuing the latest UVC code and tried running a
self-compiled 2.6.28 kernel which did not help, but I then grabbed the
bleeding-edge sources from UVC mercurial repo (revision 9904,) compiled
and loaded `videodev` and `uvcvideo` from the compiled copy, and I have
video! The picture is inverted, but it's close. From a few sources I've
read that this is a common issue and can be worked around with using a
parameter on `insmod` and I'll post these results to the UVC list soon.

Keyboard double-presses
-----------------------

The keyboard is a full-size keyboard which makes me happy. But I'm
having one issue: sometimes I'm getting double key-presses. Irregularly,
`vim foo` actually comes out as `vimm foo`. I'm not sure if this is a
hardware issue or a software issue, but I'm a solid typist and confident
that this isn't just shaky hands.

Comments
--------

I've used lots of other things that Just Worked and aren't mentioned
here. CD burning worked out of the box. Wireless & ethernet with
NetworkManager work fine. USB works fine of course. Audio works now that
I've found the checkbox which toggles back and forth between headphones
and speakers.
