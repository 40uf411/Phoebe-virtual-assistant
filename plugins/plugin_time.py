import datetime
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk 

from plugins.plugin import Plugin

class TimePlugin(Plugin):
    def execute(self, command):
        box = gtk.Box(spacing=10, orientation="vertical")
        # Clock
        now = datetime.datetime.now()
        clockLabel = gtk.Label(
            label=now.strftime("%H : %M")
        )
        clockLabelContext = clockLabel.get_style_context()
        clockLabelContext.add_class("timePlugin_clock")
        box.add(clockLabel)
        # Timezone
        t = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
        tLabel = gtk.Label(
            label=now.strftime("Timezone : {}".format(t))
        )
        box.add(tLabel)
        return {"msg":"Here is the time:", "content":box}