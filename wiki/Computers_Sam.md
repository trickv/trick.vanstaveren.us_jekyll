---
title: Computers/Sam
permalink: wiki/Computers/Sam/
layout: wiki
---

Sam is a [Linode](http://www.linode.com/) 360 Xen machine. It runs
[vanstaveren.us](http://vanstaveren.us/) and everything on it, aside
what you'll find under
[sting.vanstaveren.us](http://sting.vanstaveren.us/) or
`home.vanstaveren.us`.

It runs Gentoo. And it's a mess.

Services:

-   httpd for 10-15 vhosts, including trick.vanstaveren.us
    -   Bicycle mileage DB
    -   Uptime DB
-   mysql with a variety of DBs
-   Postgres with a variety of DBs
-   Mail
    -   MTA: exim
    -   IMAP: dovecot
    -   Spam assassin (which doesn't work well anymore, it's out of
        date)
    -   Roundcube webmail
-   L2TP/IPSec VPN server

