from plugins.plugin_time import TimePlugin
from plugins.plugin_ping import PingPlugin
from plugins.plugin_calendar import CalendarPlugin

class Callbacks:
    plugins = {
        "time": TimePlugin,
        "ping": PingPlugin,
        "calendar": CalendarPlugin
    }