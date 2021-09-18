from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
import datetime
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk 

from plugins.plugin import Plugin

class TimePlugin(Plugin):
    def execute(self, command):
        tokens = command.split()
        
        if len(tokens) < 2: # local time
            now = datetime.datetime.now()
            t = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
            m = 'based on your PCs local timezone:'
        else:
            data = self.tzFromCity(' '.join(tokens[1:]))
            if data == False:
                return {"msg":"Sorry, I could not find a city with the name '%s'"%(' '.join(tokens[1:])), "content":None}
            now = data['datetime']
            t = data['timezone']
            m = 'in %s.' % (' '.join(tokens[1:]))
        
        box = gtk.Box(spacing=10, orientation="vertical")
        boxContext = box.get_style_context()
        theme = 'light' if int(now.strftime("%H")) < 20 else 'dark'
        boxContext.add_class("timePlugin_clock_%s" % (theme))
        # Clock
        clockLabel = gtk.Label(
            label=now.strftime("%H : %M")
        )
        clockLabelContext = clockLabel.get_style_context()
        clockLabelContext.add_class("timePlugin_clockLbl")
        box.add(clockLabel)
        # Timezone
        tLabel = gtk.Label(
            label=now.strftime("Timezone : {}".format(t))
        )
        box.add(tLabel)
        return {"msg":"Here is the time %s"%(m), "content":box}
    
    def tzFromCity(self, city):
        # initialize Nominatim API
        geolocator = Nominatim(user_agent="geoapiExercises")
        # getting Latitude and Longitud
        location = geolocator.geocode(city)
        if location == None:
            return False
        # Time from Tz
        tz = TimezoneFinder().timezone_at(lng=location.longitude, lat=location.latitude)
        timeByTz = pytz.timezone(tz)
        
        return {
            'location' : location,
            'latitude' : location.latitude,
            'longitude' : location.longitude,
            'timezone' : tz,
            'datetime' : datetime.datetime.now(timeByTz)
        }