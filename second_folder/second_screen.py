from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


# Load the KV file associated with FirstScreen
Builder.load_file('second_folder/second_screen.kv')

class SecondScreen(Screen):
    def switch_to_first_screen(self):
        self.manager.current = 'first'