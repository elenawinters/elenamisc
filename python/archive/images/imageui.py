from tkinter import BOTH, BOTTOM, END, HORIZONTAL, LEFT, Menu, NSEW, RIGHT, StringVar, Text, TOP, X, Y
from tkinter.ttk import Entry, Frame, Label, PanedWindow, Progressbar, Scrollbar, Style, Treeview


class ImageUI(Frame):
    def __init__(self):
        super().__init__()
        self.create_widgets()
        self.setup_variables()
        self.setup_style()

    def create_widgets(self):
        # self.menubar = Menu()
        # self.menubar.add_command(label="Open", command=self._askopen)
        pass

    def setup_variables(self):
        self.bg_color = '#2C2F33'
        self.fg_color = '#23272A'
        self.greyple = '#99AAB5'

    def setup_style(self):
        style = Style()
        style.theme_create('elenabot', settings={
            "TNotebook": {
                "configure": {
                    "background": self.fg_color  # Your margin color
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "background": self.fg_color,  # tab color when not selected
                    "padding": [10, 2],  # [space between text and horizontal tab-button border, space between text and vertical tab_button border]
                    "focuscolor": self.bg_color,  # match focus color so the lines stop showing Madge
                    "font": "white"
                },
                "map": {
                    "foreground": [("selected", "white"), ("!disabled", self.greyple)],
                    "background": [("selected", self.bg_color)]  # Tab color when selected
                }
            }
        })
        style.theme_use('elenabot')
        print('this is here now')
