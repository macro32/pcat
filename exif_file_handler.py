#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  exif_file_handler.py
#  
#  Copyright 2019 john ratcliffe
#  

import os
from os.path import join, getsize
import subprocess

import xml.etree.ElementTree as ET

class ExifFileHandler:
	
	def __init__(self, root_dir, file_type):
		self.rootdir = root_dir
		self.filetype = file_type
		
	def process_result( f, result ):
#		return ET.fromstring(result)
		exif = ET.fromstring(result)	
		elements = exif.getiterator()
		for e in elements:
			print( e.tag, ': ', e.text )
		
		
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
		for root, dirs, files in os.walk(rootdir):
			if len(files) > 0:
				extract( root, files )
	
