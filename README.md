# cse210-05
## Title: Cycle Game

## Description
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.
The game starts by the player running the file in main.py file
-Players can move up, down, left and right using the:
If Player one move using the W, S, A and D keys.
If Player two move using the I, K, J and L keys.
if player's move != collision,  trail grows, this increases by a single trail as they cut corners, the longer the game and number of corners the higher/longer the trail. 
-Players try to maneuver so the opponent collides with their trail
If a player collides with their opponent's trail
-A "game over" message is displayed in the middle of the screen.
-The cycles turn white.
-Players keep moving and turning but don't run into each other.


## Project Structure
---
The project files and folders are organized as follows:
```
+-- snake               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
Name                        Assigned                                                    Email
___________________         _______________________________________________             ________________
Guillermo Quinteros         Snake, Score, Color, Food                                   qui22003@byui.edu        
Nelson Muchonji B.          Director, Game, VideoService, Keyboard, Point, Cast         bif20001@byui.edu
Erika Ramirez               Actor, KeyboardService, MoveActorsAction, Script            ramirezerika328@gmail.com
Daniel                      Action, HandleCollisionsAction, DrawActorsAction,
