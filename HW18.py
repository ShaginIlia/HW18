class Building:
    def __init__(self, floor, type):
        self.numberOfFloors = int(floor)
        self.buildingType = str(type)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType ==  other.buildingType


    def __str__(self):
        return f'{self.numberOfFloors, self.buildingType}'


b = Building(2, 'деревянный')
ab = Building(5, 'stone')
print(b)
print(b.numberOfFloors == ab.numberOfFloors)
print(b.buildingType == ab.buildingType)


