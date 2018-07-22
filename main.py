#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2018 john@johnratcliffe.com
#  

import sqlite
import exif
import glob
import subprocess

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
	x_resolution_orientation UNSIGNED INTEGER,
	y_resolution_orientation UNSIGNED INTEGER,
	resolution_unit_orientation VARCHAR(16),
	date_and_time DATETIME,
	YCbCr_positioning VARCHAR(32),
	compression VARCHAR(64),
	x_resolution_compression UNSIGNED INTEGER,
	y_resolution_compression UNSIGNED INTEGER,
	resolution_unit_compression VARCHAR(16),
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

sql_insert_tags = """INSERT INTO tags (
	image_description,
	manufacturer,
	model,
	orientation,
	x_resolution_orientation,
	y_resolution_orientation,
	resolution_unit_orientation,
	date_and_time,
	YCbCr_positioning,
	compression,
	x_resolution_compression,
	y_resolution_compression,
	resolution_unit_compression,
	exposure_time,
	f_number,
	iso_speed_ratings,
	exif_version,
	original_date_and_time,
	digital_date_and_time,
	components_configuration,
	compressed_bits_per_pixel,
	shutter_speed,
	aperture,
	exposure_bias,
    maximum_aperture_value,
    metering_mode,
    flash,
    focal_length,
    maker_note,
    user_comment,
    flash_pix_version,
    colour_space,
    pixel_x_dimension,
    pixel_y_dimension,
    focal_plane_x_resolution,
    focal_plane_y_resolution,
    focal_plane_resolution,
    sensing_method,
    file_source,
    custom_rendered,
    exposure_mode,
    white_balance,
    digital_zoom_ratio,
    scene_capture_type,
    interoperability_ind,
    interoperability_version,
    relatedimagewidth,
    relatedimagelength	
    )
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
"""

# alternate number 1 is to use simplified 'property' type associations
sql_create_property_table = """CREATE TABLE IF NOT EXISTS property (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	images_id REFERENCES images( id ), 	-- foreign key
	name VARCHAR(128),	-- mostly shortish text, integers or floats, we'll see
	value VARCHAR(256), -- sort of an enum but there may be a better way
	type INTEGER 
)"""

sql_insert_property = """INSERT INTO property (
	images_id,
	name,
	value,
	type
	)
VALUES (?,?,?,?)  
)"""

# alternate number 2 is to use a different DB, like the {key, value} nosql shit
# todo: have another look at the fashionable nosql dbs

# set up operational parameters
def init():
	print( "init()" )
	# check program args
	# extract args and create processing classes
	db = sqlite.Sqlite()
	sql = sql_create_image_table
	print( sql )
	db.execute( sql )
	sql = sql_create_tag_table
	print( sql )
	db.execute( sql )
	sql = sql_create_property_table
	print( sql)
	db.execute( sql )
	data = exif.Exif()
	# set up logging
	# set up database

def process_result( result ):
#	print( result )
	lines = result.split( '\n' )
	split_lines = []
	for i in range( 0, len(lines) ):
		try:
			split_lines.append(lines[i].split('|')[0])
			split_lines.append(lines[i].split('|')[1])
		except Exception as e:
			print( e )
	print( lines )
			
	
	
def get_exif_data( file ):
	print( file )
	result = subprocess.run( ['exif', file], stdout=subprocess.PIPE ).stdout.decode('utf-8')
	process_result( result )
	
	
def extract( files ):
	for f in files:
		get_exif_data( f )
		
# process the files
def process():
	print( "process()" )
	files = glob.glob( './*.JPG' )
	print( files )
	extract( files )
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
	

# process an image file, start with jpgs and
# extract EXIF data
 

def main(args):
    print( "pcat: photo catalogue generator" )
    print( "processing...." )
    
    init()
    process()
#    cleanup()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
