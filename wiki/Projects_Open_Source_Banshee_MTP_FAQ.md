---
title: Projects/Open Source/Banshee/MTP/FAQ
permalink: wiki/Projects/Open_Source/Banshee/MTP/FAQ/
layout: wiki
---

### Q: What devices are supported? What should I do if my MTP device is \_not\_ supported?

**A:** Check the
[compatibility](/wiki/Projects/Open_Source/Banshee/MTP/Compatibility "wikilink")
page to see what players Banshee supports. This list is derived from
libgphoto2's device list which is contained in
[camlibs/ptp2/library.c](http://svn.sourceforge.net/viewcvs.cgi/*checkout*/gphoto/trunk/libgphoto2/camlibs/ptp2/library.c)
of libgphoto2 from subversion. If you need a MTP device added to both my
compatibility list (which is hardcoded in Banshee) and/or the libgphoto2
library.c, please [contact](/wiki/Contact "wikilink") me :)

### Q: What does this mess mean when I run `autogen.sh` in libgphoto2?

`> ./autogen.sh`  
`` Looking for `./configure.{ac,in}'... ./configure.in ``  
`` autogen.sh:init: Entering directory `.' ``  
`ls: libltdl/*: No such file or directory`  
`` libtoolize: cannot list files in `/usr/share/libtool/libltdl' ``  
`` Could not create libltdl directory `libltdl'. ``  
`` Leaving `/home/jonathan/libgphoto2' and aborting. ``  
`` autogen.sh:init: Left directory `.' ``

**A:** You are missing libltdl. Be sure to install it!
