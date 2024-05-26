class Building:
    def __init__(self, floor, type):
        self.numberOfFloors = int(floor)
        self.buildingType = str(type)

    def __eq__(self, other):
        return self.numberOfFloors == self.buildingType

    def __str__(self):
        return f'{self.numberOfFloors, self.buildingType}'


b = Building(2, 'деревянный')
print(b)
print(b.numberOfFloors == b.buildingType)
