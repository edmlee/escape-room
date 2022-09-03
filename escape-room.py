class Choice():
    def __init__(self, answer, current_room, start, end):
        self.answer = answer
        self.current_room = current_room
        self.start = start
        self.end = end

        answer = answer.lower().strip()


# Track user's input
def selection(start, end):
    choice.answer = input(f"Make your selection ({start}-{end}): ")
    choice.start = start
    choice.end = end
    return choice


# Menu screen for the 2 main actions
def select_action(choice, current_room):
    print(f"You are in the {current_room}:")
    print("1) Explore the room")
    print("2) Change Locations")
    selection(1, 2)
    choice.current_room = current_room
    return choice


# Menu screen for the rooms
def room(choice, room_objects):
    choice.start = 1
    choice.end = len(room_objects)
    for i in range(choice.start, choice.end + 1):
        print(f"{i}) {room_objects[i - 1]}")
    selection(choice.start, choice.end)
    return choice


def location(choice, rooms_list):
    count = 1
    choice.end = 2
    nearby_room_index = [[1, 3], [0, 2], 1, [0, 4], 3]
    nearby_rooms = {rooms_list[i]:j for i, j in enumerate(nearby_room_index)}
    for r in nearby_rooms.get(choice.current_room):
        print(f"{count}) Go to {rooms_list[r]}")
        count += 1



# Main
rooms_list = ["Living Room", "Bedroom", "Bathroom", "Kitchen", "Garage"]
living_room_objects = ["Couch", "Rug", "Plant", "TV", "Shelf"]
inventory = []
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
            room(choice, living_room_objects)
            quit()
        elif choice.answer == "2":
            location(choice, rooms_list)
            quit()
        else:
            if choice.answer != "quit":
                print("\nInvalid response. Please try again!")