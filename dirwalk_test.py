#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dirwalk_test.py
#  
#  Copyright 2019 john ratcliffe
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


args = parser.parse_args()

	
def process_result( f, result ):
	exif = ET.fromstring(result)
	elements = exif.getiterator()
	for e in elements:
		print( e.tag )
		print( e.text )
	
	
def get_exif_data( file ):
	result = subprocess.run( ['exif', '-x', file], stdout=subprocess.PIPE ).stdout.decode('utf-8')
	process_result( file, result )


def extract( root, files ):
	for f in files:
		filename = join(root, f)
		name, extension = os.path.splitext( filename )
		extension = extension[1:].lower()
		if extension == args.filetype:
			get_exif_data( filename )
		
def process():
	for root, dirs, files in os.walk('/home/john/Pictures'):
		if len(files) > 0:
			if files != []:
				extract( root, files )
        
def main(args):
    print( "pcat: photo catalogue generator: directory/file walking test" )
    print( "processing...." )

    process()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
