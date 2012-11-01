# -*- coding: utf-8 -*-
import gtk,gobject
logo_file = "./pic/lenovo5.jpg"
#logo_file = "./pic/girl.gif"
class tempBox(gtk.VBox):
        def __init__(self):
                super(tempBox,self).__init__()
                logo = gtk.Image()
                logo.set_from_file(logo_file)
		#logo.set_size_request(80, 30)
                label = gtk.Label("Computer view")
		label.set_markup("<span font=\"12.5\" >Computer view</span>")
		hbox = gtk.HBox()
		hbox.pack_start(label, False, False, 1)
#                progress1 = gtk.ProgressBar()
#                progress1.set_text("dfffffffff")
#                progress1.set_pulse_step(0.01)
#                progress1.set_fraction(0.5)
#                progress1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(51400, 61400, 51400))
#                progress1.modify_bg(gtk.STATE_ACTIVE, gtk.gdk.Color(1400, 61400, 51400))
#                progress1.modify_bg(gtk.STATE_INSENSITIVE, gtk.gdk.Color(1400, 6140, 51400))
#                progress1.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(1400, 61400, 1400))
#                progress1.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(51400, 61400, 51400))
#                progress1.modify_base(gtk.STATE_NORMAL, gtk.gdk.Color(51400, 61400, 51400))
		cpuTemp = self.create_temp("CPU", 20)
		videoTemp = self.create_temp("Video", 40)
		hdTemp = self.create_temp("Harddisk", 60)
		zbTemp = self.create_temp("Motherboard", 80)
                self.pack_start(logo, False, False, 2)
                self.pack_start(hbox, False, False, 7)
                self.pack_start(cpuTemp, False, False, 7)
                self.pack_start(videoTemp, False, False, 7)
                self.pack_start(hdTemp, False, False, 7)
                self.pack_start(zbTemp, False, False, 7)
#               self.pack_start(label, False, False, 2)
#               self.pack_start(progress1, False, False, 2)
		

	def create_temp(self,tempType,tempValue):
		vbox = gtk.VBox()
		progress1 = gtk.ProgressBar()
                progress1.set_text(tempType)
                progress1.set_pulse_step(0.01)
                progress1.set_fraction(tempValue/100.00)
		hbox = gtk.HBox()
		label1 = gtk.Label()
		label1.set_markup("<span font=\"12.5\" >%s temp \t</span>"%(tempType) )
		label2 = gtk.Label()
		if tempValue > 60 :
			strTemp = "".join("<span font=\"12.5\" foreground=\"red\">%s ℃ </span>" % tempValue)
		else:
			strTemp = "".join("<span font=\"12.5\" foreground=\"green\">%s ℃ </span>" % tempValue)
		label2.set_markup(strTemp)
	
		hbox.pack_start(label1, False, False, 1)
		hbox.pack_start(label2, False, False, 1)
		
		vbox.pack_start(progress1, False, False, 1)
		vbox.pack_start(hbox, False, False, 1)
		return vbox	
