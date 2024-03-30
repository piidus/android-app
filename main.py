from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from first_folder import FirstScreen
from second_folder import SecondScreen

class LoginScreen(Screen):
    def go_to_first(self):
        self.manager.current = 'first'

class WindowManager(ScreenManager):
    pass


class LogInApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Olive'
        self.screen_manager = Builder.load_file('main.kv')
        return self.screen_manager
    
    

if __name__ == '__main__':
    LogInApp().run()

