#update: 2012.10.26
#version: 1.1.2
#description:
#This is a test tool
#
#changelog:
#
import gtk, gobject
import dm_common_func as comf
bg_color=gtk.gdk.Color(60000, 65000, 55003, 60000)
class dm_botBox(gtk.HBox):
        def __init__(self):
                super(dm_botBox,self).__init__()
                label=gtk.Label("version v0.1  linpus")
		strlab="<span font=\"12.5\" >version v0.1  linpus</span>"
		label.set_markup(strlab)
                self.pack_start(label, False, False,15)
		comf.modify_window_bgcolor(self, bg_color)
