import webbrowser
import time
import random
i = 0
while i < 10:
    sites = random.choice(['google.com','youtube.com','amazon.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange
    i += 1