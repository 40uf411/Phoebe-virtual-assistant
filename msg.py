import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk 

class Msg(gtk.ListBoxRow):
    def __init__(self):
        temp = "./templates/msg.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(temp)
        self.revealStat = False
        
        self.content = self.builder.get_object("SentItemListBox")
        self.revealBtn = self.builder.get_object("MsgButton")
        self.revealBtnIcn = self.builder.get_object("MsgButtonIcon")
        self.revealer = self.builder.get_object("MsgRevealer")
        
        self.revealBtn.connect('clicked', self.reveal)
        
        self.content.show()
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