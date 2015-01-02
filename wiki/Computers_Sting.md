---
title: Computers/Sting
permalink: wiki/Computers/Sting/
layout: wiki
---

### What It Is

Sting is my dual P2-350 ~~128meg~~ 256meg [Asus
P2B-D](http://www.motherboard.cz/mb/asus/P2B-D.htm)
webserver/router/firewall/backup/you-name-it box.

It is named for [the
dagger](http://en.wikipedia.org/wiki/List_of_Middle-earth_weapons_and_armour#Sting)
which Bilbo and later Frodo used in *The Hobbit* and *The Lord Of The
Rings*.

<img src="Sting_front_2015-01-01.jpg" title="fig:Sting_front_2015-01-01.jpg" alt="Sting_front_2015-01-01.jpg" width="168" />
<img src="IMG_4113.jpg" title="fig:IMG_4113.jpg" alt="IMG_4113.jpg" width="168" />
<img src="IMG_20101101_072133.jpg" title="fig:IMG_20101101_072133.jpg" alt="IMG_20101101_072133.jpg" width="300" />
<img src="IMG_4118.jpg" title="fig:IMG_4118.jpg" alt="IMG_4118.jpg" width="300" />

### History

Sting has been my home network keystone since about 2004. It's an old
slow dog that never quits.

### The Uptime Saga

-   Back in college, I was excited when it hit uptimes of 90 and 53
    days.
-   I moved to Chicago in 2006 and made some money, and bought a UPS.
    That helped.
-   After a year, living at my Hutchinson St apartment, the uptime grew.
    It prompted me to write a simple [uptime tracking service for my
    computers](http://vanstaveren.us/~trick/uptime/), so I would have a
    proper record aside this page.
-   Less than 12 hours before I moved out of that apartment, it crashed
    due to a disk controller fault at an uptime of 279 days.
-   I moved to my Washtenaw Ave apartment in 2008, replaced the disk
    controller and disks with hand-me-down SATA disks, and left it on
    from December 2008 onwards.
-   In May 2010, I moved from the ground floor to the top floor of the
    apartment on Washtenaw Ave. I planned and executed a successful move
    of Sting whilst on, with it's UPS in hand!
-   On November 1st 2010, the [power supply in Sting finally gave
    way](:Image:IMG_20101101_211542.jpg "wikilink") and it died in the
    middle of the night, at 687 days up. 94% of the way to two years. I
    replaced the power supply with a [new gigantic
    one](:Image:IMG_4120.jpg "wikilink") from Cooler Master.
-   In 2011 I moved to China and left Sting with my friend Dan. Disks
    from [mc](/wiki/Computers/McTrickster "wikilink") were consolidated into
    sting, and mc found a dumpster.
    -   Unfortunately Sting was taken offline a few months later, and
        was in storage for 3 years.
-   In December 2014 Sting was installed to the Weir house. Set up with
    an automatic shutdown when idle, and a monthly power-on schedule for
    the 13th at 07:00 UTC, sting will surface from time to time.

I may never beat 687 days with a real physical computer of my own.

### Software

Sting runs [GNU](http://www.gnu.org/)/[Linux](http://kernel.org/) with a
2.6 kernel. It's primary based on [Slackware
10.2](http://www.slackware.org/) and [Dropline Gnome
2.14](http://www.droplinegnome.org/).

It has been massively upgraded over the years. 2.4 to 2.6 was a bit of a
challenge, and I've found my `/usr/local` to be extensive.

It runs lots of fun services like:

-   Apache 2.0 web server with PHP 5
-   SSH and OpenVPN servers
-   Exim SMTP server
-   Subversion server
-   Internal services like a Netfilter firewall, VPN bridge and DHCP
    server, DNS server with custom records and an NTP server.
-   Tunnels or proxies several services from
    [mc](/wiki/Computers/Mc "wikilink") for music sharing.

You can visit sting's web interface at
[sting.vanstaveren.us](http://sting.vanstaveren.us/)
