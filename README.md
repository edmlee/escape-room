# Escape Room Game

Two game modes:  
    1) Hidden Object Game  
    2) Escape Room Game  

Required Files: `secret_layout.txt`, `escape_layout.txt`, `responses.txt`  
----------------------------------
1) Hidden Object Game  (Simple)
----------------------------------
Objective: Find the secret object to win the game  

How to play:  
1. Run `secret_object.py` or select `Hidden Object Game` from the executable file  
2. Follow the instructions and input values into the terminal  
3. Type "quit" at the main menu to exit the game  
4. The game will automatically terminate upon finding the secret object  

The conditions have been randomly generated. This includes the:  
-  Starting location  
-  Room which holds the secret object  
-  Secret object itself  

The connected rooms are fixed and have not been randomly generated.  
Check the `floor_plan.png` file for more information about the room layouts. This can also be viewed in the game  

New objects can be added into the game to increase the difficulty  
The code will automatically update these new additions  

----------------------------------
2) Escape Room Game (Advanced)
----------------------------------
Objective: You are trapped in a house. Find the secret items to unlock the exit  

How to play:  
1. Run `escape-room.py`  or select `Escape Room Game` from the executable file  
2. Follow the instructions and input values into the terminal  
3. Type "quit" at the main menu to exit the game  
4. Find the secret items scattered around the house  
5. After finding all the required items, use them to escape the house  
6. The game will automatically terminate upon unlocking the exit  

Other Information:  
- This is an advanced version of the Secret Object Game but with the introduction of extra objectives  
- The starting and exit locations are pre-selected and is not randomly generated  
- When interacting with objects in the game, the response is randomly selected from a list that is loaded from "responses.txt"  
- This text file can be appended to add more custom responses  
- There will be a slight time delay when interacting with certain features of the game
- The locations of the secret items (a.k.a keys) are randomly generated  
- These keys are colour coded and are randomly selected from a list  
- The number of keys in the game can be changed to increase/decrease the game difficulty  
- Keys are stored in an inventory and can be tracked throughout the gameplay  
- The floor plan of the house can be viewed at anytime  
- The exit will remain locked unless all keys have been found  
- Different messages will be shown when interacting with the exit depending on whether it's locked or unlocked  
