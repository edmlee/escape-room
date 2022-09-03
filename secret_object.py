import random
import time

class Choice():
    def __init__(self, answer, start, end):
        self.answer = answer.lower().strip()
        self.start = start
        self.end = end


# Create all the objects in the game. Can add or remove items from the lists.
def create_items(choice):
    choice.rooms_list = ["Living Room", "Bedroom", "Bathroom", "Kitchen", "Garage"]
    choice.room_objects = [ ["Couch", "Rug", "Plant", "TV", "Shelf"],
                    ["Bed", "Desk", "Drawer", "Lamp", "Wardrobe"],
                    ["Cabinet", "Toilet", "Basin", "Bathtub", "Towel"],
                    ["Cabinet", "Sink", "Microwave", "Oven", "Fridge"],
                    ["Tools Rack", "Car Trunk", "Spare Tire", "Boxes", "Door"], ]
    
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

# Track user's input
def selection(start, end):
    time.sleep(choice.delay)
    if end > 1:
        choice.answer = input(f"Make your selection ({start}-{end}): ")
    else:
        choice.answer = input(f"Make your selection ({start}): ")
    choice.start = start
    choice.end = end


# Menu screen for the 2 main actions
def select_action(choice):
    time.sleep(choice.delay)
    print(f"\nYou are in the {choice.current_room}:")
    print("1) Explore the room")
    print("2) Change Locations")
    selection(1, 2)


# Menu screen for the objects a in a room
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
        time.sleep(choice.delay)
        selection(choice.start, choice.end)
        flag = check_objects(choice, flag)


# List connected rooms
def location(choice):
    count = 1
    print("\nWhere would you like to go?")
    for r in choice.connected.get(choice.current_room):
        print(f"{count}) {choice.rooms_list[r]}")
        count += 1

    index = {i:j for i, j in enumerate(choice.connected.get(choice.current_room))}
    choice.end = count - 1

    # Change rooms
    time.sleep(choice.delay)
    selection(choice.start, choice.end)
    try:
        int(choice.answer)
    except ValueError:
        print("Invalid response. Please try again!")
    else:
        if int(choice.answer) in list(range(choice.start, choice.end + 1)):
            choice.current_room = choice.rooms_list[index[int(choice.answer) - 1]]
        else:
            print("\nInvalid response. Please try again!")

        print(f"New location: {choice.current_room}")


# Check objects in each room
def check_objects(choice, flag):
    try:
        int(choice.answer)
    except ValueError:
        print("Invalid response. Please try again!")
    else:
        # Winning condition
        if choice.current_room == choice.random_room and (int(choice.answer) - 1) == choice.random_object_index:
            print(f"Congratulations you have found the secret object [{choice.random_object}] in the [{choice.random_room}]")
            quit()        
        if choice.answer == str(choice.end):
            flag = True
        elif int(choice.answer) in list(range(1, choice.end)):
            print("There's nothing there. Please try again")
        else:
            print("\nInvalid response. Please try again!")
        return flag


# Main
start_delay = 1
game_started = False
quit_game = False
game_over = False

choice = input("Do you want to play (yes/no)? ")
choice = Choice(choice, 1, 2)
choice.delay = 0.1
create_items(choice)

while(choice.answer != "quit" or quit_game != False):    
    # Start menu
    if game_started == False:
        if choice.answer == "yes":
            name = input("Please enter your name: ")
            print(f"Welcome to the hidden object game {name}")
            print("Find the secret object to win the game. Let's begin!")
            time.sleep(start_delay)
            game_started = True
        elif choice.answer == "no":
            print("Maybe next time. Bye")
            quit()
        else:
            print("\nInvalid response. Please try again!")
            choice.answer = input("Do you want to play (yes/no)? ")

    # Start first task        
    if game_started == True: 
        select_action(choice)
        if choice.answer == "1":
            room(choice)
        elif choice.answer == "2":
            location(choice)
        else:
            if choice.answer != "quit":
                print("\nInvalid response. Please try again!")
                