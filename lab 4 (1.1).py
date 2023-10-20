
try:
    a = input("Enter your string: ")

    a_tuple = tuple(a) #метод tuple и есть то, что разделяет введенный нами строку

    print(f"The string with tuple is: {a_tuple}")
except ValueError:
    print("Error")