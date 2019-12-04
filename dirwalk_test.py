#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dirwalk.py
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
import os
from os.path import join, getsize
import subprocess

from xml.dom import minidom
import xml.etree.ElementTree as ET

# process the program arguments
import argparse
import itertools

import logging

# logger stuff
logger = logging.getLogger('dirwalk_test')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('dirwalk_test.log')
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

args = parser.parse_args()

# set up operational parameters
def init():
	pass
	# check program args
	# extract args and create processing classes
	# set up logging
	# set up database

#def process_result( f, result ):
#	lines = result.split( '\n' )
#	entries = {}
#	for i in range( 0, len(lines) ):
#		try:
#			if lines[i].find( '|') > 0:
#				entries[lines[i].split('|')[0]] = lines[i].split('|')[1]
#		except Exception as e:
#			print( e )
#	print( entries )

def process_result( f, result ):
	print( '<?xml version="1.0"?>\n' + result )
#	tree = ET.fromstring(result)
#	doc = minidom.parseString( result )
#	print( doc )
	
def get_exif_data( file ):
	result = subprocess.run( ['exif', '-x', file], stdout=subprocess.PIPE ).stdout.decode('utf-8')
	process_result( file, result )


def extract( root, files ):
	filetypes = { '.JPG', '.jpg'}
	for f in files:
		print( join(root, f) )
		filename = join(root, f)
		name, extension = os.path.splitext( filename )
		if extension in filetypes:
			get_exif_data( filename )
		
# process the files
def process():
	#files = glob.glob( './*.JPG' )
	#extract( files )
	# assume dir structure is /Pictures/yyyy/mm/dd
	# where only the leaf nodes dd contain files
	#
	# start at root directory
	# for each subdirectory
	#   get list of subdirectories
	#   if subdirectories == [] then
	#     get list of files
	#     for each file
	#       extract exif data
	#       select all tags of interest
	#       create database entry with the tag data
	for root, dirs, files in os.walk('/media/sf_Pictures'):
		if len(files) > 0:
			#print(root, "consumes", end=" ")
			#print(sum(getsize(join(root, name)) for name in files), end=" ")
			#print("bytes in", len(files), "non-directory files")
			if files != []:
				extract( root, files )
			if 'CVS' in dirs:
				dirs.remove('CVS')  # don't visit CVS directories
        
def main(args):
    print( "pcat: photo catalogue generator: directory/file walking test" )
    print( "processing...." )
    
#    init()
    process()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
