import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength = strength
    
    def attack(self):
        #return strenth to solider
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        #remove damage from health
        self.health-=damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health,strength)


    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        #remove damage from health
        super().receiveDamage(damage)
        if self.health >0:
            return f"{self.name} has recieved {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)

    def receiveDamage(self, damage):
        # your code here
        super().receiveDamage(damage)
        if self.health >0:
            return f"{self.name} has recieved {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"        

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        attacked_saxon = random.choice(self.saxonArmy)
        attacking_viking = random.choice(self.vikingArmy)

        damage = attacking_viking.strength
        result = attacked_saxon.recieveDamage (damage)
        self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health>0]
        return result


    def saxonAttack(self):
        # your code here
        attacked_viking = random.choice(self.vikingArmy)
        attacking_saxon = random.choice(self.saxonArmy)

        damage = attacking_saxon.strength
        result = attacked_viking.recieveDamage (damage)
        self.vikingArmy = [viking for viking in self.vikingArmy if viking.health>0]
        return result

    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            return "Vikings have won the war of the century!!"
        if not self.vikingArmy
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy)>=1 and len(self.vikingArmy)>=1:
            return "Vikings and Saxons are still in the thick of battle."
    pass

#yop
class War2:
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        attacked_saxon = random.choice(self.saxonArmy)
        attacking_viking = random.choice(self.vikingArmy)

        damage = attacking_viking.strength
        result = attacked_saxon.recieveDamage (damage)
        self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health>0]
        return result


    def saxonAttack(self):
        # your code here
        attacked_viking = random.choice(self.vikingArmy)
        attacking_saxon = random.choice(self.saxonArmy)

        damage = attacking_saxon.strength
        result = attacked_viking.recieveDamage (damage)
        self.vikingArmy = [viking for viking in self.vikingArmy if viking.health>0]
        return result

    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        if not self.vikingArmy
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy)>=1 and len(self.vikingArmy)>=1:
            return "Vikings and Saxons are still in the thick of battle."
    pass


