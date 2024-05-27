import to_do_oop


class ToDoList:

    def __init__(self):
        self.to_do_list = []

    def add_to_do_element(self, element: to_do_oop.ToDo):
        self.to_do_list.append(element)

    def remove_to_do_element(self, element: to_do_oop.ToDo):
        self.to_do_list.remove(element)

    def print_to_do_list(self):
        for element in self.to_do_list:
            print(element)
