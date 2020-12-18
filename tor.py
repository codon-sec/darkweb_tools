#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

url = 'https://ipinfo.io/json'

response = requests.get(url, proxies=proxies)
print(response.text)