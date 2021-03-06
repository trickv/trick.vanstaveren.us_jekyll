---
title: Gentoo/Dev/EbuildQuiz2
permalink: wiki/Gentoo/Dev/EbuildQuiz2/
layout: wiki
---

original:
[<http://www.gentoo.org/proj/en/devrel/quiz/ebuild-quiz.txt>](http://www.gentoo.org/proj/en/devrel/quiz/ebuild-quiz.txt)

------------------------------------------------------------------------

Ebuild development quiz Revision 1.11.1 - 01 January 2007 Answer in
whatever length necessary for completeness. Review documentation.
Consult your mentor if you're unable to locate answers.

-   -   Organizational structure questions

1. When is it appropriate to post to gentoo-core rather than gentoo-dev?

2. Who should be contacted with complaints about specific developers or

`   projects?`

3. What is the proper method for suggesting a wide-ranging feature or

`   enhancement to Gentoo?`

4. What is the purpose of the Gentoo Council?

5. What is the purpose of the Gentoo project structure?

6. What is the purpose of herds? To allow developers who work on similar
packages to collaborate and share work.

-   -   Ebuild technical/policy questions

1. You 1. You change a package's ebuild to install an init script.
Previously,

`   the package had no init script at all.`  
`   Is a revision bump necessary? Why? What about when adding a patch?`

-   -   yes, a new revision is required, else current users will not get
        the script installed. unless it is a trivial init script. i
        can't think of an example where an init script is trivial.
    -   with adding a patch, it is necessary unless the patch fixes a
        build failure (in which case the package would nt be installed
        anywhere regardless.) user submits a “live” CVS ebuild. What
        would be a preferable

`   alternative to such an ebuild?`

A versioned CVS ebuild, which pulls from CVS using a specific date stamp
(or -r for SVN) so that the code users would compile does not change.
Better yet, a CVS snapshot could be used if upstream's CVS server is
unreliable, overloaded, or if the upstream developers can recommend one
based on the state of the code.

3. (a) What is repoman? How would you check for QA problems with

`  repoman?`

-   repoman is a bit of a wrapper for cvs and helper for managing and
    making commits to the portage tree.

`  (b) A user submits a brand-new ebuild for a new package. What are the`  
`   proper steps (including repoman/cvs commands) to take to add`  
`   this ebuild to the tree?`

4. A user submits an ebuild that has numerous technical problems and

`   violates policy. How would you handle that situation?`

5. You have a set of new ebuilds that could potentially benefit

`   from a global USE flag. What steps should be taken before`  
`   a new USE flag is implemented? What should be done if the`  
`   USE flag only applies to a single package?`

-   First must be discussed on the gentoo-dev mailing list
    -   There may already be a similar use flag, or
    -   Other packages may want to use it and it should be generic
        enough for others to use
-   It must be used by more than one project; else it belongs as a local
    use flag

6. You're creating an ebuild. Unfortunately, the ebuild's 'make install'

`   target causes numerous access violations. What is the best `  
`   course of action to take to have a clean, straightforward`  
`   ebuild?`

-   Get to the root of the problem - fix whatever part(s) of the autofoo
    system are broken and go from there. Ship a patch with the ebuild
    that fixes the sandbox violations, and work with upstream (or at
    least file a bug with them) to get the build system fixed.

7. You're creating an ebuild that needs a patch. The patch is

`   nontrivially large - bigger than 20kbytes. Where should`  
`   the patch be kept?`

-   Within the Gentoo mirrors system; patches can be tarred up and added
    to SRC\_URI so they get fetched with the package itself. This will
    keep the CVS tree from growing any bigger than it needs to be.

8. You're creating an ebuild that has its own license - one that

`   doesn't exist in /usr/portage/licenses/. What is the proper`  
`   course of action?`

-   First, make sure the new license permits us to use the package with
    Gentoo :)
-   Put it in a (preferrably plain text) file into the portage tree's
    licenses directory and commit it before submitting the ebuild to the
    tree.

9. (a) You wish to have an ebuild marked “stable,” taking it out of

`   ~ARCH KEYWORDS. It's a library. What steps should`  
`   be taken to do so?`

`  (b) You wish to mark an ebuild `“`testing,`”` putting it into ~ARCH`  
`   KEYWORDS. It was previously hard-masked in package.mask.`  
`   What should be done prior to doing so?`

`  (c) You wish to have an ebuild marked `“`stable.`”` It is a popular`  
`   application, but no other ebuilds depend on it.`  
`   What should be done first?`

10. You're committing a user-submitted ebuild. What should be in the

`   initial ChangeLog?`

11. What is the difference between DEPEND and RDEPEND?

-   DEPEND is compile time dependencies - eg. compiler requirements,
    build libraries, etc.
-   RDEPEND is run time dependencies - dynamic linked libraries, and
    anything else that's required to run.

12. You wish to make a change to an ebuild, but you checked

`   ChangeLogs and metadata.xml and it appears to be maintained by `  
`   someone else. How should you proceed?`

13. You find a situation in which an eclass may be useful. What should

`   you do before implementing such an eclass?`

14. You find a package that will not build on some architectures without

`   PIC (-fPIC) code in the shared libraries. What is the proper way`  
`   to handle this situation?`

15. What do you do when you'd like to have a package you maintain

`   tested or marked stable on other architectures?`

-   File a bug with the respective arch team, or contact a developer
    directly.

16. How can you verify an ebuild has correct run time dependencies

`   (RDEPEND) for all installed binaries?`

17. How do you deal with a situation in which an ebuild wishes to

`   install a file already installed by another package?`

-   There are few situations where this can happen, and the course of
    action is to either:
    -   Set the other package as a blocker. This way the two packages
        cannot be installed at the same time. Or,
    -   Have the ebuild depend on the other package, and then simply not
        install the file.
-   Which is best depends on which packages are being dealt with.

18. Most configure scripts attempt to automatically determine

`   settings based on the host system. When should the ebuild`  
`   specifically override settings?`

-   To implement USE flags
-   To enforce that any other gentoo specific things are picked up,
    including configured build tools, our filesystem heirarchy standard,
    etc.

<!-- -->

-   -   Please also submit the following information:

<!-- -->

-   GPG public key ID (if you do not have one, please create one)

<!-- -->

-   Date of birth: 1983-12-13

<!-- -->

-   Where do you live (Town/City, Country): Chicago, IL, USA

<!-- -->

-   What are your programming/scripting skills, if applicable?

<!-- -->

-   What other areas are you experienced in?

<!-- -->

-   What other projects have you contributed to, if any?
    -   Banshee music player; author of several plugins as well as
        MTP-DAP interface
    -   libgphoto2-sharp (maintainer) and libgphoto2 “enthusiast” (will
        write code someday, I swear!
    -   lirc-sharp (author)...bit of a sleeping project, but I will get
        back to it
    -   Used to hack xfce back in the day...but those were the bored
        college daze...

<!-- -->

-   Tell us about yourself. This doesn't need to be strictly

`  computer-relevant; things like where you're from,`  
`  hobbies, job, family, interests...`

-   -   Love to cycle, lots and lots :)
    -   If you can buy it at Starbucks, it's my kind of drink.
    -   Work my 9-5 as a PHP/MySQL developer, so I love any language
        that is typed (not as in keyboard, but as in variables).
    -   I love to watch people interact with computers and tell them how
        badly their computer is designed. It's so true.

  
q!
