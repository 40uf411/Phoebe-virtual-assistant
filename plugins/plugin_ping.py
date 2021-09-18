from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
import datetime
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk 

from plugins.plugin import Plugin

from ping3 import ping, verbose_ping

class PingPlugin(Plugin):
    def execute(self, command):
        tokens = command.split()
        if len(tokens) < 2: # local time
            return {"msg":"Sorry can't ping 'Nothing'", "content":None}
        
        temp = "./templates/pingBox.glade"
        self.dist = tokens[1]
        self.builder = gtk.Builder()
        self.builder.add_from_file(temp)
        
        self.box = self.builder.get_object("pingBox")
        self.distLb = self.builder.get_object("dist")
        self.timeLb = self.builder.get_object("time")
        
        self.distLb.set_text("Pinging: %s" % (self.dist))
        self.timeLb.set_text("Time: %.2f Seconds" % (ping(self.dist)))
        
        return {"msg":"Pong!", "content":self.box}