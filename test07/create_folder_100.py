class Role:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power
        if final_hp > enemy_hp:
            print("我赢了")
        elif final_hp < enemy_hp:
            print("敌人赢了")
        else:
            print("平局")

class Houyi(Role):
    def __init__(self, hp, power, defense):
        Role.__init__(self, hp, power)
        self.defense = defense

    def fight(self, enemy_hp, enemy_power):
        while True:
            self.hp = self.hp - enemy_power
            enemy_hp = enemy_hp - self.power + self.defense
            if self.hp <= 0:
                print("我成尸体了")
                break
            if enemy_hp <= 0:
                print("敌人成尸体了")
                break
            if self.hp > enemy_hp:
                print("我赢了")
            elif self.hp < enemy_hp:
                print("敌人赢了")
            else:
                print("平局")

houyi = Houyi(1000, 200, 100)
houyi.fight(1000, 100)
