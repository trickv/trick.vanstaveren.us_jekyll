---
title: Projects/Open Source/Banshee/MTP/Known Bugs
permalink: wiki/Projects/Open_Source/Banshee/MTP/Known_Bugs/
layout: wiki
---

-   We're assuming the device has ONLY mp3's on it. It does not show
    anything without the mp3 mime type on the device. It's possible to
    have WMA's on there from use with WMP, as well as WAV files (from
    voice recording or something).

<!-- -->

-   Shutdown causes segfaults and glib free errors. I have yet to figure
    out where this is coming from.

<!-- -->

-   libgphoto2\_port's disk driver must be making some hal calls,
    because Banshee.Dap.Mtp looses it's hal information right when we
    first run a device scan with libgphoto2. The workaround is to remove
    the disk driver:

` sudo rm /usr/local/lib/libgphoto2_port/0.6.1/disk.*`