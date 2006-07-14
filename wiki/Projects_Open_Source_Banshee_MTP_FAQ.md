---
title: Projects/Open Source/Banshee/MTP/FAQ
permalink: wiki/Projects/Open_Source/Banshee/MTP/FAQ/
layout: wiki
---

### Q: What does this mess mean when I run `autogen.sh` in libgphoto2?

`> ./autogen.sh`  
`` Looking for `./configure.{ac,in}'... ./configure.in ``  
`` autogen.sh:init: Entering directory `.' ``  
`ls: libltdl/*: No such file or directory`  
`` libtoolize: cannot list files in `/usr/share/libtool/libltdl' ``  
`` Could not create libltdl directory `libltdl'. ``  
`` Leaving `/home/jonathan/libgphoto2' and aborting. ``  
`` autogen.sh:init: Left directory `.' ``

A: You are missing libltdl. Be sure to install it!

------------------------------------------------------------------------

......
