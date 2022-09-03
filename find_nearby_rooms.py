rooms_list = ["Living Room", "Bedroom", "Bathroom", "Kitchen", "Garage"]
nearby_room_index = [[1, 3], [0, 2], [1], [0, 4], [3]]
nearby_rooms = {rooms_list[i]:j for i, j in enumerate(nearby_room_index)}

room_name = rooms_list[4]

for room_name in rooms_list:
    count = 1
    print(f"\nCurrent room is [{room_name}]")
    for r in nearby_rooms.get(room_name):
        print(f"{count}) Go to {rooms_list[r]}")
        count += 1