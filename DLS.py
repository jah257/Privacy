from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import NumericProperty

var_width = 6
var_height = 6


class DummyLocation(App):

    def build(self):
        layout = GridLayout(cols=var_width, row_default_height=40, padding=40 )

        area = var_height * var_width
        count = 0

        while count<area:

            layout.add_widget(Button(text=' ')) # size_hint_x=None, width=100))

            count+=1

        return layout

class test(GridLayout):
    Num=NumericProperty(10)
    str0 = '[color=224422][size=64]Number: '
    str1 = '.[/color][size]'
    NumSel = 11*[None]
    for i in range(11):
        NumSel[i]=str0 + str(i) + str1

class testApp(App):
    def build(self):
        return test()



#testApp().run()
DummyLocation().run()