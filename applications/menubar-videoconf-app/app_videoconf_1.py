# -*- coding: utf-8 -*-
import rumps
import pyperclip
import videoconf
import webbrowser


class MyToolbox(rumps.App):
    @rumps.clicked("Instant Video Conference")
    def launch_video_conference(self, sender):
        url = videoconf.generate_videoconf_url()
        webbrowser.open(url, new=2)
        pyperclip.copy(url)


if __name__ == '__main__':
    rumps.debug_mode(True)
    app = MyToolbox("⛏")
    app.run()


# faker / python
