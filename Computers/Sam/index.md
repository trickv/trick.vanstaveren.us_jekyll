---
title: Computers/Sam
permalink: Computers/Sam/
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
    -   Roundcube webmail
    -   trick.vanstaveren.us mediawiki
-   mysql with a variety of DBs
-   Postgres with a variety of DBs
-   Mail
    -   MTA: exim
    -   IMAP: dovecot
    -   Spam assassin (which doesn't work well anymore, it's out of
        date)
-   L2TP/IPSec VPN server
-   OpenVPN client (and defunct, but willing, OpenVPN servers)
-   Nagios
-   Munin node

HG's Squiddy is set to consume tons of ram, so it's making HG run out of
memory.
