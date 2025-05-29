import multiprocessing
import random

#Функция, которая сгенерирует числа
def num_generator(conn, count, min_val, max_val):
    for _ in range(count):
        num = random.randint(min_val, max_val)
        conn.send(num)
        print(f"Generator send: {num}")
    conn.send(None)  
    conn.close()

#Функция, которая возведет числа в квадрат
def square(conn):
    while True:
        num = conn.recv()
        if num is None:
            break
        square = num ** 2
        print(f"Calculator get: {num}, square: {square}")
    conn.close()


def main():
    send_conn, recv_conn = multiprocessing.Pipe()

    num = 1000          
    min_val = -1_000_000    
    max_val = 1_000_000     

    generator = multiprocessing.Process(target=num_generator,args=(send_conn, num, min_val, max_val))
    calculator = multiprocessing.Process(target=square,args=(recv_conn,))

    # Запуск
    generator.start()
    calculator.start()

    # Завершение
    generator.join()
    calculator.join()


if __name__ == "__main__":
    main()