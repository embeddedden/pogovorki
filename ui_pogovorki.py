from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from pogovorki import Pogovorka

class UIPogovorki(BoxLayout):

    def __init__(self, **kwargs):
        super(UIPogovorki, self).__init__(**kwargs)
        self.pogovorka_instance = Pogovorka()
        self.orientation = 'vertical'
        self.buttons_layout = BoxLayout(orientation='horizontal')
        self.btn_next = Button(text='Следующая')
        self.btn_next.bind(on_release=self.next_pogovorka)
        self.btn_prev = Button(text='Предыдущая')
        self.btn_prev.bind(on_release=self.prev_pogovorka)
        self.btn_rand = Button(text='Случайная')
        self.btn_rand.bind(on_release=self.random_pogovorka)
        self.buttons_layout.add_widget(self.btn_prev)
        self.buttons_layout.add_widget(self.btn_rand)
        self.buttons_layout.add_widget(self.btn_next)
        self.pogovorka = Label(text=self.pogovorka_instance.read_pogovorka())
        self.add_widget(self.pogovorka)
        self.add_widget(self.buttons_layout)

    def next_pogovorka(self, obj):

        pogovorka_line = self.pogovorka_instance.read_next_pogovorka()
        if pogovorka_line != 'none':
            self.pogovorka.text = pogovorka_line
        else:
            self.pogovorka.text = 'Поговорки закончились'

    def prev_pogovorka(self, obj):

        pogovorka_line = self.pogovorka_instance.read_prev_pogovorka()
        if pogovorka_line != 'none':
            self.pogovorka.text = pogovorka_line
        else:
            self.pogovorka.text = 'Поговорки закончились'

    def random_pogovorka(self, obj):

        pogovorka_line = self.pogovorka_instance.read_random_pogovorka()
        if pogovorka_line != 'none':
            self.pogovorka.text = pogovorka_line
        else:
            self.pogovorka.text = 'Поговорки закончились'
