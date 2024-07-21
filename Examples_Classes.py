class House():
   """описание дома"""
   def __init__(self, street, number):
        """свойства дома"""
        self.street = street
        self.number = number

   def build(self):
       """строить дом"""
       print("Дои на улице " + self.street + " под номером " + str(self.number)+ " построен.")


House1 = House("Киевская",20)
House2 = House("Киевская", 21)

House1.build()

