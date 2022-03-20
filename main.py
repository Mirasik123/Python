# библиотеки
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import mainthread
from kivy.core.clipboard import Clipboard as Cb
from kivy.uix.label import Label
import threading
import socket


# main class
class Club21(App):

	def click(self, instance):
		self.label.text = "Ера гей!"
	def click2(self, instance):
		self.label.text = "Ера не гей!"

	# постройка выджетов на окне
	def build(self):

		but_together = BoxLayout()
		grid = GridLayout(cols=1)

		# виджеты
		my_but = Button(text="Нажмешь \nГей!", font_size=30, background_color="cyan", on_press=self.click) 
		think_of_name = Button(text="Нажмешь \nне гей!", font_size=30, background_color="cyan", on_press=self.click2)
		self.label = Label(text="Привет", font_size=30)

		but_together.add_widget(my_but)
		but_together.add_widget(think_of_name)

		grid.add_widget(but_together)
		grid.add_widget(self.label)

		# возвращяем виджеты
		return grid
# запускаем приложение
if __name__ == '__main__':
	Club21().run()