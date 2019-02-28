from  classes.enemy import Enemy

enemy = Enemy(200, 60)
print("hp",enemy.get_hp())
















'''
import random

class Enemy:

    hp = 600

# This is used to intiliaze and to make the values more dynamic
    def __init__(self, atkl, atkh):

        self.atkl = atkl
        self.atkh = atkh

    def getatk(self):

        print("Enemy attack is : ", self.atkl)

    def gethp(self):
        print(" Enemy Hp is :", self.hp)

enemy1 = Enemy(40, 60)
enemy1.getatk()
enemy1.gethp()

enemy2 = Enemy(90, 100)
enemy2.getatk()
enemy2.gethp()








'''
'''
playerhp = 500
enmyatkl = 25
enmyatkh = 50


while playerhp > 0 :

    damage = random.randrange(enmyatkl, enmyatkh)
    playerhp = playerhp - damage

    if playerhp <=30:
        playerhp = 30

    print(" Enemy attack dmg was" , damage , "your health is ", playerhp)

    if playerhp > 30 :
        continue

    print("you're health is low so you will be transported to an INN")
    break


'''




