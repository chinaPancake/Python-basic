from pexels_api import API
from tkinter import *

#wgranie api key z pexels
PEXELS_API_KEY = '563492ad6f917000010000018b2652bcf7e841a0b049109d310692e0'
api = API(PEXELS_API_KEY)

#wyszukiwanie hasła 'corgi' z strony 1, 5 wyszukań na strone
api.search('corgi', page=1, results_per_page=5)
photos = api.get_entries()

for photo in photos:
    print('photographer: ', photo.photographer)
    print(photo.original)