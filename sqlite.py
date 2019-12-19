#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sqlite.py
#  
#  Copyright 2018 john ratcliffe
#  
#  sqlite3 database handler
#
#  creates and manipulates sqlite tables holding the exif data
#
#  not sure of the best way of holding the data. there are a lot of {key,value}
#  pairs around, but I am not sure this indicates I need this kind of structure rather than
#  an RDBMS, starting with sqlite as the store. might have to try both. be an interesting
#  exercise anyway.
#
#  
#

import sqlite3

class Sqlite:
	
	def __init__(self):
		self.db_file = "photographs.db"

		self.sql_create_image_table = """CREATE TABLE IF NOT EXISTS images (
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

		self.sql_insert_image = """INSERT INTO images (
			filename,
			location,
			technical,
			composition,
			suitability,
			event,
			scene_type,
			notes)
		VALUES ( ?,?,?,?,?,?,?,? )
		"""


		self.sql_create_tag_table = """CREATE TABLE IF NOT EXISTS tags (
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

		self.sql_insert_tags = """INSERT INTO tags (
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
		self.sql_create_property_table = """CREATE TABLE IF NOT EXISTS property (
			id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			images_id REFERENCES images( id ), 	-- foreign key
			name VARCHAR(128),	-- mostly shortish text, integers or floats, we'll see
			value VARCHAR(256), -- sort of an enum but there may be a better way
			type INTEGER DEFAULT 0
		)"""

		self.sql_insert_property = """INSERT INTO property (
			images_id,
			name,
			value,
			type
			)
		VALUES (?,?,?,?)  
		"""

	def create_connection(self):
    """ create a database connection to a SQLite database """
    """ if the file does not exist then it is created     """
    conn = None
    try:
        conn = sqlite3.connect(self.db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
	return conn

	# use sqlite for now...
	# alternate is to use a different DB, like the {key, value} nosql shit
	# todo: have another look at the fashionable nosql dbs
	def execute_noreturn(self, sql):
		conn = create_connection()
		c = self.conn.cursor()
		c.execute(sql)
		id = c.lastrowid
		self.conn.commit()
		self.conn.close()
		return id

		
	def execute(self, sql, values):
		conn = create_connection()
		c = self.conn.cursor()
		c.execute(sql, values)
		id = c.lastrowid
		self.conn.commit()
		self.conn.close()
		return id


	def create_image_table(self):
		self.execute_noreturn( self, sql_create_image_table )


	def create_tag_table(self):
		self.execute_noreturn( self, sql_create_tag_table )
		
		
	def create_property_table(self):
		self.execute_noreturn( self, sql_create_property_table )
		
            
	def create_image_database(filename):
		if not filename:
			self.db_file = filename
		self.create_image_table()
		self.create_tag_table()
		self.create_property_table()
		
		
	def insert_image(self, image_data):
		pass
		
	
	def insert_tag(self, tag_data):
		pass
		
		
	def insert_property(self, property_data):
		pass
