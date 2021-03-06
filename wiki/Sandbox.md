---
title: Sandbox
permalink: wiki/Sandbox/
layout: wiki
---

Debugging Banshee
-----------------

Banshee is still under heavy development, and as such, you may encounter
various bugs, some of which may lead to crashes. Banshee is developed
under [Mono](http://mono-project.com/), and debugging a crash, depending
on where the bug is, can either be easy or more difficult than with
traditional C programs.

Understanding Managed vs. Native
--------------------------------

There are two places where a crash can occur: in managed code (inside
the Mono runtime), and in native code (C code, for example). Crashes in
managed code usually lead to *exceptions*, and crashes in native code
usually lead to *segmentation faults (segfault),* although it is
possible for crashes in managed code to lead to segfaults (though this
may indicate a bug in the Mono runtime).

For the purposes of this document, “debugging” refers mainly to the act
of reproducing a crash and obtaining a good *stack trace.* A stack trace
helps developers isolate offending crash-causing code.

A crash in managed code is usually easier to debug than a crash in
native code. A managed crash will produce a stack trace immediately on
an *unhandled exception.* This can then be copied and provided in bug
reports. However, if the crash was in managed code and also caused a
segfault, the Mono runtime will *attempt* to print a native stack trace
as well, following the managed exception trace. While this is good,
further debugging may be helpful in providing a more verbose native
stack trace.

Preparing to Reproduce a Crash
------------------------------

Once a crash is experienced, it is best to try to reproduce it
immediately, under a “debugging” environment. The main requirement is to
simply try running Banshee from a terminal, so trace information can be
seen. However, there are a few things that can be done differently to
produce better data.

Banshee provides a `banshee` shell script that is installed to
`$(prefix)/bin`. It sets a few environment variables, and runs the
`mono` runtime program. This can be done manually from the command line,
and the Mono `--debug` option can be added. This will use the `.mdb`
files installed for each Banshee assembly to produce better managed
stack traces (for instance, code line numbers are printed).

**Run Banshee manually from command line**

`$ mono --debug /usr/lib/banshee/banshee.exe`

After running Banshee using this method, try reproducing the crash. If a
managed stack trace is printed after the crash, copy and paste the trace
into a text editor. If you notice the words “Segmentation Fault” or a
native stack trace following a managed stack trace, further debugging
may be necessary. If this is not the case, please [file the
bug](/wiki/Bugs "wikilink"), and include your full managed trace and
instructions on reproducing the crash.

Getting a Backtrace for a Segfault
----------------------------------

First, set up your `~/.gdbinit` file. This will instruct gdb to handle
some special signals that Mono uses, as well as automate the managed
code backtrace that we will be using:

`$ cat > ~/.gdbinit << `“`EOF`”  
`handle SIGXCPU SIG35 SIG33 SIGPWR nostop noprint`  
  
`define mono_backtrace`  
` select-frame 0`  
` set $i = 0`  
` while ($i < $arg0)`  
`   set $foo = mono_pmip ($pc)`  
`   if ($foo == 0x00)`  
`     frame`  
`   else`  
`     printf `“`#%d`` ``%p`` ``in`` ``%s\n`”`, $i, $pc, $foo`  
`   end`  
`   up-silently`  
`   set $i = $i + 1`  
` end`  
`end`  
  
`EOF`

Now run Banshee inside `gdb`:

`$ gdb --eval-command=run --args mono --debug /usr/lib/banshee/banshee.exe`

Banshee will now start to run. Once started, attempt to reproduce the
crash. If a segfault happens (SIGSEGV), execution will be paused and you
will return to the `gdb` prompt. Once this happens:

`(gdb) mono_backtrace 15`

That will produce a backtrace of the last 15 calls; automatically
showing managed names.

Now in your terminal, scroll up to where you started `gdb` and copy all
of the output. This selection is your native trace that will be useful
on [bug reports](/wiki/Bugs "wikilink").

Other Resources
---------------

If you would like to learn a lot more about debugging Mono applications
by displaying all exceptions, getting threaded stack traces, and tracing
program flow in some or all namespaces, read the Mono Project's
[Debugging](http://www.mono-project.com/Debugging) page.
