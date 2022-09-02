def select_action(choice, room):
    print(f"1) Explore the {room}")
    print("2) Change Locations")
    choice = input("Make your selection: ")
    return choice

def living_room(living_room_objects):
    for i in range(1, len(living_room_objects) + 1):
        print(f"{i}) {living_room_objects[i - 1]}")

rooms = ["Living Room", "Bedroom", "Bathroom", "Kitchen", "Garage"]
living_room_objects = ["Couch", "Rug", "Plant", "TV", "Shelf"]
inventory = []

choice = input("Do you want to play? (yes/no) ")

if choice.lower().strip() == "yes":
    print("You have been locked in an unknown house. You are located in the Living Room. Find the exit!")
    choice = select_action(choice, rooms[0])
else:
    print("Maybe next time. Bye")

if choice.lower().strip() == "1":
    living_room(living_room_objects)
else:
    print("next")
    
