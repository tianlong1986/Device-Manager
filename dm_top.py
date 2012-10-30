#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: tom
#update: 2012.10.26
#version: 1.1.2
#description:
#This is a test tool
#
#changelog:
#
import gtk, gobject

class dm_topbar(gtk.HBox):
	def __init__(self):
        	super(dm_topbar,self).__init__()
		label=gtk.Label("hardware check")
		self.pack_start(label, False, False,5)

	
