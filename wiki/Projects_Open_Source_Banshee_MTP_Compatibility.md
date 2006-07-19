---
title: Projects/Open Source/Banshee/MTP/Compatibility
permalink: wiki/Projects/Open_Source/Banshee/MTP/Compatibility/
layout: wiki
---

The only actual tested device is, of course, my Creative Zen Micro,
which is known to work fine.

I've been in touch with a user with a Creative Portable Media Center
which seemed to have some filesystem issues at the gphoto level. I don't
know where that one went...

I “hear” that some iRiver devices don't work perfectly yet with
libgphoto2...

Of course, if you'd like to donate me a MTP player of any brand or
sorts, I'll be happy to make it work for you :)

------------------------------------------------------------------------

Whether or not your player is compatible with Banshee's MTP support
depends on [libgphoto2's device
list](http://svn.sourceforge.net/viewcvs.cgi/*checkout*/gphoto/trunk/libgphoto2/camlibs/ptp2/library.c),
and my [device
list](http://cvs.gnome.org/viewcvs/*checkout*/banshee/src/Banshee.Dap/Mtp/MtpDeviceId.cs)
in Banshee's MTP driver. If your device is not on both lists, it will
not work. If you have a new device to add to the list, please [e-mail
me](/wiki/Contact "wikilink") and I'll help you out!

------------------------------------------------------------------------

The following is a direct snap from my codebase of supported devices:

`                        Full Device Name                               Display/Short Name      Vendor ID   Product ID */`  
`           new DeviceId(`“`iRiver`` ``T10`` ``(alternative)`”`,                    `“`iRiver`` ``T10`”`,           0x4102,     0x1113),`  
`           new DeviceId(`“`iRiver`` ``T20`` ``FM`”`,                               `“`iRiver`` ``T20`` ``FM`”`,        0x4102,     0x1114),`  
`           new DeviceId(`“`iRiver`` ``U10`”`,                                  `“`iRiver`` ``U10`”`,           0x4102,     0x1116),`  
`           new DeviceId(`“`iRiver`` ``T10`”`,                                  `“`iRiver`` ``T10`”`,           0x4102,     0x1117),`  
`           new DeviceId(`“`iRiver`` ``T20`”`,                                  `“`iRiver`` ``T20`”`,           0x4102,     0x1118),`  
`           new DeviceId(`“`iRiver`` ``T30`”`,                                  `“`iRiver`` ``T30`”`,           0x4102,     0x1119),`  
`           new DeviceId(`“`iRiver`` ``H10`”`,                                  `“`iRiver`` ``H10`”`,           0x4102,     0x2102),`  
`           new DeviceId(`“`iRiver`` ``Portable`` ``Media`` ``Center`”`,                `“`iRiver`` ``PMC`”`,           0x1006,     0x4002),`  
`           new DeviceId(`“`iRiver`` ``Portable`` ``Media`` ``Center`”`,                `“`iRiver`` ``PMC`”`,           0x1006,     0x4003),`  
`           new DeviceId(`“`Phillips`` ``HDD6320`”`,                            `“`HDD6320`”`,              0x0471,     0x01eb),`  
`           new DeviceId(`“`Phillips`` ``HDD6130/17`”`,                         `“`HDD6130/17`”`,           0x0471,     0x014c),`  
`           new DeviceId(`“`Creative`` ``Zen`` ``Vision`”`,                         `“`Zen`` ``Vision`”`,           0x041e,     0x411f),`  
`           new DeviceId(`“`Creative`` ``Portable`` ``Media`` ``Center`”`,              `“`Media`` ``Center`”`,         0x041e,     0x4123),`  
`           new DeviceId(`“`Creative`` ``Zen`` ``Xtra`”`,                           `“`Zen`` ``Xtra`”`,             0x041e,     0x4128),`  
`           new DeviceId(`“`Second`` ``Generation`` ``Dell`` ``DJ`”`,                   `“`Dell`` ``DJ`”`,              0x041e,     0x412f),`  
`           new DeviceId(`“`Creative`` ``Zen`` ``Micro`”`,                          `“`Zen`` ``Micro`”`,            0x041e,     0x4130),`  
`           new DeviceId(`“`Creative`` ``Zen`` ``Touch`”`,                          `“`Zen`` ``Touch`”`,            0x041e,     0x4131),`  
`           new DeviceId(`“`Dell`` ``Pocket`` ``DJ`”`,                              `“`Pocket`` ``DJ`”`,            0x041e,     0x4132),`  
`           new DeviceId(`“`Creative`` ``Zen`` ``Sleek`”`,                          `“`Zen`` ``Sleek`”`,            0x041e,     0x4137),`  
`           new DeviceId(`“`Creative`` ``Zen`` ``MicroPhoto`”`,                     `“`Zen`` ``MicroPhoto`”`,       0x041e,     0x413c),`  
`           new DeviceId(`“`Creative`` ``Zen`` ``Sleek`` ``Photo`”`,                    `“`Zen`` ``Sleek`` ``Photo`”`,      0x041e,     0x413d),`  
`           new DeviceId(`“`Creative`` ``Zen`` ``Vision:M`”`,                       `“`Zen`` ``Vision:M`”`,         0x041e,     0x413e),`  
`           new DeviceId(`“`Samsung`` ``YP-T7J`”`,                              `“`Samsung`` ``YP-T7J`”`,       0x04e8,     0x5047),`  
`           new DeviceId(`“`Samsung`` ``YH-999`` ``Portable`` ``Media`` ``Center`”`,        `“`Samsung`` ``YH-999`”`,       0x04e8,     0x5a0f),`  
`           new DeviceId(`“`Samsung`` ``YH-925`”`,                              `“`Samsung`` ``YH-925`”`,       0x04e8,     0x502f),`  
`           new DeviceId(`“`Dell`` ``DJ`` ``Ditty`”`,                               `“`DJ`` ``Ditty`”`,             0x413c,     0x4500),`  
`           new DeviceId(`“`Toshiba`` ``Gigabeat`”`,                            `“`Gigabeat`”`,             0x0930,     0x000c),`  
`           new DeviceId(`“`JVC`` ``Aleno`` ``XA-HD500`”`,                          `“`JVC`` ``Aleno`”`,            0x04f1,     0x6105),`  
`           new DeviceId(`“`Intel`` ``Bandon`` ``Portable`` ``Media`` ``Center`”`,          `“`Intel`` ``Bandon`”`,         0x045e,     0x00c9),`  
`           new DeviceId(`“`Sandisk`` ``Sansa`` ``e200`”`,                          `“`Sansa`` ``e200`”`,           0x0781,     0x7420)`

| asdf || dfg
