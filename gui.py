import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk 
from gi.repository import Gdk as gdk 
from gi.repository import GLib 
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
        
        self.notification_revealer = self.builder.get_object("notification-revealer")
        self.notification_message = self.builder.get_object("notification-message")
        self.builder.connect_signals(
            {
                "close-notification": self.close,
            }
        )
        self.notification_revealer.show_all()
        
        self.reset = self.builder.get_object("reset")
        self.button = self.builder.get_object("run")
        self.cmd = self.builder.get_object("cmd")
        self.run = self.builder.get_object("run")
        self.vcmd = self.builder.get_object("voiceCmd")
        
        
        
        self.reset.connect("clicked", self.on_question_clicked)
        self.cmd.connect("activate", self.execCmd)
        self.button.connect("clicked", self.execCmd)
        
        self.main = self.builder.get_object("main")
        self.main.connect("delete-event", gtk.main_quit)
        self.main.show()
        
    def on_menuitem_activated(self, menuitem):
        print("%s Activated" % (menuitem.get_label()))
        
    def execCmd(self, widget, key=None):
        msg = self.cmd.get_text()
        if msg != "":
            self.runCmd(msg)

    def runCmd(self, msg):
        e = Msg(msg, self.execCmd, self)
        self.histo.add(e.row)
        self.cmd.set_text('')
        result = self.dspr(msg)
        e = SysMsg(**result)
        self.histo.add(e.row)

    def showNotification(self, msg):
        self.notification_message.set_text(msg)
        self.notification_revealer.set_reveal_child(True)
        self.notification_revealer.auto_hide_id = GLib.timeout_add(
            5_000, self.closeNotification, self.notification_revealer
        )


    def closeNotification(self, w=None):
        self.notification_revealer.set_reveal_child(False)
        GLib.source_remove(self.notification_revealer.auto_hide_id)
        del self.notification_revealer.auto_hide_id


    def on_question_clicked(self, widget):
        dialog = gtk.MessageDialog(
            flags=0,
            message_type=gtk.MessageType.WARNING,
            buttons=gtk.ButtonsType.YES_NO,
            text="This is an ERROR MessageDialog",
        )
        dialog.format_secondary_text(
            "And this is the secondary text that explains things."
        )
        dialog.run()
        print("ERROR dialog closed")

        dialog.destroy()


        #dialog.destroy()
if __name__ == "__main__":
    styleProvider = gtk.CssProvider()
    styleProvider.load_from_path('./css/style.css')
    gtk.StyleContext.add_provider_for_screen(
        gdk.Screen.get_default(), styleProvider, 
        gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    main = Main()
    gtk.main()