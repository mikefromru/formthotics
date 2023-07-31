from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.label import MDLabel


from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.button import MDRaisedButton

# class MikeyButton(ButtonBehavior, MDRaisedButton):
class MikeyButton(MDRaisedButton):

    def set_radius(self, *args) -> None:
        if self.rounded_button:
            self._radius = 20

class RegisterScreen(Screen):

    def register(self):
        MDSnackbar(
            MDLabel(
                text="Server is not working now",
                # theme_text_color="Custom",
                # text_color="#393231",
            ),
        ).open()
