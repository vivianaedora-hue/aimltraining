class student:
    def __init__(self, id, name):
        self.id=id
        self.name=name

    def print_info(self):
        print('Student ID: ',self.id)
        print('Student name: ',self.name)