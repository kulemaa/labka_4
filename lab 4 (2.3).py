
a_set = {1, 2, 3, 4, 5}
b_set = {5, 7, 8, 9, 2, 10}


a_set.difference_update(b_set) # difference_update же уже выполняет обратную задачу

print(f"difference set is: {a_set}")

#но также есть и метод без использования differende_update
a_set = {1, 2, 3, 4, 5}
b_set = {5, 7, 8, 9, 2, 10}

a_set -= b_set

print(f"difference set is: {a_set}")