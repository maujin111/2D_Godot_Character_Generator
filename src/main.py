import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import sys



builder = Gtk.Builder()
builder.add_from_file("src/ui/ui.glade")
win = builder.get_object("window1")


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    
    def on_about_clicked(self,about):

        about = builder.get_object("about_window")
        about.run()
        about.hide()

        pass

 


def generar():
 
        pass




def main(argv):
    
    def gtk_style():
        
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path("src/ui/gtk.css")

        Gtk.StyleContext.add_provider_for_screen( Gdk.Screen.get_default(), style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    
    
    builder.connect_signals(Handler())
    gtk_style()
    
    
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main(sys.argv)