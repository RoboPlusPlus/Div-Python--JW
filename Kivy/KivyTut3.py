from kivy.app import App
import kivy
"""
Denne printer "text"-property fra "Label"-parent i "SimpleKivy.kv" - fil.

"""


kivy.require("1.8.0") #versjonskontroll. Trenger minimum kivy  v "x.y.z"

from kivy.uix.label import Label # En Label kan også fungere som en knapp eller lignende


class SimpleKivy(App):
    def build(self):
        return Label()

if __name__ == "__main__":
    SimpleKivy().run()


