class Pet:
     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
     all = []

     def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)



class Owner:
     def __init__(self, name):
        self.name = name

     def pets(self):
        """Return a list of all pets that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

     def add_pet(self, pet):
        """Assign the pet to this owner, after validating it's a Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Can only add an instance of Pet.")
        pet.owner = self

     def get_sorted_pets(self):
        """Return the owner's pets sorted alphabetically by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)



owner1 = Owner("John")
owner2 = Owner("Jane")


pet1 = Pet("Fido", "dog", owner1)
pet2 = Pet("Whiskers", "cat", owner1)
pet3 = Pet("Clifford", "dog", owner2)


owner2.add_pet(Pet("Jerry", "reptile", owner2))


print(owner1.pets())
print(owner2.pets())


print(owner1.get_sorted_pets())  
print(owner2.get_sorted_pets())