import secret_object
import escape_room


while True:
    print("Select an option:")
    print("1) Play Hidden Object Game")
    print("2) Play Escape Room Game")
    print("3) Quit")

    selection = input("Make you selection (1-3): ")

    if selection == "1":
        secret_object.main()
    elif selection == "2":
        escape_room.main()
    elif selection == "3":
        quit()
    else:
        print("Invalid response. Please try again!")
