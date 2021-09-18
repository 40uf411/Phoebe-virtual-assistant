from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
import datetime
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk 

from plugins.plugin import Plugin

from ping3 import ping, verbose_ping

class CalendarPlugin(Plugin):
    def execute(self, command):
        temp = "./templates/calendar.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(temp)
        
        self.box = self.builder.get_object("calendarPlugin_box")
        
        # self.box = gtk.Box()
        # self.calendar = gtk.Calendar()
        # self.calendar.set_detail_height_rows(1)
        # self.calendar.set_property("show-details",True)
        # self.box.add(self.calendar)
        # boxContext = self.box.get_style_context()
        # boxContext.add_class("calendarPlugin_box")
        self.box.show_all()
        
        return {"msg":"Here is your calendar.", "content":self.box}