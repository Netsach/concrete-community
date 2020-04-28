# -*- coding: utf-8 -*-
import uuid


def generate_videoconf_url():
    unique_id = uuid.uuid4()
    url = f'https://meet.jit.si/{unique_id}'
    return url


if __name__ == '__main__':
    print("*" * 80)
    print('generate_videoconf_url')
    print("-" * 80)
    print(generate_videoconf_url())
    print("*" * 80)
