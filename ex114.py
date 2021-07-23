"""
Crie um código em Python que testa se o site Pudim está acessível pelo computador usado.
"""

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('Fora do AR')
else:
    print('Online')
