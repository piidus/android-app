
"""
Script for run for final
"""

# import importlib
import os

# from kivy import Config
# from kivymd.theming import ThemeManager
# from PIL import ImageGrab

# # TODO: You may know an easier way to get the size of a computer display.
# Config.set("graphics", "height", 900)
# Config.set("graphics", "width", 300)

# from kivy.core.window import Window

# Place the application window on the right side of the computer screen.
# Window.top = 30
# Window.right= 10 #=  Window.width - 650
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager


class MYProject(MDApp):
    KV_DIRS = [os.path.join(os.getcwd(), "View")]
    

    def build_app(self) -> MDScreenManager:
        """
        In this method, you don't need to change anything other than the
        application theme.
        """

        import View.screens
        

        self.manager_screens = MDScreenManager()
        

        screens = View.screens.screens

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

        return self.manager_screens

   
if __name__ == "__main__":
    MYProject().run()
