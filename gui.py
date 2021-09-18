import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk 
from gi.repository import Gdk as gdk 
from guiMsg.msg import Msg
from guiMsg.sysMsg import SysMsg

from dispatcher import Dispatcher

class Main(gtk.Window):
    dspr = Dispatcher()
    def __init__(self) -> None:
        temp = "./templates/main.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(temp)
                
        menubutton = self.builder.get_object("more")
        menu = gtk.Menu()
        menubutton.set_popup(menu)
        for count in range(1, 6):
            menuitem = gtk.MenuItem(label="Item %i" % (count))
            menuitem.connect("activate", self.on_menuitem_activated)
            menu.append(menuitem)
        menu.show_all()
        
        
        self.histo = self.builder.get_object("histo")
        self.histo.show_all()
        
                
        self.button = self.builder.get_object("run")
        self.cmd = self.builder.get_object("cmd")
        self.run = self.builder.get_object("run")
        self.vcmd = self.builder.get_object("voiceCmd")
        
        
        
        self.cmd.connect("activate", self.execCmd)
        self.button.connect("clicked", self.execCmd)
        
        main = self.builder.get_object("main")
        main.connect("delete-event", gtk.main_quit)
        main.show()
        
    def on_menuitem_activated(self, menuitem):
        print("%s Activated" % (menuitem.get_label()))
        
        
    def execCmd(self, widget, key=None):
        msg = self.cmd.get_text()
        if msg != "":
            e = Msg(msg, self.execCmd)
            self.histo.add(e.row)
            self.cmd.set_text('')
            result = self.dspr(msg)
            e = SysMsg(**result)
            self.histo.add(e.row)
        
if __name__ == "__main__":
    styleProvider = gtk.CssProvider()
    styleProvider.load_from_path('./css/style.css')
    gtk.StyleContext.add_provider_for_screen(
        gdk.Screen.get_default(), styleProvider, 
        gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    main = Main()
    gtk.main()