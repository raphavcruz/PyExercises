#Guessnthe number!
#The Algorithm will generate a value from 1-100 and you will have to guess based on the app instruction
import random
class GuessTheNumber:
    def __init__(self):
        self.any_number = 0
        self.min_value = 1
        self.max_value = 100

    def Start(self):
            self.GenerateRdmNumber()

    def GenerateRdmNumber(self):
            return random.randint(self.min_value, self.max_value)

