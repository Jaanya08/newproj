import time

class MysteryAdventure:
    def __init__(self):
        self.inventory = []
        self.locations = {
            "Mansion Entrance": "A grand but eerie mansion stands before you.",
            "Library": "Rows of dusty books line the walls. A mysterious book catches your eye.",
            "Basement": "It’s dark and cold. Something seems hidden in the shadows.",
            "Secret Room": "You’ve uncovered a hidden chamber filled with strange artifacts."
        }
        self.current_location = "Mansion Entrance"

    def display_location(self):
        print(f"\nYou are at: {self.current_location}")
        print(self.locations[self.current_location])
        time.sleep(1)

    def explore(self):
        if self.current_location == "Library":
            print("You find an old book with a hidden key inside!")
            self.inventory.append("Key")
        elif self.current_location == "Basement":
            if "Key" in self.inventory:
                print("You use the key to unlock a secret door!")
                self.current_location = "Secret Room"
            else:
                print("You see a locked door but have no key.")
        elif self.current_location == "Secret Room":
            print("You discover an ancient artifact and solve the mansion's mystery! You win!")
            exit()
        else:
            print("There's nothing special here.")
        time.sleep(1)

    def move(self):
        print("\nWhere do you want to go?")
        for loc in self.locations.keys():
            print(f"- {loc}")
        choice = input("Enter location: ")
        if choice in self.locations:
            self.current_location = choice
        else:
            print("Invalid location. Try again.")

    def play(self):
        print("Welcome to the Mystery Adventure Game!")
        while True:
            self.display_location()
            action = input("\nDo you want to (1) Explore or (2) Move? ")
            if action == "1":
                self.explore()
            elif action == "2":
                self.move()
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    game = MysteryAdventure()
    game.play()
