class Choice():
    def __init__(self, answer, current_room, start, end):
        self.answer = answer
        self.current_room = current_room
        self.start = start
        self.end = end

        answer = answer.lower().strip()


# Track user's input
def selection(start, end):
    if end > 1:
        choice.answer = input(f"Make your selection ({start}-{end}): ")
    else:
        choice.answer = input(f"Make your selection ({start}): ")
    choice.start = start
    choice.end = end


# Menu screen for the 2 main actions
def select_action(choice, current_room):
    print(f"\nYou are in the {current_room}:")
    print("1) Explore the room")
    print("2) Change Locations")
    selection(1, 2)
    choice.current_room = current_room


# Menu screen for the rooms
def room(choice, rooms_list):
    room_objects = [ ["Couch", "Rug", "Plant", "TV", "Shelf"],
                     ["Bed", "Desk", "Drawer", "Lamp", "Wardrobe"],
                     ["Cabinet", "Toilet", "Basin", "Bathtub", "Towel"],
                     ["Cabinet", "Sink", "Microwave", "Oven", "Fridge"],
                     ["Tools Rack", "Car Trunk", "Spare Tire", "Boxes", "Door"], ]

    objects = {rooms_list[i]:j for i, j in enumerate(room_objects)}
    count = 1
    choice.start = 1
    choice.end = len(room_objects)

    print("\nYou find the follow objects: ")
    for r in objects.get(choice.current_room):
        print(f"{count}) {r}")
        count += 1

    selection(choice.start, choice.end)


# Find adjacent rooms
def location(choice, rooms_list):
    count = 1
    choice.end = 2
    nearby_room_index = [[1, 3], [0, 2], [1], [0, 4], [3]]
    nearby_rooms = {rooms_list[i]:j for i, j in enumerate(nearby_room_index)}

    # Display nearby locations
    print("\nWhere would you like to go?")
    for r in nearby_rooms.get(choice.current_room):
        print(f"{count}) {rooms_list[r]}")
        count += 1

    index = {i:j for i, j in enumerate(nearby_rooms.get(choice.current_room))}
    choice.end = count - 1

    # Change locations
    selection(choice.start, choice.end)
    if int(choice.answer) in list(range(choice.start, choice.end + 1)):
        choice.current_room = rooms_list[index[int(choice.answer) - 1]]
    else:
        print("\nInvalid response. Please try again!")

    print(f"New location: {choice.current_room}")


# Main
rooms_list = ["Living Room", "Bedroom", "Bathroom", "Kitchen", "Garage"]
inventory = []

# Set the room to start on. Alter this value for testing.
current_room = rooms_list[0]
game_started = False
quit_game = False
game_over = False

# Start Game
choice = input("Do you want to play (yes/no)? ")
choice = Choice(choice, current_room, 1, 2)

while(choice.answer != "quit" or quit_game != False):    
    # Start menu
    if game_started == False:
        if choice.answer == "yes":
            print(f"You have been locked in an unknown house. Find the exit!")
            game_started = True
        elif choice.answer == "no":
            print("Maybe next time. Bye")
            quit()
        else:
            print("\nInvalid response. Please try again!")
            choice.answer = input("Do you want to play (yes/no)? ")

    # Start first task        
    if game_started == True: 
        select_action(choice, current_room)
        if choice.answer == "1":
            room(choice, rooms_list)
            quit()
        elif choice.answer == "2":
            location(choice, rooms_list)
            quit()
        else:
            if choice.answer != "quit":
                print("\nInvalid response. Please try again!")
                