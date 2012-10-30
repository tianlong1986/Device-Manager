# -*- coding: utf-8 -*-
import gtk, gobject
from xml.etree import ElementTree

list_text_color = gtk.gdk.Color(60000, 5000, 30003, 60000)
class dm_main(gtk.HBox):
	def __init__(self):
		super(dm_main, self).__init__()
		hwlist = self.createList()
		infoview = self.createView()
		other = self.createOther()
		self.pack_start(hwlist, False,False,5)
		self.pack_start(infoview, False,False,50)
		self.pack_start(other, False,False,5)
		#self.set_size_request(100, 150)
	
		self.dictTag = {'ALL':'all','CPU':'cpu', 'MEM':'memory'}
	def createList(self):
	        store = gtk.ListStore(gobject.TYPE_STRING,
                                     gobject.TYPE_STRING)
                #for item in self.alltype:
                store.append(("ALL","All View"))
		store.append(("ZB", "zhuban info"))
		store.append(("CPU", "CPU info"))
		store.append(("MEM", "Memory info"))

		treeView = gtk.TreeView(store)
                cell1 = gtk.CellRendererText()
                cell1.set_property( 'editable', False )
		#selection = treeView.get_selection()
                treeView.connect('cursor-changed', self.on_item_click_cb, store)
		treeView.set_headers_visible(False)

                column1 = gtk.TreeViewColumn("", cell1, text=1)
		treeView.modify_text(gtk.STATE_NORMAL,list_text_color)

                treeView.append_column(column1)
                treeView.columns_autosize()
		treeView.set_size_request(100, 300)
		return treeView

	def createView(self):
		vbox = gtk.VBox()
		self.detail_buffer = gtk.TextBuffer()
                detailTextView = gtk.TextView(self.detail_buffer)
                detailTextView.set_editable(False)
		detailTextView.set_size_request(200,300)

                detailTextView.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(514, 5140, 5140))
                detailTextView.set_cursor_visible(False)
                detailTextView.set_wrap_mode (gtk.WRAP_CHAR);

		label=gtk.Label("VIEW")
		vbox.pack_start(label, False,False, 2)
		vbox.pack_start(detailTextView, False,False, 2)
		vbox.set_size_request(200,200)
		return vbox
	def createOther(self):
		label = gtk.Label("Temperature ....")
		return label

	def on_item_click_cb(self, widget, model):
		#model = selection.get_mode()
		(path, col) = widget.get_cursor()
	        print model[path][0], path
	        print model[path][1]
		self.selected = model[path][0]
		#if model[path][0] == "CPU":
		self.read_xml(open("hwinfo.xml").read())

	def print_node(self,node):
	    	'''打印结点基本信息'''
	    	print "=============================================="
	    	#print "node.attrib:%s" % node.attrib
	    	#print "node.attrib:%s" % node.items()
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
	def read_xml(self,text):
	    	'''读xml文件'''
	    # 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件）   
	    # root = ElementTree.parse(r"D:/test.xml")
	    	root = ElementTree.fromstring(text)
		eitor = root.getchildren()
    	#	for e in eitor:
	 #       	self.print_node(e)  
	    # 获取element的方法
	    # 1 通过getiterator
	    	lst_node = root.getiterator("node")
		strid=self.dictTag.get(self.selected)
		print "8888888888888888888=",strid
	    	for node in lst_node:
			#eitor = node.getchildren()
    			#for e in eitor:
	        	#	self.print_node(e)  
				#print node.findall("capability").items()	    
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
		
