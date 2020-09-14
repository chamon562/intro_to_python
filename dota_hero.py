class DotaHero():
    def __init__(self, name, heroType, role):
        self.name = name
        self.heroType = heroType
        self.role = role
        self.hp = 0
    
    def add_hp(self, hp):
        self.hp += hp
    
    def damage_hp(self, damage_hp):
        self.hp -= damage_hp

    def trade_hero(self, new_team):
        self.team = new_team

axe = DotaHero("Axe", "Strength Hero", "Tank")
axe.add_hp(3500)
print('{} is the hero you have chosen and he has {} health points.'.format(axe.name, axe.hp))