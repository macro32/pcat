#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  test_file.py
#  
#  Copyright 2019 john ratcliffe
#  

import unittest
import exif_file_handler

class TestFileMethods( unittest.TestCase):
	
	def test_file():
		fh = ExifFileHandler('/home/john/Pictures', 'jpg')

if __name__ == '__main__':
    unittest.main()
