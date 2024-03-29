from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from first_folder import FirstScreen
from second_folder import SecondScreen



class LogInApp(MDApp):
    def build(self):
        self.screen_manager = Builder.load_file(filename='main.kv')
        return self.screen_manager

if __name__ == '__main__':
    LogInApp().run()

