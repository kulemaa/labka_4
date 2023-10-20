
a_set = {1, 2, 3, 4, 7}
b_set = {8, 7, 9, 4, 2, 0, 10}
c_set = {4, 0, 1}

for element in a_set.copy(): #получается мы избегаем изменения в a_set, и из-за этого создаем еопию этого элемента
    if element in c_set:
        a_set.remove(element) # в if если в элементы есть в a_set то мы их удаляем и добавляем в b_set
        b_set.add(element)

print(f"Set c after the operation: {c_set}")
