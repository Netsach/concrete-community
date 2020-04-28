# -*- coding: utf-8 -*-
from videoconf import generate_videoconf_url
import webbrowser

# mailto:contact@netsach.com


def create_link(emails):
    mailing_list = ','.join(emails)
    link = f'mailto:{mailing_list}?body={generate_videoconf_url()}'
    return link


def open_webbrowse_callback(*args, **kwargs):
    emails = kwargs.get('emails')
    return webbrowser.open(url=create_link(emails), new=2)


if __name__ == '__main__':
    emails = ('test1@gmail.com', 'test2@gmail.com')
    print("*" * 80)
    print(emails)
    print("-" * 80)
    print(create_link(emails))
    print("*" * 80)
