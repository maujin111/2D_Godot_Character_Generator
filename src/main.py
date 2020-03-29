import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import sys
import os



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

    def on_generar_clicked(self,generar):
        field_file_name  =   builder.get_object("file_name")
        file_name = field_file_name.get_text()+".gd"
        file_chooser = builder.get_object("path")
        file_path = file_chooser.get_current_folder()
        try:
            create_file(file_path,file_name)
            msg = builder.get_object("success")
            msg.run()
        except:
            msg = builder.get_object("error")
            msg.run()
        
        pass


    def on_succes_acept_clicked(self,success):
        msg = builder.get_object("success")
        msg.hide()

    def on_error_acept_clicked(self,error):
        msg = builder.get_object("error")
        msg.hide()


def create_file(file_path,file_name):
    gd_file = open(file_path+"/"+file_name,"w" )
    gd_file.write("Prueba")
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