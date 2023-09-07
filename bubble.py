from random import randint
import time

def bubble(array):
    start = time.process_time()
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    end = time.process_time() - start
    print(f'Список отсортирован за {end} секунд.\n\nОтсортированный список:\n\n{array}\n')
    print(f'Сумма 10 минимальных чисел списка:{sum(array[:9])} \nСумма 10 максимальных чисел списка:{sum(array[-10:])}')

def generator(num):
    spisok = []
    for _ in range(num):
        spisok.append(randint(10000,99999))
    print(f'Список сгенерирован.\n\n{spisok}\n')
    return spisok

def nask(amin=20,amax=1000):
    while True:
        try:
            num = int(input(f'введите количество чисел для сортировки(от {amin} до {amax}):\n'))
        except ValueError:
            print('Число введено неверно! Попробуйте снова\n')
        if num > 1000 or num < 20:
            print(f'Введённое число не попадает в диапазон [{amin}..{amax}]. Попробуйте снова\n')
        else:
            return num
    
bubble(generator(nask()))

#ляля тополя
