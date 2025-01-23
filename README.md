# KidPet Game

## Overview
KidPet is a simple simulation game where you raise a virtual pet. Your pet can get hungry, dirty, and even sick. You must take care of it by feeding it, washing it, and curing it when it's sick. As your pet's experience points (XP) increase, it can grow into an adult. Your goal is to manage your pet's needs and ensure it stays healthy and happy!

## Requirements
- Python 3.x
- Pygame (for rendering and game logic)
- Asset files (images for the pet’s different states)

You can install the required Pygame library using the following:

```bash
pip install pygame
```

## How to Play

1. **Start the Game**:
   Simply run the `game.py` file to start the game.
   
2. **Care for Your Pet**:
   The pet will have various statuses:
   Click till the egg breaks and your creature is born!
   - **Hunger**: If hunger goes below 50, the pet will be hungry.
   - **Dirty**: If the pet becomes too dirty, it can die.
   - **Sickness**: The pet can become sick at random times, when the pet is sick it consumes double the food. You can cure it once it gets sick.

4. **Pet Interaction**:
   - Feed the pet to increase its hunger and gain XP.
   - Wash the pet to reduce dirt and gain XP.
   - Cure the pet if it's sick to make it healthy again.


## Controls

- Use the in-game UI buttons to interact with your pet.
    - **Meat button**: Increases hunger and gives you XP.
    - **Sponge button**: Reduces the pet's dirtiness and gives XP.
    - **Pill-jar button**: Cures the pet when it is sick.

## Game Structure

- **Game Class**: Manages the main game loop, screen, and pet creation.
- **KidPet Class**: Represents the pet with various attributes like hunger, dirtiness, and sickness. It handles all the logic related to the pet's needs and updates.
- **Egg Class**: Initializes the pet in its initial state.
- **UI Class**: Responsible for drawing the user interface, including hunger and XP bars.

## Running the Game

1. Clone the repository or download the files.
2. Ensure you have the required assets in the `Assets` directory.
3. Run the game by executing:

```bash
python game.py
```

Enjoy taking care of your pet!
