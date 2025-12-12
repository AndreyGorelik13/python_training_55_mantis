from sys import maxsize


class Project:

    def __init__(self,  name = None, description = None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}:{self.description}"

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description

    def __lt__(self, other):
        # сортируем по имени, если имена совпадают — по описанию
        if self.name != other.name:
            return self.name < other.name
        return self.description < other.description