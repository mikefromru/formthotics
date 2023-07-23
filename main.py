from kivymd.app import MDApp
import kivy
from kivy.lang import Builder
from kivy.core.text import LabelBase

import settings

# main
from screens.register.register import RegisterScreen
from screens.login.login import LoginScreen

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import (
    NoTransition,
    SlideTransition,
    CardTransition,
    SwapTransition,
    FadeTransition,
    WipeTransition,
    FallOutTransition,
    RiseInTransition
)

class App(MDApp):

    def build(self):
        # Builder.load_file('main.kv')
        Builder.load_file('screens/register/register.kv')
        # Builder.load_file('screens/login/login.kv')
        #Builder.load_file('screens/levels/levels.kv')
        #Builder.load_file('screens/faq/faq.kv')
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"
        self.sm = ScreenManager()
        self.sm = ScreenManager(transition=FadeTransition(duration=.1))

        self.sm.add_widget(RegisterScreen(name='register_screen'))
        # self.sm.add_widget(LoginScreen(name='login_screen'))

        return self.sm

if __name__ == '__main__':
    LabelBase.register(name='OpenSans',
        fn_regular='fonts/OpenSans/OpenSans-Regular.ttf',
        fn_italic='fonts/OpenSans/OpenSans-Italic.ttf',
        fn_bold='fonts/OpenSans/OpenSans-Bold.ttf',
        fn_bolditalic='fonts/OpenSans/OpenSans-BoldItalic.ttf',
    )
    App().run()
