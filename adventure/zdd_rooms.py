"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
from time import sleep
import random


class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            return [x for x in user_items if x.name != "old book"]
        return user_items

## ----------------------------------------------------------------
## List here all rooms

class UndergroundLake(Room):
    def __init__(self, name, description, items=None):
        super().__init__(name, description, items)
        self.monsters_awake = False
        self.treasure_found = False  # New state: Has the player already found the treasure?

    def run_story(self, user_items):
        print(self.description)
        while True:
            action = input("What would you like to do? (enter platform / inspect water / dive / leave): ").strip().lower()

            if action == "enter platform":
                self.monsters_awake = True
                print(
                    "You step onto the platform and pick up the lantern. Suddenly, the water begins to churn, "
                    "and creatures emerge!"
                )
                self.handle_creatures(user_items)
            elif action == "inspect water":
                print("You see your reflection... and notice something shimmering in the water!")
                print("Maybe you should dive?")
            elif action == "dive":
                if self.treasure_found:
                    print("You have already found the treasure. There's nothing else here.")
                else:
                    print("You dive into the cold water and start searching...")
                    if any(item.name == "Mysterious Lantern" for item in user_items):
                        print("The lantern lights the way. You discover a chest!")
                        treasure = Item("Golden Necklace", "A shiny necklace made of pure gold.", movable=True)
                        user_items.append(treasure)
                        self.treasure_found = True
                        print("You take the Golden Necklace with you!")
                    else:
                        print("Without light, it's too dark to find anything. You swim back up.")
            elif action == "leave":
                print("You leave the lake and return to the previous area.")
                break
            else:
                print("That is not a valid action. Please try again.")
        return user_items

    def handle_creatures(self, user_items):
        if any(item.name == "Mysterious Lantern" for item in user_items):
            print("The lantern protects you! The creatures retreat into the darkness.")
        else:
            print(
                "Without the lantern, the creatures attack you! "
                "You barely escape back to the shore, but you're exhausted."
            )

class TableTennisRoom(Room):

    training_score = 0
    skills = []

    

    def play_match(self):
        """
        Simulates a table tennis match between the player and the robot.

        First, the player and the robot decide who has the first serve by
        choosing a number between 1 and 2. If the player's number matches the
        random number, the player has the first serve.

        Then the actual match begins. The player's winning probability is
        determined by their training score. The player wins if their winning
        probability is higher or equal to a random number between 0 and 4.
        """
        print()
        print("To start the match, we need to choose who has the first serve.")
        print("If your number is equal to a random number between 1 and 2, you get the first serve.")
        first_serve_input = input("Choose number 1 or 2: ")
        first_serve = random.randint(1, 2)

        if first_serve == int(first_serve_input):
            print("You have the first serve! Good luck!")

        else:
            print("The robot has the first serve! Good luck!")

        winning_probability = self.training_score
        random_number = random.randint(0, 4)

            
        if winning_probability >= random_number:
            sleep(3)
            print("You won the match! Congratulations!")
                    

        elif winning_probability < random_number:
            sleep(3)
            print("The robot won the match! Better luck next time.")
            print("Maybe you should train a bit more.")
                    

    def train(self):
        """
        Train a specific table tennis skill to improve the player's chance of winning a match.

        The player can choose to train either 'attack', 'defense', or 'service'. If the player
        chooses to train a skill that they already have, they will be asked to choose another
        skill to train.

        The training process takes 3 seconds and will increase the player's training score by 1.
        """
        print()
        print("You decide to train to improve your game.")

        while True:
            training_choice = input("What would you like to train? 'attack', 'defense', or 'service': ")

            if training_choice in self.skills:
                print("You already trained your", training_choice + "!")
                print("I think you should focus on another skill instead.")

            else:
                print("OK let's improve your", training_choice + "!")
                sleep(3)
                self.training_score += 1
                self.skills.append(training_choice)
                print("Wow your", training_choice + " looks really good now!")
                break

            

    def run_story(self, user_items):

        """
        main loop
        When the player enters the room, they are asked if they want to play a match or train.
        If they choose to play a match or tain, they need to have a racket in their inventory. 
        If they don't have a racket, they are asked if they want to buy one.
        If they choose to leave the room, the function will break the loop and return the user_items.

        """
        
        print("Welcome to the ZDD Table Tennis Room where you can play table tennis.")
        print("Here you can play a match against a robot or train to improve your game.")


        while True:
            print()
            choice = input ("You're in the ZDD Table Tennis Room. Would you like to play a match, train or leave the room? (match/train/leave): ")

            if choice == "match":
               
                if "table tennis racket" in [item.name for item in user_items]:
                    self.play_match()

                elif "table tennis racket" not in [item.name for item in user_items]:	
                    print("You don't have a racket. You need a racket to play table tennis.")
                    racket_input = input("Would you like to borrow a racket? (yes/no): ")

                    if racket_input == "yes":
                        table_tennis_racket = Item("table tennis racket", "a table tennis racket", movable=True)
                        user_items.append(table_tennis_racket)
                        print("You borrowed a racket. Let's play a match!")
                        self.play_match()

                    elif racket_input == "no":
                        print("Sorry, you can't play table tennis without a racket.")

                    else:
                        print("Invalid choice. Please try again.")

            
            elif choice == "train":

                if "table tennis racket" in [item.name for item in user_items]:
                    self.train()
                    

                elif "table tennis racket" not in [item.name for item in user_items]:
                    print("You need a racket to train.")
                    racket_input = input("Would you like to borrow a racket? (yes/no): ")

                    if racket_input == "yes":
                        table_tennis_racket = Item("table tennis racket", "a table tennis racket", movable=True)
                        user_items.append(table_tennis_racket)
                        print("You borrowed a racket. Now we can start the training session!")
                        self.train()
                        

                    elif racket_input == "no":
                        print("Sorry, you can't play table tennis without a racket.")

                    else:
                        print("Invalid choice. Please try again.")
                        

            elif choice == "leave":
                break

            else:
                print("Invalid choice. Please try again.")

                    

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Add your room instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

mysterious_lantern = Item("Mysterious Lantern", "A lantern emitting a calming light. It protects against the creatures of the Underground Lake.", movable=True)
underground_lake = UndergroundLake(
    "The Underground Lake",
    "A vast, dark room with a silent lake and a mysterious lantern on a platform.",
    [mysterious_lantern]
)
table_tennis_room = TableTennisRoom("table tennis room", "A room where you can play table tennis.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "underground_lake":underground_lake,
    "table_tennis_room": table_tennis_room
}
