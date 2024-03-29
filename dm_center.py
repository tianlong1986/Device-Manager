# -*- coding: utf-8 -*-
import gtk, gobject
import os
import pango
import time
import thread
from xml.etree import ElementTree
import dm_detail
from dm_temperature import tempBox
import dm_common_func as comf 

#hwinfo_file = "/tmp/.hwinfo.xml"
win_bg_image="/usr/share/autotest/bg/1.jpg"

hwinfo_file = "./hwinfo.xml"
list_text_color = gtk.gdk.Color(60000, 5000, 30003, 60000)
#list_text_bk_color = gtk.gdk.Color(3800, 17600, 2303, 60000)#深绿色
list_text_bk_color = gtk.gdk.Color(38000, 57600, 65303, 60000)
win_bg_color=gtk.gdk.Color(60000, 65000, 55003, 60000)
win_fg_color=gtk.gdk.Color(60, 55500, 33,63000)
class dm_main(gtk.HBox):
	def __init__(self):
		super(dm_main, self).__init__()
		self.hwlist = self.createList()
		infoview = self.createView()
		other = tempBox()
		other.set_size_request(200,500)
		self.pack_start(self.hwlist, False,False,5)
		self.pack_start(infoview, False,False,10)
		self.pack_start(other, False,False,5)
		#self.set_size_request(100, 150)
	
		self.dictTag = {'ALL':'tom',
				'CPU':'cpu', 
				'ZB':'core', 
				'VGA':'display', 
				'HD':'ide', 
				'DRM':'driver', 
				'NET':'network', 
				'SOUND':'multimedia', 
				'MEM':'memory'}
	def createList(self):
	        store = gtk.ListStore(gobject.TYPE_STRING,
                                     gobject.TYPE_STRING)
                #for item in self.alltype:
                store.append(("ALL","Computer View"))
                store.append(("DRM","Driver View"))
		store.append(("CPU", "CPU info"))
		store.append(("ZB", "Motherboard info"))
		store.append(("MEM", "Memory info"))
		store.append(("HD", "HardDisk info"))
		store.append(("VGA", "Video info"))
		store.append(("MON", "Monitor info"))
		store.append(("CDR", "CD-ROM info"))
		store.append(("NET", "Net Card info"))
		store.append(("SOUND", "Sound card info"))
		store.append(("BAT", "Battery info"))
		store.append(("OTHER", "Other info"))

		treeView = gtk.TreeView(store)
                cell1 = gtk.CellRendererText()
                cell1.set_property( 'editable', False )
		cell1.set_property("foreground", "red")
		cell1.set_property("background-gdk", list_text_bk_color)
		cell1.set_property("size-points", 16)
		
		print "ttttttttttt",cell1.get_property("family")
                treeView.connect('cursor-changed', self.on_item_click_cb, store)
		treeView.set_headers_visible(False)

                column1 = gtk.TreeViewColumn("", cell1, text=1)
		#treeView.modify_text(gtk.STATE_NORMAL,list_text_color)

                treeView.append_column(column1)
                treeView.columns_autosize()
		treeView.set_size_request(150, 500)
		comf.set_bg_image(treeView,win_bg_image)
		return treeView

	def createView(self):
		vbox = gtk.VBox()
		#os.system("lshw -xml > /tmp/.hwinfo.xml")
		self.detail_buffer = gtk.TextBuffer()
                detailTextView = gtk.TextView(self.detail_buffer)
                detailTextView.set_editable(False)
		detailTextView.set_size_request(300,450)

                detailTextView.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(514, 5140, 5140))
                detailTextView.set_cursor_visible(False)
                detailTextView.set_wrap_mode (gtk.WRAP_CHAR);

		hbox = gtk.HBox()
		label1_text="".join("<span size=\"x-large\">Find</span> <span foreground=\"red\" size=\"xx-large\">%s</span> <span size=\"x-large\">hardware need to install drivers</span>"%(2))
		label1=gtk.Label("Find ")
		label1.set_markup(label1_text)
		label2=gtk.Label()
		label2.modify_text(gtk.STATE_NORMAL,list_text_color)
		label3=gtk.Label("hardware need to install drivers ")
		#fontdesc = pango.FontDescription("Purisa 11")
		fontdesc = pango.FontDescription("Purisa 11")
		fontdesc.set_weight(pango.WEIGHT_ULTRABOLD)
		label2.set_markup("<span foreground=\"red\" font=\"12.5\">%s</span>" % (2) )
		button3=gtk.Button("Detailed information")
		button3.set_relief(gtk.RELIEF_NONE)
		#button3.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(514, 5140, 514))
		#button3.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(5140, 5140, 514))
		#button3.modify_text(gtk.STATE_NORMAL, gtk.gdk.Color(50, 514000, 51400,6000))
		#button3.modify_base(gtk.STATE_NORMAL, gtk.gdk.Color(50, 5140, 514))
		#button3.modify_font(fontdesc)
		button3.get_child().set_markup("<span  foreground=\"blue\" size=\"x-large\">Detail</span>")
		#button3.set_size_request(100,40)
		button3.connect("clicked", self.view_detail_clicked)

		hbox.pack_start(label1, False, False,0)
		hbox.pack_start(button3, False, False,1)
		vbox.pack_start(hbox, False,False, 2)
		vbox.pack_start(detailTextView, False,False, 2)
		#vbox.set_size_request(200,200)
		self.root = self.load_xml(open(hwinfo_file).read())
		return vbox

	def view_detail_clicked(self,widget):
		self.hwlist.set_cursor(1)
		return
		self.norDevices = [[],[]]
		self.norDevices[0].append("Wireless")
		self.norDevices[1].append("Net device")
		self.norDevices[0].append("Video")
		self.norDevices[1].append("Video card")
		dm_detail.detailWin(self.norDevices)

	def on_item_click_cb(self, widget, model):
		#model = selection.get_mode()
		(path, col) = widget.get_cursor()
	        print model[path][0], path
	        print model[path][1]
		self.selected = model[path][0]
		self.read_xml(self.root)

	def print_node(self,node):
	    	'''打印结点基本信息'''
	    	print "=============================================="
	    	print "node.attrib:%s" % node.attrib
	    	print "node.attrib:%s" % node.items()
	    	#print "node.attrib:" , node
		#return
		#if node.attrib.has_key("id") > 0 :
		#	print "key=id,value=", node.get("id")
		#	print node.findall("capability")
    		#for key,value in node.items():
      		#	print "%s:%s" % (key, value)   
	#	if node.get("id") == "cpu":
		self.detail_buffer.delete(self.detail_buffer.get_start_iter(), self.detail_buffer.get_end_iter())
	    	for subnode in node.getchildren():
      			print "11 %s:%s" % (subnode.tag, subnode.text)  
			endIter = self.detail_buffer.get_end_iter()
			self.detail_buffer.insert(endIter, "\n%s : %s" % (subnode.tag, subnode.text))
			
	    #    print "node.attrib['age']:%s" % node.attrib['age']
	    #print "node.tag:%s" % node.tag
	    #print "node.text:%s" % node.text
	def load_xml(self,text):
	    	'''读xml文件'''
	    # 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件）   
	    # root = ElementTree.parse(r"D:/test.xml")
		return ElementTree.fromstring(text)
	    # 获取element的方法
	    # 1 通过getiterator
	def read_xml(self,root):
	    	lst_node = root.getiterator("node")
		strid=self.dictTag.get(self.selected)
		print "8888888888888888888=",strid
		if(strid == "driver"):
			self.read_drivers2(root)
		else:
	    		for node in lst_node:
				if(node.get("id") == strid):
	        			self.print_node(node)
	    # 2通过 getchildren
	    #lst_node_child = lst_node[0].getchildren()[0]
	    #print_node(lst_node_child)
	         
	    # 3 .find方法
	    	#node_find = root.find('list')
	    	#self.print_node(node_find)
	     
	    #4. findall方法
	    	#node_findall = root.findall("physid/node/product")
	    	#self.print_node(node_findall)
	def read_drivers(self, root):
		print 222222222222
		lst_node = root.getiterator("setting")
		self.detail_buffer.delete(self.detail_buffer.get_start_iter(), self.detail_buffer.get_end_iter())
		for node in lst_node:
			print "dddddddd node=",node,"node(id)=", node.get("id")
			if(node.get("id") == "driver"):
				endIter = self.detail_buffer.get_end_iter()
				self.detail_buffer.insert(endIter, "".join("\ndriver:%s"%(node.get("value"))))
	def read_drivers2(self, root):
		lst_node = root.getiterator("setting")
		self.detail_buffer.delete(self.detail_buffer.get_start_iter(), self.detail_buffer.get_end_iter())
		for node in lst_node:
			if(node.get("id") == "driver"):
				endIter = self.detail_buffer.get_end_iter()
				self.detail_buffer.insert(endIter, "".join("\ndriver:%s"%(node.get("value"))))

