from kivymd.app import MDApp

from app.components import Root


class Copylot(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.accent_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        return Root()
