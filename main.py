#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: tom
#update: 2012.10.09
#version: 1.1.2
#description:
#This is a test tool
#
#changelog:
#
import gtk, gobject
import ConfigParser
import MySQLdb
import test
import os
import commands
import pickle
import pango
import time

import dm_top
import dm_center
WIN_WIDTH=600
WIN_HEIGHT=540
class MainUI(gtk.Window):
        def __init__(self):
                super(MainUI,self).__init__()
                self.set_title("Linpus device manager")
                self.set_size_request(WIN_WIDTH,WIN_HEIGHT)
                self.set_position(gtk.WIN_POS_CENTER)
                self.vbox=gtk.VBox(False, 2)
		hb_top = dm_top.dm_topbar();
		hb_center = dm_center.dm_main()
		self.vbox.pack_start(hb_top, False, False,10)
		self.vbox.pack_start(hb_center, False, False,10)
                self.add(self.vbox)
		self.connect("destroy", gtk.main_quit)
		self.vbox.show_all()
		self.show_all()
MainUI()
gtk.main()

