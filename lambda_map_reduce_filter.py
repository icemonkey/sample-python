from functools import reduce

print(list(map(lambda x: x ** 2, range(11))))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(reduce(lambda x, y: x * y, range(1, 11)))  # 3628800
print(list(filter(lambda x: x % 2 == 0, range(11))))  # [0, 2, 4, 6, 8, 10]
print(list(i for i in range(11) if i % 2 == 0))  # [0, 2, 4, 6, 8, 10]

l = ['{', '"', 'a', 'g', 'e', '"', ':', ' ', '1', '2', ',', ' ', '"', 'n', 'a', 'm', 'e', '"', ':', ' ', '"', 'z', 'x',
     'w', '"', '}']
print(reduce(lambda x, y: x + y, l))

l = reduce(lambda x, y: x + y, l)
print(list(i for i in l))


