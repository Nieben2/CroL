import time
import random


class energy():
    def __init__(self):
        self.max_energy = 1000
        self.energy = self.max_energy
        self.fed = 1
        self.health = 1

    def energy_loss(self, seconds, health, workload):
        self.health = health
        self.energy -= (workload * seconds / health)

        if self.energy < 0:
            if self.energy < -30: self.energy = -30
            self.energy_low(self.health, self.fed)
        return self.energy

    def energy_gain(self, seconds, healt, fed):
        self.fed = fed
        self.health = healt
        self.energy += fed * seconds * healt
        if (self.energy >= self.max_energy):
            self.energy = self.max_energy
        return self.energy

    def energy_low(self, health, fed):
        if self.energy < 0:
            print("You drive your body too hard, the energy is running out!!")
            time.sleep(2)
            print("You pass out!")
            while self.energy <= 10:
                time.sleep(5)
                self.energy = self.energy_gain(5, health, fed)
                if self.energy <= 10:
                    text = random.randint(1, 5)
                    if text == 1:
                        print("You hazily wake and try to get up, but you are still too low on energy (" + str(
                            round(self.energy, 2)) + ")")
                        print("You pass out")
                    if text == 2:
                        print("......snork...")
                    if text == 3:
                        print("You slowly wake up, trying to dispell the fog from your eyes... (" + str(
                            round(self.energy, 2)) + ")")
                        print("You pass out")
                    if text == 4:
                        print("........")
                    if text == 5:
                        print("..............")
            print("You wake up, feeling not well")
        if fed < 0 :
            print("You pass out from hunger!")
            time.sleep(10)
            print("When you wake up you are weak and powerless, you need some nutrition quickly!\n"
                  "You scrape some dirt with your fingernails and manages to collect "
                  "an unfiltered selection of vegetation and roots. You think there might "
                  "even be some insects in your upcoming meal.\n You should get some real food soon!")
            self.fed = 0.05




# human = energy()
#
# running = True
# while running:
#     prompt = input(
#         "Are you doing work or resting or eating? (w/r/e) Your energy level is " + str(round(human.energy, 2)) + "\n")
#     if prompt == "w":
#         if human.fed > 0:
#             workload = int(input("How hard will you work (1-10)?")) / 10
#             lost = human.energy - human.energy_loss(int(input("For how long are you working?")), 0.9, workload)
#             print("Energy loss was " + str(round(lost, 2)))
#             human.fed -= (workload / 10)
#         elif human.fed < 0:
#             prompt("You are so hungry that you are passing out")
#             human.energy_low(0.9, human.fed)
#     elif prompt == "e":
#         print("You eat a banana or something")
#         human.fed += 0.1
#         if human.fed > 1: human.fed = 1
#
#     elif prompt == "r":
#         gained = -human.energy + human.energy_gain(int(input("For how long are you not working?")), 0.9, human.fed)
#         print("Energy gained was " + str(round(gained)))
#     else:
#         print("Please choose (w)ork (e)at or (r)est!")
# # print(human.energy)
