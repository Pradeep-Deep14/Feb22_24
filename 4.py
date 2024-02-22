class Animal:
    @staticmethod
    def getSound():
        return 'roar'

class Cat(Animal):
    pass

print(Cat.getSound())