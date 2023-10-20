
al = (55, 6, 's', 77.3, 70.0, '7', 'A')

integers = tuple(a for a in al if isinstance(a, int)) # тут мы используем цикл и условный оператов, цикл для того чтобы он прошелся по всем элементам, а if чтобы он проверил являются ли эти элементы int.

floats = tuple(a for a in al if isinstance(a, float)) # аналогично с float

strings = tuple(a for a in al if isinstance(a, str)) # ну str то же самое

print(integers)
print(floats)
print(strings)