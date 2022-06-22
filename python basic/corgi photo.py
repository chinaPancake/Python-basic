from pexels_api import API
from tkinter import *

PEXELS_API_KEY = '563492ad6f917000010000018b2652bcf7e841a0b049109d310692e0'
api = API(PEXELS_API_KEY)

api.search('corgi', page=1, results_per_page=5)
photos = api.get_entries()

for photo in photos:
    print('photographer: ', photo.photographer)
    print(photo.original)

image.open