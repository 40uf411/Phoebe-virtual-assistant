import sys

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import GLib, Gtk

DELAY = 5_000

class Notification:
    def __init__(self, msg) -> None:
        builder = Gtk.Builder()
        builder.add_from_file("./templates/app-notification.glade")
        notification_message = builder.get_object("notification-message")
        
        builder.connect_signals(
            {
                "close-notification": self.close,
            }
        )
        self.notification_revealer = builder.get_object("notification-revealer")
        self.notification_revealer.show_all()

