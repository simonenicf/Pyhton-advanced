class Player:
    # the variables of the lives, speed and stats
    speed = 0
    life = 0
    stats = 0

    # lets you get arguments for life and speed.
    def __init__(self, l, s):
        self.life = l
        self.speed = s
    
    # While tell you what your speed, lives and stats
    def status(self):
        print("My speed is = " + str(self.speed))
        print("I have " + str(self.life))
        print("My total stat score is: " + str(self.stats))

    # Counts how much stats you have
    def total(self):
        self.stats = self.speed + self.life

x = Player(5, 1)

# exucutes my total program
x.total()

x.status()





