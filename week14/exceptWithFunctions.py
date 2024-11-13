class Character:
    def __init__(self, name, initialGold, initialExperience) -> None:
        self.name = name
        self.gold = initialGold
        self.experience = initialExperience

    def __str__(self) -> str:
        return f"{self.name} has {self.gold} gold and {self.experience} experience."

def divideLoot(characters, goldAmount, experienceAmount):
    if(goldAmount < 0 or experienceAmount < 0):
        raise ValueError("Gold and experience amounts cannot be negative")
    numCharacters = len(characters)
    goldPerCharater = goldAmount / numCharacters
    experiencePerCharater = experienceAmount / numCharacters
    for character in characters:
        character.gold += goldPerCharater
        character.experience += experiencePerCharater

def main():
    ted = Character("ted", 100, 1)
    ned = Character("ned", 20, 20)
    fred = Character("fred", 33, 21)
    
    print(ted)
    print(ned)
    print(fred)

    print("Part 1")
    try:
        divideLoot([ted, ned], 100, 100)
    except Exception as e:
        print("Exception: " + str(e))

    print(ted)
    print(ned)
    print(fred)


    print("Part 2")
    try:
        divideLoot([fred, ned], -100, 100)
    except Exception as e:
        print("Exception: " + str(e))

    print(ted)
    print(ned)
    print(fred)

    print("Part 3")
    try:
        divideLoot([], 100, 100)
    except Exception as e:
        print("Exception: " + str(e))

    print(ted)
    print(ned)
    print(fred)

if __name__ == "__main__":
    main()