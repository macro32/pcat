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
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
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



sql_create_tag_table = """CREATE TABLE IF NOT EXISTS tags (
	image_description VARCHAR(128),
	manufacturer VARCHAR(32),
	model VARCHAR(64),
	orientation VARCHAR(32),
	x_resolution UNSIGNED INTEGER,
	y_resolution UNSIGNED INTEGER,
	resolution_unit VARCHAR(16),
	date_and_time DATETIME,
	YCbCr_positioning VARCHAR(32),
	compression VARCHAR(64),
	x_resolution UNSIGNED INTEGER,
	y_resolution UNSIGNED INTEGER,
	resolution_unit VARCHAR(16),
	exposure_time VARCHAR(16),
	f_number VARCHAR(16),
	iso_speed_ratings UNSIGNED INTEGER,
	exif_version VARCHAR(32),
	original_date_and_time TIMESTAMP,
	digital_date_and_time TIMESTAMP,
	components_configuration VARCHAR(32),
	compressed_bits_per_pixel UNSIGNED INTEGER,
	shutter_speed VARCHAR(64),
	aperture VARCHAR(64),
	exposure_bias VARCHAR(64),
    maximum_aperture_value VARCHAR(64),
    metering_mode VARCHAR(64),
    flash VARCHAR(64),
    focal_length VARCHAR(64),
    maker_note TEXT,
    user_comment TEXT,
    flash_pix_version VARCHAR(64),
    colour_space VARCHAR(16),
    pixel_x_dimension UNSIGNED INTEGER,
    pixel_y_dimension UNSIGNED INTEGER,
    focal_plane_x_resolution REAL,
    focal_plane_y_resolution REAL,
    focal_plane_resolution VARCHAR(16),
    sensing_method VARCHAR(32),
    file_source VARCHAR(16),
    custom_rendered VARCHAR(32),
    exposure_mode VARCHAR(32),
    white_balance VARCHAR(32),
    digital_zoom_ratio REAL,
    scene_capture_type VARCHAR(16),
    interoperability_ind VARCHAR(16),
    interoperability_version UNSIGNED INTEGER,
    relatedimagewidth UNSIGNED INTEGER,
    relatedimagelength UNSIGNED INTEGER	
    )
"""

# set up operational parameters
def init():
	print( "init()" )
	# check program args
	# extract args and create processing classes
	db = sqlite.Sqlite()
	sql = sql_create_image_table
	print( sql)
	db.execute( sql )
	sql = sql_create_tag_table
	db.execute( sql )
	data = exif.Exif()
	# set up logging
	# set up database

	
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
#    process()
#    cleanup()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
