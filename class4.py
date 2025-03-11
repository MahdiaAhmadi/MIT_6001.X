
class Spell(object): #Parent Class
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell): # child Class
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell): #child Class
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio() # one object from Accio class create
spell.execute() # print out --> Accio
studySpell(spell) # print out --> Summoning Charm Accio 
# No description
studySpell(Confundo()) # print out --> Confundus Charm Confundo 
# Causes the victim to become confused and befuddled.