from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


# Load the KV file associated with FirstScreen
Builder.load_file('first_folder/first_screen.kv')

class FirstScreen(Screen):
    def switch_to_second_screen(self):
        self.manager.current = 'second'