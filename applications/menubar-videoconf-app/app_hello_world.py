# -*- coding: utf-8 -*-
import rumps


class MyToolbox(rumps.App):
    @rumps.clicked("Hello world")
    def my_function(self, sender):
        print('Hello World !')


if __name__ == '__main__':
    rumps.debug_mode(True)
    app = MyToolbox("⛏")
    app.run()
