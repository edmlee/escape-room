rooms_list = ["Living Room", "Bedroom", "Bathroom", "Kitchen", "Garage"]
room_objects = [ ["Couch", "Rug", "Plant", "TV", "Shelf"],
                 ["Bed", "Desk", "Drawer", "Lamp", "Wardrobe"],
                 ["Cabinet", "Toilet", "Basin", "Bathtub", "Towel"],
                 ["Cabinet", "Sink", "Microwave", "Oven", "Fridge"],
                 ["Tools Rack", "Car Trunk", "Spare Tire", "Boxes", "Door"], ]

objects = {rooms_list[i]:j for i, j in enumerate(room_objects)}
room_name = rooms_list[1]

for room_name in rooms_list:
    count = 1
    print(f"\nCurrent room is: [{room_name}]")
    for r in objects.get(room_name):
        print(f"{count}) {r}")
        count += 1