from kivy.app import App
from ui_pogovorki import UIPogovorki

class MainUI(App):

    def build(self):
        return UIPogovorki()

if __name__ == '__main__':
    MainUI().run()
