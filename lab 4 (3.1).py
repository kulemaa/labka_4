import itertools

cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

sorted_cars = sorted(cars_list, key=lambda x: x[0]) # в этой задаче мы делаем сортировку по manufacter и group моделей машин
for manufacturer, group in itertools.groupby(sorted_cars, key=lambda x: x[0]): # key=lambda x: x[0] - это анонимная (лямбда) функция, которая принимает элемент x и возвращает значение x[0], то есть первый элемент кортежа, в данном случае, марку автомобиля
    group_list = list(group)
    count = len(group_list)
    models = [car[1] for car in group_list]
    print(f"{manufacturer} {count} - {', '.join(models)}")