import random
import time
import os


class Choice():
    def __init__(self, answer, start, end):
        self.answer = answer
        self.start = start
        self.end = end


# Create all the objects in the game. Can add or remove items from the lists.
def create_items(choice):
    choice.rooms_list = ["Living Room", "Bedroom", "Bathroom", "Kitchen", "Garage"]
    choice.room_objects = [ ["Couch", "Rug", "Plant", "TV", "Shelf"],
                            ["Bed", "Desk", "Drawer", "Lamp", "Wardrobe"],
                            ["Cabinet", "Toilet", "Basin", "Bathtub", "Towel"],
                            ["Cabinet", "Sink", "Microwave", "Oven", "Fridge"],
                            ["Tools Rack", "Car Trunk", "Spare Tire", "Box", "Door"], ]
    
    # Select which rooms are connected to each other. Check "room_layout.png" for more info
    choice.connected_index = [[1, 3], [0, 2], [1], [0, 4], [3]]

    choice.objects = {choice.rooms_list[i]:j for i, j in enumerate(choice.room_objects)}
    choice.connected = {choice.rooms_list[i]:j for i, j in enumerate(choice.connected_index)}

    # Randomly select the secret object
    choice.current_room = random.choice(choice.rooms_list)
    choice.random_room = random.choice(choice.rooms_list)
    choice.random_object = random.choice(choice.objects.get(choice.random_room))
    choice.random_object_index = choice.objects.get(choice.random_room).index(choice.random_object)
    
    # Display details in the terminal. For testing purposes only. It should be commented out!
    # print(f"Secret room is: {choice.random_room}")
    # print(f"List of objects: {choice.objects.get(choice.random_room)}")
    # print(f"Secret object is: {choice.random_object}")
    # print(f"Secret object index is: {choice.random_object_index}")


# Start menu
def start_game(choice, start_delay, game_started, floor_plan):
    if game_started == False and floor_plan == False:
        if choice.answer.lower().strip() == "yes":
            name = input("Please enter your name: ")
            print(f"\nWelcome to the hidden object game {name}")
            print("Find the secret object to win the game. Let's begin!\n")
            time.sleep(start_delay)
            game_started = True
        elif choice.answer.lower().strip() == "no":
            print("Maybe next time. Bye")
            quit()
        else:
            print("Invalid response. Please try again!")
            choice.answer = input("Do you want to play (yes/no)? ")
        
    # Show the option to view the floor plan
    elif game_started == True and floor_plan == False:
        choice.answer = input("Would you like to view floor plan (yes/no)? ")
        if choice.answer.lower().strip() == "yes":
            layout()
            floor_plan = True
        elif choice.answer.lower().strip() == "no":
            floor_plan = True
        else:
            print("Invalid response. Please try again!")

    # Start selection phase
    elif game_started == True and floor_plan == True:
        select_action(choice)
        if choice.answer.lower().strip() == "1":
            room(choice)
        elif choice.answer.lower().strip() == "2":
            location(choice)
        elif choice.answer.lower().strip() == "3":
            layout()
        else:
            if choice.answer.lower().strip() != "quit":
                print("Invalid response. Please try again!")
    return game_started, floor_plan


# Display floor plan of the building
def layout():
    file_name = "secret_layout.txt"
    if os.path.exists(file_name):
        file = open(file_name, "r")
        lines = file.readlines()

        for line in lines:
            line = line.rstrip("\n")
            print(line)
        file.close()
    else:
        print("> Missing file required to start the game")
        print(f"> Please import \"{file_name}\" into the same directory")
        quit()
    if input("Enter any key to continue: ") == "quit":
        quit()
    

# Track user's input
def selection(choice):
    if choice.end > 1:
        choice.answer = input(f"Make your selection ({choice.start}-{choice.end}): ")
    else:
        choice.answer = input(f"Make your selection ({choice.start}): ")


# Menu screen for the 2 main actions
def select_action(choice):
    print(f"\nYou are in the {choice.current_room}:")
    print("1) Explore The Room")
    print("2) Change Locations")
    print("3) View Floor Plan")
    selection(choice)


# Menu screen for the objects in a room
def room(choice):
    choice.start = 1
    choice.end = len(choice.objects.get(choice.current_room)) + 1
    flag = False

    while flag != True:
        count = 1
        print("\nYou find the following objects: ")
        for r in choice.objects.get(choice.current_room):
            print(f"{count}) {r}")
            count += 1
        
        print(f"{choice.end}) Go back")
        selection(choice)
        flag = check_objects(choice, flag)


# Menu screen for the connected rooms
def location(choice):
    count = 1
    print("\nWhere would you like to go?")
    for r in choice.connected.get(choice.current_room):
        print(f"{count}) {choice.rooms_list[r]}")
        count += 1

    index = {i:j for i, j in enumerate(choice.connected.get(choice.current_room))}
    choice.end = count - 1

    # Change rooms
    selection(choice)
    try:
        int(choice.answer.lower().strip())
    except ValueError:
        print("Invalid response. Please try again!")
    else:
        if int(choice.answer.lower().strip()) in list(range(choice.start, choice.end + 1)):
            choice.current_room = choice.rooms_list[index[int(choice.answer.lower().strip()) - 1]]
        else:
            print("Invalid response. Please try again!")

        print(f"New location: {choice.current_room}")


# Check objects in each room
def check_objects(choice, flag):
    try:
        int(choice.answer.lower().strip())
    except ValueError:
        print("Invalid response. Please try again!")
    else:
        # Winning condition
        if choice.current_room == choice.random_room and (int(choice.answer.lower().strip()) - 1) == choice.random_object_index:
            print(f"Congratulations! You have found the secret object [{choice.random_object}] in the [{choice.random_room}]\n")
            quit()        
        elif choice.answer.lower().strip() == str(choice.end):
            flag = True
        elif int(choice.answer.lower().strip()) in list(range(1, choice.end)):
            print("There's nothing there. Please try again")
            time.sleep(choice.delay)
        else:
            print("Invalid response. Please try again!")
        return flag


# Main
menu_options = 3
start_delay = 1
game_started = False
floor_plan = False

choice = input("Do you want to play (yes/no)? ")
choice = Choice(choice, 1, menu_options)
choice.delay = 1
create_items(choice)

while(choice.answer.lower().strip() != "quit" or floor_plan == False):    
    game_started, floor_plan = start_game(choice, start_delay, game_started, floor_plan)
