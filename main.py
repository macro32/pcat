#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2018 john@johnratcliffe.com
#  

import sqlite
import exif


# process the program arguments
import argparse
import itertools

parser = argparse.ArgumentParser(description='Process image files to start a catalogue.')
parser.add_argument('-r', '--rootdir',
                    help='root directory for the source image files')
parser.add_argument('-f', '--filename', default='001.jpg',
                    help='a single source image file')
parser.add_argument('-t', '--filetype', default='jpg',
                    help='file type to process (e.g. jpg)')

def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)
 
parser.add_argument('-s', '--startdate', 
                    help='Start date (format YYYY-MM-DD)', 
                    type=valid_date)
parser.add_argument('-e', '--enddate', 
                    help='End date (format YYYY-MM-DD)', 
                    type=valid_date)

parser.add_argument('-d', '--database', 
                    help='Database name',
                    default='photo_catalogue.db')

# different and mutually exclusive requirement processing
compatible_options1 = ( '-x', '-a', '-n' )
parser.add_argument('-x', '--extract', 
                    help='Extract all exif data and save to sqlite database')

parser.add_argument('-a', '--add', 
                    help='Add extra tag data from file and save to sqlite database')

parser.add_argument('-n', '--notes', 
                    help='Add notes from file and save to sqlite database')

# the following are speculative and assume I will run separate ID software for different types of images
compatible_options2 = ( '-b', '-p' )
parser.add_argument('-b', '--botanical', 
                    help='Run image id for flowers and save to sqlite database')

parser.add_argument('-p', '--portrait', 
                    help='Run portrait id for portraits and save to sqlite database')
                    

exclusives = itertools.product(compatible_options1, compatible_options2)
for exclusive_grp in exclusives:
    group = parser.add_mutually_exclusive_group()
    group.add_argument(exclusive_grp[0])
    group.add_argument(exclusive_grp[1])



                                
args = parser.parse_args()


# set up operational parameters
def init():
	print( "init()" )
	# check program args
	# extract args and create processing classes
	db = sqlite.Sqlite()
	data = exif.Exif()
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
