# pcat
Photograph catalogue maker

So here's the thing. I wanted to find a photo of a rose that I took and made a graphite drawing of but I could not find it in my photo directories. I can't remember where it came from. And I haven't kept a note of what I did. Which is naughty but it happens.

This is going to help me start a proper catalogue of 15+ years worth of photographs. Starting with pulling the EXIF data that gets embedded into jpg images. The libexif library and exif program are written in C, with no dependencies. They are command line driven and output to stdout. So they are easy to run from a Python script and just pipe data into text files for processing. I am not interested in neat integration, just getting the basic info into a database.

It was suggested to me that there might be some great applications out there that do a fantastic job with photos. Lightroom was highly recommended today and a quick Google turns up Luminar 2018 which seems a distinct rival. 

So let's start with my requirements, which are pretty straightforward:

* runs on Linux (currently I run lubuntu, but will need to get some new kit soon, may get FreeBSD compatible, even considering a MacBook, but not sure I can justify the expense for something that seems to be stagnating)
* provides good tag support, eg searches, number of tags, stuff you might get with a good SQL query
* it would be very nice and very handy to have some sort of image recognition capability
* handle notes
* handle location
* handle scene types well (another 'tag' thing, but maybe more...)
* does a bunch of reconciliation between what I think I have, and what it is (e.g dates)
* use existing libraries and services which comply (i.e. cost neawt)
* it costs neawt
* command line is fine (who *needs* a stinking GUI?)

Use Cases are good. Let's do a Use Case or three.

1. Extract date taken. Save to DB. Check with current directory (yyyy/mm/dd). Flag differences.
2. Add location(s). I can remember most.
3. Add tags indicating content (e.g Landscape, River, Seascape, Sunset, Sunrise, Flower, Rose, ...)
4. Add notes. Context. Special circumstances. Memories. 
5. Add quality indicator. Subjective, but useful. Technical quality, composition, potential usefulness, are all factors.
6. Extract technical data. Save to DB. Specifically f-stop, exposure, ISO, etc.
7. Auto analyse content to help with tagging. Ambitious, maybe. But instructive and fun. Portraits. Flowers. For starters.

Why haven't I considered the photo manager applications? Well, the best cost, but a modest price would be considered. However, a lifetime of not paying for most of my software has spoiled me, and made me reluctant to give someone money for something I can implement myself, whatever the requirements. My reduced circumstances mean free and Open Source is even more attractive. And rolling your own is quite satisfying and a way of keeping my hand in.

Still, it doesn't hurt to check out the stuff that will run on Linux. I use Shotwell as my photo maanger for no other reason than it runs on Linux and seems OK. Can't complain. Can't extol. Lightroom was recommended  but at first glance it does seem tied to Windows and Mac, so it may be a non-starter. Similarly with Luminar. I need to investigate more closely and tie down what I actually want.

It looks like Lightroom only runs on recent Windows or macOS versions. The only Windows I run is an old XP box for my retro games. I have no plans to run Windows in the near future. And as much as I want to run macOS, I really find it hard to justify the cost, given what they have done with the MacBook Pro. So it looks like a no go for Lightroom.

So after a couple of days reflection. The Use Cases aren't brilliant. Perhaps.... 

1. Collate, consolidate and check what I have.
   * remove duplicates
   * check and fix dates
   * check I have everything
   
2. Add additional information
   * assign tags for location
   * add (tags?) quality indicator(s) - technical, composition, feasibility for a painting
   * add tag(s) for difficulty to turn into a painting
   * extract EXIF data and save it in searchable format
 
3. Analyse image for content
   * recognition software or manual? flowers, portraits should be relatively easy, what else?, add tags
   
4. Add context and personal comment and additional content
   * personal notes on the scene (feelings, opinion)
   * context notes (event, background)
   
   

