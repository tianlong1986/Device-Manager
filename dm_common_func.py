import gtk,gobject

def set_bg_image(widget,filename):
	style = widget.get_style().copy()
        img_pixbuf = gtk.gdk.pixbuf_new_from_file(filename)
        img_pixmap = img_pixbuf.render_pixmap_and_mask()[0]
        for state in (gtk.STATE_NORMAL, gtk.STATE_ACTIVE, gtk.STATE_PRELIGHT,
        	gtk.STATE_SELECTED, gtk.STATE_INSENSITIVE):
                style.bg_pixmap[state] = img_pixmap
                widget.set_style(style)
def modify_window_fgcolor(widget, color):
	widget.modify_fg(gtk.STATE_NORMAL, color)
        widget.modify_fg(gtk.STATE_ACTIVE, color)
        widget.modify_fg(gtk.STATE_PRELIGHT, color)
        widget.modify_fg(gtk.STATE_SELECTED, color)

def modify_window_bgcolor(widget, color):
        widget.modify_bg(gtk.STATE_NORMAL, color)
        widget.modify_bg(gtk.STATE_ACTIVE, color)
        widget.modify_bg(gtk.STATE_PRELIGHT, color)
        widget.modify_bg(gtk.STATE_SELECTED, color)
        #widget.set_opacity(0.9)
        #widget.set_decorated(True)

