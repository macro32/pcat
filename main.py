#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2018 john <john@amadeus>
#  

# process the program arguments
import argparse

parser = argparse.ArgumentParser(description='Process image files to start a catalogue.')
parser.add_argument('-r', '--rootdir',
                    help='root directory for the source image files')
parser.add_argument('-f', '--file', default='image.jpg',
                    help='a single source image file')
parser.add_argument('-t', '--filetype', default='jpg',
                    help='file type to process (e.g. jpg)')
args = parser.parse_args()


# set up operational parameters
def init():
	print( "init()" )
	# check program args
	# extract args and create processing classes
	# set up logging
	# set up database
	pass
	
# process the files
def process():
	print( "process()" )
	# for each directory
	#   get list of files
	#   for each file
	#     extract exif data
	#     select all tags of interest
	#     create database entry with the tag data
	pass
	
# clean up
def cleanup():
	print( "cleanup()" )
	# remove temporary files
	# write summary/statistics
	pass
	

# process an image file, start with jpg
# extract EXIF data
 

def main(args):
    print( "pcat: photo catalogue generator" )
    print( "processing...." )
    
    init()
    process()
    cleanup()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
