---
title: Computers/hg
permalink: wiki/Computers/hg/
layout: wiki
---

A virtual machine run on Linode in Fremont. I've memorized it's IP
173.255.250.167.

Originally installed around 2011 using Debian 6 32-bit. Meant as a proxy
which I built right before I went to China.

Linode history:

-   2011-04: linode 512 (Xen)
-   2013-07: upgraded to linode 2014
-   2015-10: started researching in-place upgrade from 32 to 64 bit.
-   2016-03: Debian 6 (squeeze) LTS ends...oops!
-   2016-10: converted from 32-bit to 64-bit (still on Debian 6)

Somewhere in there I enabled IPv6 which worked out of the box on almost
everything - except iftop which in squeeze is IPv4 only.

Now that it's gone unsupported in 2016, I'm looking to convert it to
64-bit and upgrade on to wheezy and jessie.
