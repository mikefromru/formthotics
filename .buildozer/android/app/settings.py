from kivy.core.window import Window
from kivy.utils import platform

if platform != 'android':
    Window.size = (350, 750)
    Window.top = 70
    Window.right = 70

