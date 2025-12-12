from sys import maxsize


class Project:

    def __init__(self, id = None,  name = None, description = None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.id}:{self.name}"

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __lt__(self, other):
        if self.name != other.name:
            return self.name < other.name
        return self.description < other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize