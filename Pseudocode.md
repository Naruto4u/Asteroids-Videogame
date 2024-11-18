# Pseudocode Frame for Asteroids-like Game with Gravity and Momentum

### 1. Start: Define the beginning of the process.
```
Initialize game:
    Load assets (sprites, sounds)
    Initialize player properties (position, health, default weapon, currency, velocity = 0)
    Initialize enemies and asteroids
    Initialize shop inventory with purchasable items
    Initialize timers (slow motion, overdrive)
    Set up game boundaries and camera
```
### 2. Input: Describe what data the program will take in.
```
Player input:
    Get mouse position
    Detect left/right mouse button clicks
    Detect special key presses (e.g., for slow motion, overdrive)
    Get scroll wheel input for changing weapons
    Get player input for interacting with the shop (buy/equip items)
```
### 3. Process: Outline the steps the program will perform with the input.
```
Game loop:
    While game is running:
        # Player controls with momentum and gravity effect
        Rotate player to face the mouse cursor

        If left mouse button is pressed:
            # Apply thrust to move player towards the mouse direction
            Apply thrust vector towards mouse position
            Add current thrust to player velocity vector

        # Update player position with momentum
        If player is moving (velocity > 0):
            Update player position based on current velocity vector
            Apply gradual deceleration to simulate gliding effect (e.g., multiply velocity by a friction factor < 1)

        # Update player direction while maintaining momentum
        If mouse position changes and player is moving:
            Calculate the new direction vector towards the updated mouse position
            Gradually blend current velocity vector with new direction vector to simulate natural movement towards mouse
            Update player velocity to include the influence of new direction while maintaining existing momentum

        # Special abilities
        If special key is pressed (e.g., for slow motion):
            Activate slow motion if available
            Start slow motion timer
        If overdrive key is pressed:
            Activate overdrive mode if available
            Start overdrive timer

        # Timer logic
        If slow motion timer > 0:
            Decrease timer
        Else:
            Cancel slow motion effect and reset speed

        If overdrive timer > 0:
            Decrease timer
        Else:
            Cancel overdrive effect and revert player abilities

        # Collision detection
        Check for collisions between player and asteroids/enemies
        Check if player collects power-ups

        # Shop interaction
        If shop is accessed:
            Display shop menu
            If player has enough currency:
                Allow purchase and equip items

        # Entity updates
        Update positions of asteroids and enemies
        Ensure enemies bounce off boundaries

        # Camera update
        Center camera on player, keep enemies in game area
```
### 4. Output: State what the program will produce as a result.
```
Render game:
    Display player, asteroids, enemies, and background
    Show player HUD (health, ammo, score, current weapon, timers)
    Display shop menu when accessed
    If player health reaches zero:
        Show "Game Over" screen
        Display final score
```
### 5. End: Define the end of the process.
```
If game ends (player health reaches zero or manual exit):
    Stop game
    Display final score and prompt for restart or quit
```