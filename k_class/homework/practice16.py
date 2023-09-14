class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self):
        print(f"{self.name}가 공격받았습니다!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name}이(가) 기절했습니다.")
        else:
            print(f"{self.name}의 체력: {self.health}")


character = Character("캐릭터")

character.attack()
character.take_damage(30)
character.attack()
character.take_damage(80)
