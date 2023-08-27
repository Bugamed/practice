
def nfib(number):
    x,y = 0,1
    n = 1
    try:
        number = int(number)
    except:
        raise ValueError
    if number <= 0:
        raise OutOfRangeError
    while number >= n:
        x,y = y, x+y
        n += 1
    return x

# Создание списка через list() - прошу прощения, я не очень понял, как конкретно от меня ожидается эта проверка,
# поэтому сделаю это УЖАСНО ТУПО

result = list((nfib(1), nfib(2), nfib(3), nfib(4), nfib(5),
              nfib(6), nfib(7), nfib(8), nfib(9), nfib(10),
              nfib(11), nfib(12), nfib(13), nfib(14), nfib(15),
              nfib(16), nfib(17), nfib(18), nfib(19), nfib(20)
))

print(result)

# Создание списка через генератор списка

result = [nfib(i) for i in range(1,21)]
print(result)

# Создание списка через цикл for
result = []
for i in range(1,21):
    result.append(nfib(i))
print(result)

# Создание списка через генератор множества

result = {nfib(i) for i in range(1,21)}
print(result)