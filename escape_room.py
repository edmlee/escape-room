import random
import time


class Choice():
    def __init__(self, answer, start, end):
        self.answer = answer
        self.start = start
        self.end = end


# Create all the objects in the game
def create_items(choice):
    choice.rooms_list = ["Living Room", "Bedroom", "Bathroom", "Kitchen", "Garage"]
    choice.room_objects = [ ["Couch", "Rug", "Plant", "TV", "Shelf"],
                            ["Bed", "Desk", "Drawer", "Lamp", "Wardrobe"],
                            ["Cabinet", "Toilet", "Basin", "Bathtub", "Towel"],
                            ["Cabinet", "Sink", "Microwave", "Oven", "Fridge"],
                            ["Tools Rack", "Car Trunk", "Spare Tire", "Box", "Door"], ]
    choice.inventory = set()
    
    # Select which rooms are connected to each other. Check "floor_plan.png" for more info
    choice.connected_index = [[1, 3], [0, 2], [1], [0, 4], [3]]

    # Set the start and exit locations
    choice.current_room = choice.rooms_list[0]
    choice.exit_room = choice.rooms_list[4]
    choice.exit_object = choice.room_objects[4][4]

    # Link the objects to their corresponding rooms
    choice.objects = {choice.rooms_list[i]:j for i, j in enumerate(choice.room_objects)}
    choice.connected = {choice.rooms_list[i]:j for i, j in enumerate(choice.connected_index)}

    # Randomize the colours of the special keys used to unlock the exit
    special_room_objects = []
    special_room = ""
    special_object = ""
    colours = "Red, Green, Blue, Orange, Yellow, Black, White, Pink, Purple"
    colours = colours.split(", ")
    check = True
    for index, colour in enumerate(colours):
        colours[index] = colour + " Key"
    random.shuffle(colours)

    # Randomize the location of the special keys
    while len(special_room_objects) != choice.number_of_keys:
        special_room = random.choice(list(choice.objects.keys()))
        special_object = random.choice(choice.objects[special_room])
        # Special keys should not be located at the exit door. Also remove duplicates
        if (special_room != choice.exit_room and special_object != choice.exit_object and 
                [special_room , special_object] not in special_room_objects):
            special_room_objects.append([special_room, special_object])
    choice.special_keys = dict(zip(colours, special_room_objects))
    
    # Show locations of the keys. Leave as a comment
    print(choice.special_keys)


def load_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except:
        missing_file(file_name)
        quit()
    return lines


def missing_file(file_name):
    print("> Missing file required to use this feature")
    print(f"> Please import \"{file_name}\" into the same directory")


# Display layout for the floor plan
def print_layout(choice):
    for line in choice.layout:
        line = line.rstrip("\n")
        print(line)
    check_continue = input("Enter any key to continue: ")
    if check_continue.lower().strip() == "quit":
        quit()


# Start screen
def start_game(choice, game_started, floor_plan):
    if game_started == False and floor_plan == False:
        if choice.answer.lower().strip() == "yes":
            print("---")
            print("You have been locked in an unknown house. Find the exit!")
            print("Wait, what's this...? Looks like a floor plan of the building")
            print("Now we know where the exit is! Hope it's not locked though...")
            print("---")
            check_continue = input("Enter any key to continue: ")
            if check_continue.lower().strip() == "quit":
                quit()
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
            print_layout(choice)
            floor_plan = True
        elif choice.answer.lower().strip() == "no":
            floor_plan = True
        else:
            print("Invalid response. Please try again!")

    # Main menu inputs
    elif game_started == True and floor_plan == True:
        select_action(choice)
        if choice.answer.lower().strip() == "1":
            display_objects(choice)
        elif choice.answer.lower().strip() == "2":
            location(choice)
        elif choice.answer.lower().strip() == "3":
            print_layout(choice)
        elif choice.answer.lower().strip() == "4":
            show_inventory(choice)
        else:
            if choice.answer.lower().strip() != "quit":
                print("Invalid response. Please try again!")
    return game_started, floor_plan


