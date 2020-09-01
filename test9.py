class Monster:
    def __init__(self, name, size, hp, sub):
        self.name = name
        self.size = size
        self.hp = hp
        self.sub = sub

    # def attack(self):
        #	globals last_hp
        #    last_hp = self.hp-self.sub
    #    return last_hp


green = Monster("green1", 10, 50, 7)

print(green.name)
