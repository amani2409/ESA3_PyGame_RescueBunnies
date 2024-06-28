# Rescue Bunnies
Rescue Bunnies is a small 2D indigame. You are playing a bunny who needs to catch all the bunnies in the level within a given time and bring them to there house.
You can only catch one bunny.
If you are faster you will get a better score. 

## Requirements
- Python 3.x
- Pygame
- SQLite

## Controls
### Login Screen:
  - Enter your username and password to login or for creating a new profil

### Start Menu:
  - You can see your total highscore
  - Press 'h' to see the global highscore
  - Press 's' to start the game - you will continue at the last stopped level
  - Press 'r' to reset your highscore and level. Now you can beginn again
  - Press 'q' to quit the game

### Highscore:
  - You can see the top 10 of player with the highest score
  - Press 'b' to go back to the start menu

### Game:
  - For navigating:
    - Press 'd' to move to the right side
    - Press 'a' to move to the left side
    - Press 'g' when you collide with a NPC Bunny to catch it
    - Then move with the bunny to the house
    - Press 'w' to release it
    - Press 'esc' if you want to end this game, you will then get to the start menu

### End/Lost Screen:
  - if you didn't rescued all the bunnies within the given time you can try it again, otherwise you won't go to the next level
  - Press 'r' to restart the game
  - Press 'h' to return to the start menu
  - Press 'q' to quit the game

## File Overview:
  - **main.py:** Runs the game. It also contains the switch of the screens and keyinputs for the screens 
  - **database.py:** Initialzing the database, creates the database, creates a user or get the needed user, updating and getting the highscore and level, resetting highscore and level
  - **game.py:** Game logic
  - **levels.py:** Contains the diverent levels 
  - **screen.py:** Draws all the needed screens (e.g. start_menu, login, endScreen, but not the level)
  - **directory: classes:**
      - **character.py:** Creating the player and the NPC bunnies
      - **spritesheet.py:** Creates the sprites for the player and NPC bunnies
      - **variables.py:** For constants and variables which are needed in other files
