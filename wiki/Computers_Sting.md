---
title: Computers/Sting
permalink: wiki/Computers/Sting/
layout: wiki
---

Sting, my fabulous dual P2-350 128meg ram server/firewall/etc box.

Sting has been my firewall now for almost four years, and all I've had
to replace on it is some bad ram and a bad hard drive. My best uptime
was something like 90 days, but the best I have on record is “22:14:06
up 53 days, 21:05, 1 user, load average: 0.00, 0.00, 0.00”. Once I get
down to Chicago and have some cash to buy it a backup battery and toss
in some more ram, I suspect I will never turn it off until the next time
I move. We'll see :)

It runs lots of fun software, built on top of Slackware 10.2 w/ Dropline
Gnome 2.14:

-   Apache 2.0 web server, with mod\_mono & PHP 5
    -   hosts lots of little bits 'n pieces of fun stuff, including
        iFolder
-   iFolder 3.5 server (instructions to build will come soon on
    [Log](/wiki/Log "wikilink") and on ifolder site)
-   SSH, FTP, TightVNC services
-   Testing box for the [Horde Application
    Framework](http://www.horde.org/) CVS.
-   Subversion server
-   Netfilter firewall
    -   w/ traffic shaping marking and l7\_filter added on
    -   Port forwarding stuff for [mc](/wiki/Computers/Mc "wikilink")

You can visit sting's web interface at
[sting.vanstaveren.us](http://sting.vanstaveren.us/)
