import random
import PySimpleGUI as sg

class SimpleSingleDiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        #layout
        self.layout = [
            [sg.Text("Roll the dices?")],
            [sg.Button("yes"),sg.Button("no")]
        ]
        
    def Start(self):
        #window
        self.window = sg.Window("Single Dice Simulador", layout=self.layout)
        #events
        self.events, self.values, = self.window.Read()
        while True:
            try:
                if self.events == "yes" or self.events == "y":
                    self.RollDice()
                    break
                elif self.events == "no" or self.events == "n":
                    print("Thanks for playing!")
                    break
                else:
                    print("Pleast state yes (y) or no (n)")
            except:
                print("Reply error")


    def RollDice(self):
        print(random.randint(self.min_value,self.max_value))

simulator = SimpleSingleDiceSimulator()
simulator.Start()

