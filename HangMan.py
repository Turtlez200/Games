import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import random

class GridWindow(GridLayout, Screen):

    index = []
    lives = 5

    words = ["flower", "leaves", "painting", "window", "chaos", "mistake", "impossible",
             "break", "madden", "welcome", "mailbox", "amazed", "zebra", "driveway", "classroom",
             "racecar", "bottom", "misery", "lampost", "postcard", "guitar", "violin",
             "highway", "chemistry", "sandwich", "square", "bail", "mold", "justice", "janitor", "pizza"]

    word = "fuck ur mom"
    under = word
    emp = ""
    for x in range(len(under)):
        under = under[0:x] + "_" + under[x + 1:]
    list = list(under)
    for x in range(1, len(list) + len(list) - 1, 2):
        list.insert(x, " ")
    emp = (emp.join(list))
    win = False
    play_ag = False
    string = "Screen Shot 2021-10-19 at 7."

    def __init__(self, **kwargs):
        super(GridWindow, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 1

        self.ins = GridLayout()
        self.ins.cols = 2

        self.life = Image(source=f"{self.string}56.36 AM.png", allow_stretch=True)
        self.chosen = TextInput(multiline=False, font_size=40)
        self.ins.add_widget(self.life)
        self.ins.add_widget(self.chosen)

        self.inside.add_widget(self.ins)

        self.but = Button(text="Submit", font_size=40, background_color =(0, 0, 1, 1))
        self.but.bind(on_press=self.btn)
        self.inside.add_widget(self.but)

        self.add_widget(self.inside)

        self.undersc = (Label(text=self.emp, font_size=70, opacity =(0.5)))
        self.add_widget(self.undersc)

        self.window = self
    def btn(self, instance):
        if self.play_ag:
            pass
        self.win = False
        if self.chosen.text in self.word:
            self.win = True
            for x in range(len(self.word)):
                if self.word[x] == self.chosen.text:
                    self.index.append(x)
        for j in self.index:
            self.emp = self.emp[0:j*2] + self.word[j] + self.emp[j*2 + 1:]
        self.undersc.text = self.emp
        self.index.clear()
        if not self.win:
            self.lives -= 1
            if self.lives == 4:
                self.life.source = f"{self.string}57.24 AM.png"
            elif self.lives == 3:
                self.life.source = f'Screen Shot 2021-10-19 at 8.07.36 AM.png'
            elif self.lives == 2:
                self.life.source = f'{self.string}58.14 AM.png'
            elif self.lives == 1:
                self.life.source = f'{self.string}58.57 AM.png'
            elif self.lives == 0:
                self.life.source = f'{self.string}59.33 AM.png'
                self.undersc.font_size = 40
                self.undersc.text = f"YOU LOSE! The word was: {self.word}"
        if "_" not in self.emp:
            self.undersc.text = "YOU WIN!!"
            self.but.text = "Play Again?"
            self.play_ag = True
        if self.chosen.text == self.word:
            self.undersc.text = "YOU WIN!!"
            self.but.text = "Play Again?"
            self.play_ag = True
        self.chosen.text = ""



class HangMan(App):
    def build(self):
        return GridWindow()


if __name__ == "__main__":
    HangMan().run()
