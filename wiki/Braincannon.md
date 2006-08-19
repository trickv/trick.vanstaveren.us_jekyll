---
title: Braincannon
permalink: wiki/Braincannon/
layout: wiki
---

[Hourly Log](/wiki/Braincannon/Hours "wikilink")

### Task Queue:

Priority Items: 1. Setting a cookie that tracks which tab...**DONE**

2. Develop a better solution for sizing the widgets in the listing
dashboard (xProperties.cfm?action=edit&pUID=whatever). You had some good
ideas as far as strengthening the look of the widgets to help separate
them. I would like you to brainstorm a little and come up with some
ideas to facilitate a good spec for how to treat the size of the widgets
so that some are blumpkined huge and some relatively tiny. Maybe we can
take some of the information off a particularly large widget and put it
into an modal div layer that pops up by pushing a 'Additional Info'
button. They don't have to all be the same size, but it will help to get
them a little closer.

3. We need to work on how to somehow individualize the submit button on
each widget so that it helps to reinforce the idea of the widgets in the
first place. In other words, I as a dingbat user (not a disparaging
comment, just trying to develop for the lowest common denominator)
should somehow intuitively sense that pressing a button on a widget only
updates that widget.

4. Develop some sort of a variable array for the field values on a
widget wide basis. Let me give you the scenario so that you can
brainstorm on it: A user goes into the Listing Info widget and starts
updating some fields with more accurate data. Then they remember that
they just shot some pictures they want to upload and decide to start
doing that. It would be HUGE if the system somehow tracked their field
data in the Listing Info widget(perhaps using cookies), so that when
they finished adding picture(s), they came back to the dashboard and the
data (even though it wasn't actually submitted to the DB by pressing the
Listing Info widget submit button) was there. Or we can figure out a way
to submit all forms when you submit one. Whatever you think makes more
sense. Chew on it and get back to me.

5. Continue to make headway on the form validation. I'm not expecting
you to know every field that we need to have required, but figuring out
how to tackle some of this as an item for you would be great.

Intermediary Items: The photo gallery thing is pretty near and dear to
the WOW factor (and I continue to be impressed with the architected it
with things like dynamically changed the framecount to reflect computing
speed), so chug on that as a constant project.
