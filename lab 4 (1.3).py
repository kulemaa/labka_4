
a_tuple = input("The first: ")
b_tuple = input("The second: ")

half_a = len(a_tuple) // 2 #len() узнает сколько элементов содержит итерируемый объект.
half_b = len(b_tuple) // 2 #делим это все на 2, ибо нам нужна лишь половина введенных элементов

result = a_tuple[:half_a] + b_tuple[half_b:]

print(result, " ")