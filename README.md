# pcat
Photograph catalogue maker

So here's the thing. I wanted to find a photo of a rose that I took and made a graphite drawing of but I could not find it in my photo directories. I can't remember where it came from. And I haven't kept a note of what I did. Which is naughty but it happens.

This is going to help me start a proper catalogue of 15+ years worth of photographs. Starting with pulling the EXIF data that gets embedded into jpg images. The libexif library and exif program are written in C, with no dependencies. They are command line driven and output to stdout. So they are easy to run from a Python script and just pipe data into text files for processing. I am not interested in neat integration, just getting the basic info into a database.
