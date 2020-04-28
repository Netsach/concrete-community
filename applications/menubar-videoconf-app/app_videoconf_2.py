# -*- coding: utf-8 -*-
from functools import partial
import rumps
import pyperclip
import videoconf
import datastore
import mailto
import webbrowser


class MyToolbox(rumps.App):
    def __init__(self):
        menu = self.build_menu()
        super().__init__('⛏', menu=menu)

    def build_menu(self):
        menu = []
        for group in datastore.retrieve('group'):
            group_name = group['name']
            emails = [member['email'] for member in group['members']]

            callback = partial(mailto.open_webbrowse_callback, emails=emails)
            menu_item = rumps.MenuItem(
                title=f'Invite [{group_name}]', callback=callback
            )

            menu.append(menu_item)

        return menu

    @rumps.clicked("Instant Video Conference")
    def launch_video_conference(self, sender):
        url = videoconf.generate_videoconf_url()
        webbrowser.open(url, new=2)
        pyperclip.copy(url)


if __name__ == '__main__':
    rumps.debug_mode(True)
    app = MyToolbox()
    app.run()