# Track user's input
def selection(choice):
    if choice.end > 1:
        choice.answer = input(f"Make your selection ({choice.start}-{choice.end}): ")
    else:
        choice.answer = input(f"Make your selection ({choice.start}): ")


# Main menu screen
def select_action(choice):
    menu_screen = []
    menu_screen.append("Explore The Room")
    menu_screen.append("Change Locations")
    menu_screen.append("View Floor Plan")
    menu_screen.append("Open Inventory")
    count = 1

    print(f"\nYou are in the {choice.current_room}:")
    for option in menu_screen:
        print(f"{count}) {option}")
        count += 1

    selection(choice)


# Display list of objects
def display_objects(choice):
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


# Change locations
def location(choice):
    count = 1
    print("\nWhere would you like to go?")
    for r in choice.connected.get(choice.current_room):
        print(f"{count}) {choice.rooms_list[r]}")
        count += 1

    index = {i:j for i, j in enumerate(choice.connected.get(choice.current_room))}
    choice.end = count - 1

    selection(choice)
    try:
        int(choice.answer.lower().strip())
    except ValueError:
        print("Invalid response. Please try again!")
        location(choice)
    else:
        if int(choice.answer.lower().strip()) in list(range(choice.start, choice.end + 1)):
            choice.current_room = choice.rooms_list[index[int(choice.answer.lower().strip()) - 1]]
        else:
            print("\nInvalid response. Please try again!")
            location(choice)
        print(f"New location: {choice.current_room}")


# Check objects in each room
def check_objects(choice, flag):
    try:
        int(choice.answer.lower().strip())
    except ValueError:
        print("Invalid response. Please try again!")
    else:
        # Go back to the previous menu
        if choice.answer.lower().strip() == str(choice.end):
            flag = True
        elif int(choice.answer.lower().strip()) in list(range(1, choice.end)):
            current_object = choice.objects[choice.current_room][int(choice.answer.lower().strip()) - 1]
            # Display special messages when interacting with the exit door
            if choice.current_room == choice.exit_room and current_object  == choice.exit_object:
                if len(choice.inventory) != choice.number_of_keys:
                    print("---")
                    print("This must be the exit marked on the map")
                    print("But it seems to be locked...")
                    print(f"There's {choice.number_of_keys} coloured padlocks on the door")
                    print("Looks like you'll need to search around the house for these special keys")
                    print("Let's go back...")
                    print("---")
                    check_continue = input("Enter any key to continue: ")
                    if check_continue.lower().strip() == "quit":
                        quit()
                else:
                    print("---")
                    print("Looks like you have all the keys needed to open this door")
                    print("You carefully insert all the keys to their corresponding padlocks")
                    print("You hear a click sound and the door slams wide open")
                    print("Finally... Now it's time to go back home...")
                    print("Congratulations! You have successfully escaped. Thank you for playing!")
                    print("---")
                    quit()
            # Check for special keys
            if [choice.current_room, current_object] in choice.special_keys.values():
                    print(f"Found special item [{0}]")
                    choice.sleep(3)

            # Dislay a random message for other interactions
            else:
                response = random.choice(choice.responses)
                print(response.rstrip("\n"))
            # time.sleep(choice.delay)
        else:
            print("Invalid response. Please try again!")
        return flag


def show_inventory(choice):
    print("Current items in your inventory:")
    if len(choice.inventory) > 0:
        for item in choice.inventory:
            print(item)
    else:
        print("None")
    time.sleep(choice.delay)
        


# Main
game_started = False
floor_plan = False
file_escape_layout = "escape_layout.txt"
file_responses = "responses.txt"

choice = input("Do you want to play (yes/no)? ")
choice = Choice(choice, 1, 3)
choice.layout = load_file(file_escape_layout)
choice.responses = load_file(file_responses)
random.shuffle(choice.responses)
choice.delay = 0
# choice.delay = 3
choice.number_of_keys = 3
choice.locked = True
choice.objects_found = False

create_items(choice)

while(choice.answer.lower().strip() != "quit"):    
    game_started, floor_plan = start_game(choice, game_started, floor_plan)
