from datetime import datetime
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk 

class SysMsg(gtk.ListBoxRow):
    def __init__(self, msg, content=None):
        temp = "./templates/sysMsg.glade"
        self.msg = msg
        self.content = content
        self.builder = gtk.Builder()
        self.builder.add_from_file(temp)
        
        #self.content = self.builder.get_object("SentItemListBox")
        self.row = self.builder.get_object("PhoebeRow")
        self.msgContent = self.builder.get_object("MsgContent")
        self.phoebeContent = self.builder.get_object("PhoebeContent")
        self.time = self.builder.get_object("time")
        self.date = self.builder.get_object("date")
        
        now = datetime.now()
        self.time.set_text(now.strftime("%H:%M:%S"))
        today = datetime.today()
        self.date.set_text(today.strftime("%d/%m/%Y"))
        self.msgContent.set_text(msg)
        if content != None:
            self.phoebeContent.add(content)
        self.phoebeContent.show_all()
        self.row.show()

if __name__ == "__main__":
    main = Msg()
    gtk.main()