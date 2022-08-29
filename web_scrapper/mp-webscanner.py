import multiprocessing
import requests
from bs4 import BeautifulSoup
import tldextract
import time
from multiprocessing import Process, Queue


def worker(input_queue):
    while True:
        url = input_queue.get()
        if url is None:
            break

        print(f"URL : {url} \n")
        try:
            response = requests.get(url, timeout=1)
            soup = BeautifulSoup(response.text, 'html.parser')
            headers = response.headers
            print(f'Title : {soup.title.string} \n')
        except Exception as e:
            print(f'Exception in getting header  : {e}')


def main():
    number_of_workers = 10
    with open("C:\k\Projects\python_practice\web_scrapper\\top-1m.csv", 'r') as f:
        data = f.read()
    urls = data.split("\n")

    input_queue = Queue()
    workers = []

    # create Workers
    for i in range(number_of_workers):
        p = Process(target=worker, args=(input_queue,))
        workers.append(p)
        p.start()

    # distribute work
    # Getting Unique Domains only
    uniqueURLs = {}
    for url in urls:
        new = tldextract.extract(url)
        new_url = new.domain + '.' + new.suffix
        uniqueURLs[new_url] = True
    print(f'total URLs to be parsed are {len(uniqueURLs)}')
    for url in uniqueURLs:
        url = 'https://' + url
        input_queue.put(url)

    # ask worker to quit
    for w in workers:
        input_queue.put(None)

    # wait for workers to quit
    for w in workers:
        w.join()

    print("Done")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
