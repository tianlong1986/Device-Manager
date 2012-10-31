import gtk,gobject
class detailWin(gtk.Window):
        def __init__(self,lstDri):
                super(detailWin,self).__init__()
                scrollWin = self.create_scroll_window(lstDri)
		button = gtk.Button(" Close ")
		button.connect("clicked", self.close_button_clicked)
		vbox = gtk.VBox()
		vbox.pack_start(scrollWin, False, False,2)
		hbox = gtk.HBox()
		hbox.pack_end(button, False, False,2)
		vbox.pack_start(hbox, False, False,2)
		self.add(vbox)
		self.set_size_request(300,350)
		self.set_position(gtk.WIN_POS_CENTER)
		self.show_all()
	def create_scroll_window(self,lstDri):
		scrollWin=gtk.ScrolledWindow()
                scrollWin.set_size_request(280,300)
                scrollWin.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		store = gtk.ListStore(gobject.TYPE_INT,
                                         gobject.TYPE_STRING,
					 gobject.TYPE_STRING )
		count = len(lstDri[0])
		i = 0
		while i < count:
			store.append((i, lstDri[0][i], lstDri[1][i]))
			i = i + 1
	

		treeView = gtk.TreeView(store)
                cell1 = gtk.CellRendererText()
                cell1.set_property( 'editable', False )
                cell2 = gtk.CellRendererText()
                cell2.set_property( 'editable', False )
		column1 = gtk.TreeViewColumn("Hardware", cell1, text=1)
                column2 = gtk.TreeViewColumn("Device Type", cell2, text=2 )

                treeView.append_column(column1)
                treeView.append_column(column2)
                treeView.columns_autosize()
                scrollWin.add(treeView)
		return scrollWin
	def close_button_clicked(self, widget):
		self.destroy()
