from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from gpt import chatgpt
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField


class CustomMDTextField(MDTextField):
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode == 40 and '\n' in self.text:
            self.insert_text('\n')  # Insert the newline character as is
        else:
            super().keyboard_on_key_down(window, keycode, text, modifiers)


class Container(GridLayout):
    text_input = ObjectProperty()
    label_widget = ObjectProperty()

    def change_text(self):
        self.label_widget.text = chatgpt(self.text_input.text)


class BoxApp(MDApp):
    theme_cls = ThemeManager()
    title = "ChatGPT App"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        return Container()


if __name__ == "__main__":
    BoxApp().run()
