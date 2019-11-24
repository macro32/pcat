#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  extractexif_test.py
#  
#  Copyright 2019 john <john@sibelius>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import glob

# process the program arguments
import argparse
import itertools

import logging

# logger stuff
logger = logging.getLogger('pcat')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('pcat.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

parser.add_argument('-r', '--rootdir',
                    help='root directory for the source image files')

group = parser.add_mutually_exclusive_group()
group.add_argument('-f', '--filename', default='001.jpg',
                    help='a single source image file')

group.add_argument('-t', '--filetype', default='jpg',
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

args = parser.parse_args()

# set up operational parameters
def init():
	# check program args
	# extract args and create processing classes
	# set up logging
	# set up database

def extract( files ):
	for f in files:
		get_exif_data( f )
		
# process the files
def process():
	files = glob.glob( './*.JPG' )
	extract( files )
	# for each directory
	#   get list of files
	#   for each file
	#     extract exif data
	#     select all tags of interest
	#     create database entry with the tag data

def main(args):
    print( "pcat: photo catalogue generator: test directory/file walking" )
    print( "processing...." )
    
    init()
    process()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
