class PlayerStatus(object):
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.busts = 0

    def printStatus(self):
        print(str(self.wins) + ' wins')
        print(str(self.losses) + ' losses')
        print(str(self.draws) + ' draws')
        print(str(self.busts) + ' busts')

    def restart(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.busts = 0

