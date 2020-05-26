import requests
import threading

"""
Crawls a web snippet
Simulate a 429 
"""


def thread_site_launcher(url):
    print(threading.current_thread().getName())
    for i in range(10):
        page = requests.get(url)
        print(page.status_code)


#main code driver
while True:
    threading.Thread(target=thread_site_launcher, args=("http://www.google.com",)).start()


