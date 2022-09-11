import secret_object
import escape_room
import sys


while True:
    print("\nSelect an option:")
    print("1) Play Hidden Object Game")
    print("2) Play Escape Room Game")
    print("3) Quit")

    selection = input("Make your selection (1-3): ")

    if selection == "1":
        secret_object.main()
    elif selection == "2":
        escape_room.main()
    elif selection == "3":
        sys.exit()
    else:
        print("Invalid response. Please try again!")
