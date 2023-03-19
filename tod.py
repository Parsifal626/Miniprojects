# Определение класса задачи (task)
class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

# Определение класса списка задач (todo list)
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append(Task(title, description))

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                print(f"Задача '{title}' выполнена!")
                return
        print(f"Задача '{title}' не найдена.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Задача '{title}' удалена!")
                return
        print(f"Задача '{title}' не найдена.")

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task.title} - {'выполнена' if task.completed else 'не выполнена'}")

# Создание экземпляра списка задач
todo_list = TodoList()

# Добавление задач в список
todo_list.add_task("Купить продукты", "Хлеб, молоко, яблоки")
todo_list.add_task("Приготовить обед", "Пожарить стейк и приготовить салат")
todo_list.add_task("Постирать белье", "Положить в стиральную машину и включить")

# Отображение списка задач
todo_list.show_tasks()

# Выполнение задачи
todo_list.complete_task("Купить продукты")

# Удаление задачи
todo_list.remove_task("Приготовить обед")

# Отображение списка задач после выполнения и удаления
todo_list.show_tasks()
