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

parser = argparse.ArgumentParser(description='Process image files to start a catalogue.', prog='pcat')

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

parser.add_argument('-d', '--database', 
                    help='Database name',
                    default='photo_catalogue.db')


group = parser.add_mutually_exclusive_group()
group.add_argument('-x', '--extract', 
                    help='Extract all exif data and save to sqlite database')
                    
group.add_argument('-a', '--add', 
                    help='Add extra tag data from file and save to sqlite database')

group.add_argument('-n', '--notes', 
                    help='Add notes from file and save to sqlite database')

group = parser.add_mutually_exclusive_group()
group.add_argument('-b', '--botanical', 
                    help='Run image id for flowers and save to sqlite database')
                    
group.add_argument('-p', '--portrait', 
                    help='Run portrait id for portraits and save to sqlite database')
                                                   
args = parser.parse_args()

sql_create_image_table = """CREATE TABLE IF NOT EXISTS images (
    id AUTO
	filename VARCHAR(256),
	location VARCHAR(256),
	technical UNSIGNED INTEGER,
	composition UNSIGNED INTEGER,
	suitability UNSIGNED INTEGER,
	event VARCHAR(256),
	scene_type VARCHAR(32),
	notes TEXT
)
"""



sql_create_tag_table = """CREATE TABLE IF NOT EXISTS tags
	image_description VARCHAR(128),
	manufacturer VARCHAR(32),
	model VARCHAR(64),
	orientation VARCHAR(32),
	x-resolution UNSIGNED INTEGER,
	y-resolution UNSIGNED INTEGER,
	resolution_unit VARCHAR(16),
	date_and_time DATETIME,
	YCbCr_positioning VARCHAR(32),
	compression VARCHAR(64),
	x_resolution UNSIGNED INTEGER,
	y_resolution UNSIGNED INTEGER,
	resolution_unit VARCHAR(16),
	exposure_time VARCHAR(16),
	f-number VARCHAR(16),
	iso_speed_ratings UNSIGNED INTEGER,
	
Image Description   |                               
Manufacturer        |Canon
Model               |Canon PowerShot G12
Orientation         |Top-left
X-Resolution        |180
Y-Resolution        |180
Resolution Unit     |Inch
Date and Time       |2016:06:11 10:48:50
YCbCr Positioning   |Co-sited
Compression         |JPEG compression
X-Resolution        |180
Y-Resolution        |180
Resolution Unit     |Inch
Exposure Time       |1/250 sec.
F-Number            |f/4.0
ISO Speed Ratings   |80
Exif Version        |Exif Version 2.3
Date and Time (Origi|2016:06:11 10:48:50
Date and Time (Digit|2016:06:11 10:48:50
Components Configura|Y Cb Cr -
Compressed Bits per | 3
Shutter Speed       |7.97 EV (1/250 sec.)
Aperture            |4.00 EV (f/4.0)
Exposure Bias       |0.00 EV
Maximum Aperture Val|3.34 EV (f/3.2)
Metering Mode       |Pattern
Flash               |Flash did not fire, auto mode
Focal Length        |10.8 mm
Maker Note          |2764 bytes undefined data
User Comment        |
FlashPixVersion     |FlashPix Version 1.0
Colour Space        |sRGB
Pixel X Dimension   |3648
Pixel Y Dimension   |2736
Focal Plane X-Resolu|12493.151
Focal Plane Y-Resolu|12493.151
Focal Plane Resoluti|Inch
Sensing Method      |One-chip colour area sensor
File Source         |DSC
Custom Rendered     |Normal process
Exposure Mode       |Auto exposure
White Balance       |Auto white balance
Digital Zoom Ratio  |1.0000
Scene Capture Type  |Standard
Interoperability Ind|R98
Interoperability Ver|0100
RelatedImageWidth   |3648
RelatedImageLength  |2736
"""

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
