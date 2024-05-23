from tabulate import tabulate
import datetime


class ToDo:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.date = datetime.datetime.now().strftime("%d/%m/%y")

    def __str__(self):
        headers = ["Title", "Description", "Date"]
        data = [[self.title, self.description, self.date]]
        return tabulate(data, headers, tablefmt="grid")

    def __repr__(self):
        return self.__str__()
