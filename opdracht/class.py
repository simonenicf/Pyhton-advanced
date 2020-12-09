class Bees:
    stingPower = 5
    speed = 10
    health = 50
    cuteness = 100

    def sting(self):
        print("The bee is stinging you.")
        print("You take " + str(Bees.stingPower) + " damage.")

    def flies(self):
        print("I am a bee and I can fly.")

print(Bees.stingPower)

class qeeunBee (Bees) :
    lives = 3
         
    def sting(self):
        super().sting()
        print("You are now posioned.")

    def flies(self):
        print("Qeeun bee is too lazy to fly but she does it when she needs to.")

    def notTheBees(self):
        print("Qeeun bee summons a bunch of bees.")


beesA = Bees()
qeeunBeeA = qeeunBee()

# Super sting function
qeeunBeeA.sting()
beesA.sting()

# flies function
qeeunBeeA.flies()
beesA.flies()