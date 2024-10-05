# p5r confidant info grabber
# mvanarsdale
# 10/05/24


# libraries
from time import sleep

# confidant class 
class confidant:
    def __init__(self, name, arcana, location):
        self._name = name
        self._arcana = arcana
        self._location = location
        
    # getters
    def get_name(self):
        return self._name 
    def get_arcana(self):
        return self._arcana
    def get_location(self):
        return self._location
        
    # setters   
    def set_name(self, name):
        self._name = name 
    def set_arcana(self, arcana):
        self._arcana = arcana
        
    # methods
    def __str__(self):
        return (self._name + " has the " + self._arcana + " persona, and can be found " + self._location)
    
class personaHolder(confidant):
    def __init__(self, name, arcana, location, codeName):
        super().__init__(name, arcana, location)
        self._codeName = codeName
    
    # methods
    def __str__(self):
        return (self._name + ", referred to as " + self._codeName + " in the metaverse," + " has the " + self._arcana + " persona, and can be found " + self._location)

# subroutines         
# inputed confidants name will return information about that confidant 
def findingConfidant():
    # gets the name of the confidant user is looking for 
    message = "Enter a confidants full name"
    for char in message:
        print(char, end = "")
        sleep(0.07)
    confidantsName = input("\n") 
    # persona holding confidants 
    if confidantsName.lower() == "morgana":
        Morgana = personaHolder("Morgana", "Magician", "with the player", "Mona")
        print(Morgana)
        mainProgram()
    elif confidantsName.lower() == "ryuji":
        Ryuji = personaHolder("Ryuji", "Chariot", "at Shujin Academy on the 2nd Floor", "Skull")
        print(Ryuji)
        mainProgram()
    elif confidantsName.lower() == "ann":
        Ann = personaHolder("Ann", "Lovers", "at the underground mall", "Panther")
        print(Ann)
        mainProgram()
    elif confidantsName.lower() == "yusuke":
        Yusuke = personaHolder("Yusuke Kitagawa", "Emperor", "by the underground walkway", "Fox")
        print(Yusuke)
        mainProgram()
    elif confidantsName.lower() == "makoto":
        Makoto = personaHolder("Makoto Niijima", "Priestess", "Standing around Shujin", "Queen")
        print(Makoto)
        mainProgram()
    elif confidantsName.lower() == "futaba":
        Futaba = personaHolder("Futaba Sakura", "Hermit", "outside Leblanc", "Oracle")
        print(Futaba)
        mainProgram()
    elif confidantsName.lower() == "haru":
        Haru = personaHolder("Haru Okumura", "Empress", "on the rooftop of Shujin", "Noir")
        print(Haru)
        mainProgram()
    elif confidantsName.lower() == "akechi":
        Akechi = personaHolder("Goro Akechi", "Justice", "outside Penguin Sniper", "Crow")
        print(Akechi)
        mainProgram()
    elif confidantsName.lower() == "yoshizawa":
        Kasumi = personaHolder("Kasumi Yoshizawa", "Faith", "in Kichijoji", "Violet")
        print(Kasumi)
        mainProgram()
    # velvet room confidants
    elif confidantsName.lower() == "igor":
         Igor = confidant("Igor", "Fool", "in the Velvet Room")
         print(Igor)
         mainProgram()
    elif confidantsName.lower() == "caroline and justine":
        Twins = confidant("Caroline and Justine", "Strength", "in the Velvet Room")
        print(Twins)
        mainProgram()
    # non persona holding adult confidants 
    elif confidantsName.lower() == "sojiro":
        Sojiro = confidant("Sojiro Sakura", "Hierophant", "in LeBlanc")
        print(Sojiro)
        mainProgram()
    elif confidantsName.lower() == "mifune":
        Chihaya = confidant("Chihaya Mifune", "Fortune", "at Shinjuku")
        print(Chihaya)
        mainProgram()
    elif confidantsName.lower() == "iwai":
        Iwai = confidant("Munehisa Iwai", "Hanged Man", "at gun shop on Central Street")
        print(Iwai)
        mainProgram()
    elif confidantsName.lower() == "takemi":
        Takemi = confidant("Tae Takemi", "Death", "at her clinic")
        print(Takemi)
        mainProgram()
    elif confidantsName.lower() == "kawakami":
        Kawakami = confidant("Sadayo Kawakami", "Temperance", "by calling her from the yellow pay phone")
        print(Kawakami)
        mainProgram()
    elif confidantsName.lower() == "ohya":
        Ohya = confidant("Ichiko Ohya", "Devil", "at the Crossroads bar in Shinjuku")
        print(Ohya)
        mainProgram()
    elif confidantsName.lower() == "niijima":
        Niijima = confidant("Sae Niijima", "Judge", "in several locations throughout the story")
        print(Niijima)
        mainProgram()
    elif confidantsName.lower() == "maruki":
        Maruki = confidant("Takuto Maruki", "Councillor", "by Shinjuku's practice building")
        print(Maruki)
        mainProgram()
    elif confidantsName.lower() == "yoshida":
        Yoshida = confidant("Toranosuke Yoshida", "Sun", "in station square")
        print(Yoshida)
        mainProgram()
    # non persona holding minor confidants 
    elif confidantsName.lower() == "oda":
        Oda = confidant("Shinya Oda", "Tower", "at the Akihabara arcade")
        print(Oda)
        mainProgram()
    elif confidantsName.lower() == "hifumi":
        Hifumi = ("Hifumi Togo", "Star", "at the church")
        print(Hifumi)
        mainProgram()
    elif confidantsName.lower() == "mishima":
        Mishima = confidant("Yuuki Mishima", "Moon", "in locations like; Shibuya, Shinjuku and Akihabara")
        print(Mishima)
        mainProgram()
    else:
        noNameFound()
        findingConfidant()

# handles misinput from user typing in names  
def noNameFound():
    notFound = "Hmm...I don't see that name in my list"
    for char in notFound:
        print(char, end = "")
        sleep(0.05)
    tip = "\nTip: Check the character name guide in the README file\n"
    for character in tip:
        print(character, end = "")
        sleep(0.05)
    # sends user back to type in name again
    loadingBuffer()
    findingConfidant()

# handles misinput from user typing command
def unknownCommand():
    error = ("That command doesn't exist..")
    tip = ("\nTip: Make sure you're spelling the command exactly as presented!")
    for character in error:
        print(character, end = "")
        sleep(.05)
    for char in tip:
        print(char, end = "")
        sleep(.05)
    loadingBuffer()
    mainProgram()
    
# loading sequence for visual purposes    
def loadingBuffer():
    for star in range(5):
        print("✦", end = "")
        sleep(.5)
    print("\n")

# subroutine for main program
def mainProgram():
    loadingBuffer()
    message = "Would you like to (enter) a confidants name or (exit) the program?"
    for char in message:
        print(char, end = "")
        sleep(0.07)
    
    continueAnswer = input("\n")
    if continueAnswer.lower() == "enter":
        findingConfidant()
        loadingBuffer()
        print("\n")
        sleep(2) 
    # stops program 
    elif continueAnswer.lower() == "exit":
        loadingBuffer()
        break
    else:
        unknownCommand()
        mainProgram()
 
# main program  
running = True
while running:
    mainProgram()