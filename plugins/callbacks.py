from plugins.plugin_time import TimePlugin
from plugins.plugin_ping import PingPlugin

class Callbacks:
    plugins = {
        "time": TimePlugin,
        "ping": PingPlugin
    }