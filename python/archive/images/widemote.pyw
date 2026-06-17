import imageui


class Widemote(imageui.ImageUI):
    def init(self):
        pass

    def create_widgets(self):
        super().create_widgets()


if __name__ == "__main__":
    app = Widemote()
    app.mainloop()
