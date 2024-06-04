import os
from character import Hero, Enemy
from weapon import long_sword, short_sword, fists


print("""
                                  |>>>
                                  |
                    |>>>      _  _|_  _         |>>>
                    |        |;| |;| |;|        |
                _  _|_  _    \\.    .  /    _  _|_  _
               |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|
               \\..      /     |;   . |    \\.    .  /
                \\.  ,  /      |:  .  |     \\:  .  /
                 ||:   |_   _  |_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |       \,/
                 ||:   ||:  ,  _______   .   ||: , |            
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    '--~~__|.    |+++++__|----~    ~`---,            
-~--~                   ~---__|,--~'                  ~~----_____
<=======================================================================>
                            -- KnightFall -- 
<=======================================================================>
1. NEW GAME
2. LOAD GAME
3. CREDITS
4. GRAVEYARD
5. EXIT
<=======================================================================>
      
""")

hero = Hero(name="Hero", health=100)
hero.equip(long_sword)
enemy = Enemy(name="Enemy", health=100, weapon=long_sword)




while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input("Press Enter to continue...")


