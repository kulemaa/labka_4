try:
    a = input("Enter your word: ")

    set = {string for string in a} # тут допустим мы используем генератор множеств

    print(f"Created set is: {set}") # думаю, с ф-стрингом все понятно, юзал на всех лабках
except ValueError:
    print("Error")