from kivymd.app import MDApp
import kivy
from kivy.lang import Builder
from kivy.core.text import LabelBase

import settings

# main
from screens.register.register import RegisterScreen
from screens.login.login import LoginScreen
from screens.failed_test.test import FailedTestScreen
from screens.success_test.test import SuccessTestScreen

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
        Builder.load_file('screens/login/login.kv')
        Builder.load_file('screens/failed_test/test.kv')
        Builder.load_file('screens/success_test/test.kv')
        #Builder.load_file('screens/faq/faq.kv')
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.sm = ScreenManager()
        self.sm = ScreenManager(transition=NoTransition())

        self.sm.add_widget(RegisterScreen(name='register_screen'))
        self.sm.add_widget(LoginScreen(name='login_screen'))
        self.sm.add_widget(FailedTestScreen(name='failed_test_screen'))
        self.sm.add_widget(SuccessTestScreen(name='success_test_screen'))

        return self.sm

if __name__ == '__main__':
    LabelBase.register(name='OpenSans',
        fn_regular='fonts/OpenSans/OpenSans-Regular.ttf',
        fn_italic='fonts/OpenSans/OpenSans-Italic.ttf',
        fn_bold='fonts/OpenSans/OpenSans-Bold.ttf',
        fn_bolditalic='fonts/OpenSans/OpenSans-BoldItalic.ttf',
    )
    App().run()
