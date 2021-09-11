import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk 
from msg import Msg


class Main(gtk.Window):
    def __init__(self) -> None:
        temp = "./templates/main.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(temp)
        
        button = self.builder.get_object("run")
        button.connect("clicked", self.prnt)
        
        
        menubutton = self.builder.get_object("more")
        
        menu = gtk.Menu()
        menubutton.set_popup(menu)

        for count in range(1, 6):
            menuitem = gtk.MenuItem(label="Item %i" % (count))
            menuitem.connect("activate", self.on_menuitem_activated)
            menu.append(menuitem)
        menu.show_all()

        histo = self.builder.get_object("histo")
        
        for i in range(3):
            e = Msg()
            histo.add(e.content)
        histo.show_all()
        
        
        main = self.builder.get_object("main")
        main.connect("delete-event", gtk.main_quit)
        main.show()
        
    def on_menuitem_activated(self, menuitem):
        print("%s Activated" % (menuitem.get_label()))
        
        
    def prnt(self, widget):
        print(widget)
if __name__ == "__main__":
    main = Main()
    gtk.main()