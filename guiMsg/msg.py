from datetime import datetime
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk as gtk 
from gi.repository import Notify, GLib
from gi.repository import Gdk as gdk 

from guiMsg.notification import Notification

class Msg(gtk.ListBoxRow):
    def __init__(self, msg, run, mainWindow):
        temp = "./templates/msg.glade"
        self.clipboard = gtk.Clipboard.get(gdk.SELECTION_CLIPBOARD)
        self.parent = mainWindow
        self.msg = msg
        self.runFnc = run
        self.builder = gtk.Builder()
        self.builder.add_from_file(temp)
        self.revealStat = False
        
        #self.content = self.builder.get_object("SentItemListBox")
        self.row = self.builder.get_object("SentItemListBoxRow")
        self.revealBtn = self.builder.get_object("MsgButton")
        self.revealBtnIcn = self.builder.get_object("MsgButtonIcon")
        self.revealer = self.builder.get_object("MsgRevealer")
        self.msgContent = self.builder.get_object("MsgContent")
        self.copy = self.builder.get_object("copy")
        self.runAgain = self.builder.get_object("runAgain")
        self.time = self.builder.get_object("time")
        self.date = self.builder.get_object("date")
        
        now = datetime.now()
        self.time.set_text(now.strftime("%H:%M:%S"))
        today = datetime.today()
        self.date.set_text(today.strftime("%d/%m/%Y"))
        self.msgContent.set_text(msg)
        self.revealBtn.connect('clicked', self.reveal)
        self.runAgain.connect('clicked', self.runCmd)
        self.copy.connect('clicked', self.copy_text)
        
        self.row.show()

    def runCmd(self, w):
        self.parent.showNotification("Running command '%s' from your history" %(self.msg))
        self.parent.runCmd(self.msg)

    def copy_text(self, widget):
        def callback():
            pass
        self.clipboard.set_text(self.msg, -1)
        
        Notify.init("Command '%s' copied to clipboard" %(self.msg))
        info = Notify.Notification.new('Phoebe AI', "Command '%s' copied to clipboard" %(self.msg), 'dialog-information')
        info.set_timeout(Notify.EXPIRES_DEFAULT)
        info.set_urgency(Notify.Urgency.LOW)
        info.show()
        self.parent.showNotification("Command '%s' copied to clipboard" %(self.msg))

    def reveal(self, item):
        if not self.revealStat:
            self.revealer.show()
            self.revealer.set_reveal_child(True)
            self.revealBtnIcn.set_from_icon_name("window-close-symbolic", gtk.IconSize.BUTTON)
            self.revealStat = True
        else:
            #self.revealer.close()
            self.revealer.set_reveal_child(False)
            self.revealBtnIcn.set_from_icon_name("open-menu-symbolic", gtk.IconSize.BUTTON)
            self.revealStat = False
if __name__ == "__main__":
    main = Msg()
    gtk.main()