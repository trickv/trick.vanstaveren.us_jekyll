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

Of course, if you'd like to donate me a MTP player, I'll do my best to
make it work :)

------------------------------------------------------------------------

The following devices are known MTP devices, recognized by libgphoto2.
This is a direct snap from my codebase which filters out non-MTP
devices. If you have a MTP player that's not on this list, Banshee will
refuse to recognize it - email me and I'll help you out ASAP :)

`new DeviceId(`“`iRiver`` ``T10`` ``(alternative)`”`,                    `“`iRiver`` ``T10`”`,           0x4102,     0x1113),`  
`new DeviceId(`“`iRiver`` ``U10`”`,                                  `“`iRiver`` ``U10`”`,           0x4102,     0x1116),`  
`new DeviceId(`“`iRiver`` ``T10`”`,                                  `“`iRiver`` ``T10`”`,           0x4102,     0x1117),`  
`new DeviceId(`“`iRiver`` ``T20`”`,                                  `“`iRiver`` ``T20`”`,           0x4102,     0x1118),`  
`new DeviceId(`“`iRiver`` ``T30`”`,                                  `“`iRiver`` ``T30`”`,           0x4102,     0x1119),`  
`new DeviceId(`“`iRiver`` ``H10`”`,                                  `“`iRiver`` ``H10`”`,           0x4102,     0x2102),`  
`/* iRiver H30? Anyone? */`  
`new DeviceId(`“`iRiver`` ``Portable`` ``Media`` ``Center`”`,                `“`iRiver`` ``PMC`”`,           0x1006,     0x4002),`  
`new DeviceId(`“`iRiver`` ``Portable`` ``Media`` ``Center`”`,                `“`iRiver`` ``PMC`”`,           0x1006,     0x4003),`  
`new DeviceId(`“`Phillips`` ``HDD6320`”`,                            `“`HDD6320`”`,              0x0471,     0x01eb),`  
`new DeviceId(`“`Creative`` ``Zen`` ``Vision`”`,                         `“`Zen`` ``Vision`”`,           0x041e,     0x411f),`  
`new DeviceId(`“`Creative`` ``Portable`` ``Media`` ``Center`”`,              `“`Media`` ``Center`”`,         0x041e,     0x4123),`  
`new DeviceId(`“`Creative`` ``Zen`` ``Xtra`”`,                           `“`Zen`` ``Xtra`”`,             0x041e,     0x4128),`  
`new DeviceId(`“`Second`` ``Generation`` ``Dell`` ``DJ`”`,                   `“`Dell`` ``DJ`”`,              0x041e,     0x412f),`  
`new DeviceId(`“`Creative`` ``Zen`` ``Micro`”`,                          `“`Zen`` ``Micro`”`,            0x041e,     0x4130),`  
`new DeviceId(`“`Creative`` ``Zen`` ``Touch`”`,                          `“`Zen`` ``Touch`”`,            0x041e,     0x4131),`  
`new DeviceId(`“`Creative`` ``Zen`` ``Sleek`”`,                          `“`Zen`` ``Sleek`”`,            0x041e,     0x4137),`  
`new DeviceId(`“`Creative`` ``Zen`` ``MicroPhoto`”`,                     `“`Zen`` ``MicroPhoto`”`,       0x041e,     0x413c),`  
`new DeviceId(`“`Creative`` ``Zen`` ``Sleek`` ``Photo`”`,                    `“`Zen`` ``Sleek`` ``Photo`”`,      0x041e,     0x413d),`  
`new DeviceId(`“`Creative`` ``Zen`` ``Vision:M`”`,                       `“`Zen`` ``Vision:M`”`,         0x041e,     0x413e),`  
`new DeviceId(`“`Samsung`` ``YP-T7J`”`,                              `“`Samsung`` ``YP-T7J`”`,       0x04e8,     0x5047),`  
`new DeviceId(`“`Samsung`` ``YH-999`` ``Portable`` ``Media`` ``Center`”`,        `“`Samsung`` ``YH-999`”`,       0x04e8,     0x5a0f),`  
`new DeviceId(`“`Dell`` ``DJ`` ``Ditty`”`,                               `“`DJ`` ``Ditty`”`,             0x413c,     0x4500),`  
`new DeviceId(`“`Toshiba`` ``Gigabeat`”`,                            `“`Gigabeat`”`,             0x0930,     0x000c),`  
`new DeviceId(`“`Intel`` ``Bandon`` ``Portable`` ``Media`` ``Center`”`,          `“`Intel`` ``Bandon`”`,         0x045e,     0x00c9)`