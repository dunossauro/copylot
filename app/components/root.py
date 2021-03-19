from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string('''
<Root>:
    MDLabel:
        id: first_label
        text: 'Copylot'
        halign: 'center'
        font_style: 'H5'
''')


class Root(MDBoxLayout):
    ...
