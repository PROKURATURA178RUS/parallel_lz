import requests
import threading
import time

#Добавляем ссылки
urls = ['https://auto.ru/?utm_referrer=https%3A%2F%2Fwww.google.com%2F',
'https://www.drom.ru/',
'https://av.by/',
'https://www.youtube.com/?app=desktop&hl=ru',
'https://store.steampowered.com/?l=russian',
'https://www.instagram.com/',
'https://www.twitch.tv/',
'https://www.nvidia.com/en-us/',
'https://audi-minsk.by/',
'https://www.mercedes-benz.com/en/'
]

#Функция, которая покажет какой сайт загружен и сколько было загружено
def download(url):
    response = requests.get(url)
    print(f'Downloaded {url} (size: {len(response.content)} bytes)')

#Загрузка сайтов без потоков
def without_threading():
    start_time = time.time()
  
    for url in urls:
        download(url)
    
    end_time = time.time()
    print(f"Without threading: {end_time - start_time:.7f} sec")
    return end_time - start_time

#Загрузка сайтов с потоками
def with_threading():
    start_time = time.time()
    
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=(url,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"With threading:{end_time - start_time:.7f} sec")
    return end_time - start_time

#Функция, сравнивающая время выполнения функций
def compare(without_time, with_time):
    difference = without_time - with_time

    print(f"Without threading time {without_time:.7f} sec ")
    print(f"With threading time{with_time:.7f} sec ")
    print(f"Difference:{difference} ")

without_time = without_threading() 
with_time = with_threading()


def main():
    without_threading()
    with_threading()
    compare(without_time,with_time)

    
if __name__ == "__main__":
    main()