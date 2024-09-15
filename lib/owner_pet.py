class Pet:
     pass

     PET_TYPES = ['dog', 'cat', 'rodent', 'bird','reptile', 'exotic']
     all = []
     def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

     def get_pet(self):
        return self._pet_type
     def set_pet(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Not a valid pet type')
        self._pet_type = pet_type
     pet_type = property(get_pet, set_pet)

    

class Owner:
    pass
    def __init__(self, name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception('Input object is not of type Pet')
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

    
