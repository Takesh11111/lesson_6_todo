
tasks = []
next_id = 1


def create_task():
    global next_id

    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")

    task = {
        "id": next_id,
        "title": title,
        "description": description,
        "status": "новая"
    }

    tasks.append(task)
    next_id += 1

    print("Задача добавлена!")


def read_tasks():
    if len(tasks) == 0:
        print("Список задач пуст.")
        return

    for task in tasks:
        print("\nID:", task["id"])
        print("Название:", task["title"])
        print("Описание:", task["description"])
        print("Статус:", task["status"])


def update_task():
    task_id = int(input("Введите ID задачи: "))

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = input("Введите новое название: ")
            task["description"] = input("Введите новое описание: ")

            print("Выберите статус:")
            print("1. Новая")
            print("2. В процессе")
            print("3. Выполнена")

            choice = input("Ваш выбор: ")

            if choice == "1":
                task["status"] = "новая"
            elif choice == "2":
                task["status"] = "в процессе"
            elif choice == "3":
                task["status"] = "выполнена"
            else:
                print("Неверный статус.")
                return

            print("Задача изменена!")
            return

    print("Задача не найдена.")


def delete_task():
    task_id = int(input("Введите ID задачи для удаления: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Задача удалена!")
            return

    print("Задача не найдена.")


while True:
    print("\n===== СПИСОК ЗАДАЧ =====")
    print("1. Создать задачу")
    print("2. Просмотреть задачи")
    print("3. Изменить задачу")
    print("4. Удалить задачу")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        read_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "0":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор.")
