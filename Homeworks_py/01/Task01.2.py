todo = dict()

for i in range(3):
    dateTask = input("Введите дату: ")
    descriptionTask = input("Введите задачу: ")
    todo[dateTask] = descriptionTask

for key, value in todo.items():
    print(key + " : " + value)
