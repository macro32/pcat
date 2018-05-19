# pcat
Photograph catalogue maker

So here's the thing. I wanted to find a photo of a rose that I took and made a graphite drawing of but I could not find it in my photo directories. I can't remember where it came from. And I haven't kept a note of what I did. Which is naughty but it happens.

This is going to help me start a proper catalogue of 15+ years worth of photographs. Starting with pulling the EXIF data that gets embedded into jpg images. The libexif library and exif program are written in C, with no dependencies. They are command line driven and output to stdout. So they are easy to run from a Python script and just pipe data into text files for processing. I am not interested in neat integration, just getting the basic info into a database.

It was suggested to me that there might be some great applications out there that do a fantastic job with photos. Perhaps even everything that I want. So my thoughts are pretty straightforward. 

So my requirements are pretty straightforward:

* runs on Linux (currently I run lubuntu, but will need to get some new kit soon, may get FreeBSD compatible, even considering a MacBook, but not sure I can justify the expense for something that seems to be stagnating)
* provides good tag support, eg searches, number of tags, stuff you might get with a good SQL query
* it would be very nice and very handy to have some sort of image recognition capability
* handle notes
* handle location
* handle scene types well (another 'tag' thing, but maybe more...)
* it costs neawt
* command line is fine (who *needs* a stinking GUI?)

Why haven't I considered the photo manager applications? Well, the best cost, but a modest price would be considered. However, a lifetime of not paying for most of my software has spoiled me, and made me reluctant to give someone money for something I can implement myself, whatever the requirements. If I do look for stuff then my reduced circumstances mean free and Open Source is even more attractive. Rolling your own is quite satisfying and a way of keeping my hand in.

Still, it doesn't hurt to check out the stuff that will run on Linux. I use Shotwell as my photo maanger for no other reason than it runs on Linux and seems OK. Can't complain. Can't extol. I had Lightroom recommended highly today so I will check that out. At first glance it does seem tied to Windows and Mac, so it may be a non-starter.

