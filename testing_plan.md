# Testing Plan

**Team Members**:
- Joseph Danik
- Luca Beam

---

## Part 1: Unit Testing the Game Mechanics

### Description:
Unit tests ensure that specific game mechanics work as expected. These tests isolate features like player movement, rotation, shooting, and interactions with asteroids and enemy ships.

### Test Cases:
1. **Player Movement**:
   - **Test Data**: Move the mouse cursor and press the left mouse button.
   - **Expected Outcome**: The player ship rotates to face the mouse cursor and moves toward it smoothly while the left mouse button is held.

2. **Player Rotation**:
   - **Test Data**: Moving the mouse cursor to various positions on the screen.
   - **Expected Outcome**: The player ship always points directly at the current mouse position.

3. **Weapon Firing**:
   - **Test Data**: Pressing the right mouse button.
   - **Expected Outcome**: A projectile is created, travels in the direction the player is facing, and damages enemies or asteroids upon collision.

4. **Overdrive Activation**:
   - **Test Data**: Pressing the `Space` key when overdrive is available.
   - **Expected Outcome**: Overdrive activates, increasing the player's speed or fire rate temporarily, with a clear visual or audio cue.

---

## Part 2: Logic Testing the Game Rules and Calculations

### Description:
Logic tests ensure that game rules and calculations, such as scoring, coin drops, and power-up effects, function as intended.

### Test Cases:
1. **Scoring**:
   - **Test Data**: Destroying an asteroid or enemy ship.
   - **Expected Outcome**: The score increases appropriately (e.g., +50 for an asteroid, +100 for a ship).

2. **Coin Drops**:
   - **Test Data**: Destroying asteroids and enemy ships.
   - **Expected Outcome**: 
     - Asteroids drop coins consistently (e.g., a single coin per asteroid).
     - Enemy ships rarely drop coins (e.g., 10% chance per ship).

3. **Overdrive Cooldown**:
   - **Test Data**: Pressing the `Space` key multiple times.
   - **Expected Outcome**: Overdrive can only activate when the cooldown is complete. Attempts during cooldown display a message or visual feedback.

---

## Part 3: Boundary Testing (Edge Cases and Limits)

### Description:
Boundary tests check the game’s functionality under extreme or unusual conditions.

### Test Cases:
1. **Maximum Coin Collection**:
   - **Test Data**: Collecting coins until the maximum value is reached.
   - **Expected Outcome**: The game continues to track coins without crashing or resetting.

2. **Player Boundary Movement**:
   - **Test Data**: Moving the player beyond the screen edges.
   - **Expected Outcome**: The player wraps around to the opposite side of the screen.

3. **Overdrive Activation During Full Speed**:
   - **Test Data**: Activating overdrive when the player is already moving at maximum speed.
   - **Expected Outcome**: Overdrive applies additional benefits (e.g., fire rate increase) without breaking the game physics.

---

## Part 4: Integration Testing

### Description:
Integration tests ensure that different game components work together as intended.

### Test Cases:
1. **Gameplay and Scoring**:
   - **Test Data**: Destroying multiple asteroids and enemy ships while moving and firing.
   - **Expected Outcome**: Score increases appropriately, and coins drop from asteroids or ships as designed.

2. **Overdrive and Collision Interaction**:
   - **Test Data**: Activating overdrive and colliding with an asteroid or enemy.
   - **Expected Outcome**: Overdrive effect remains active, but the collision damages the player.

3. **Shop and Coins**:
   - **Test Data**: Collecting coins from destroyed asteroids and purchasing upgrades from the shop.
   - **Expected Outcome**: Coins decrease appropriately, and purchased items are equipped.

---

## Part 5: Handling Bad Input and Run-Time Errors

### Description:
These tests verify that the game handles unexpected inputs or errors gracefully.

### Test Cases:
1. **Invalid Key Presses**:
   - **Test Data**: Pressing unassigned keys (`Q`, `Z`, etc.).
   - **Expected Outcome**: The game ignores unassigned inputs without crashing or misbehaving.

2. **Overdrive Spam**:
   - **Test Data**: Pressing the `Space` key repeatedly during cooldown.
   - **Expected Outcome**: The game ignores the input during cooldown and provides clear feedback (e.g., a sound or visual message).

3. **Coin Overflow**:
   - **Test Data**: Collecting more coins than the maximum possible value.
   - **Expected Outcome**: The game caps the coin count without crashing or resetting values.

---

## Part 6: Summary Table

| **Test Case**                | **Test Data**                                  | **Expected Outcome**                                   |
|------------------------------|-----------------------------------------------|------------------------------------------------------|
| Player Movement              | Move mouse, press left mouse button           | Ship faces mouse and moves toward it smoothly.       |
| Weapon Firing                | Press right mouse button                      | Projectile fires in the correct direction.           |
| Overdrive Activation         | Press `Space` key                             | Overdrive activates with clear feedback.             |
| Scoring                      | Destroy asteroids or enemy ships              | Score increases correctly (+50 for asteroid, +100 for ship). |
| Coin Drops                   | Destroy asteroids or ships                    | Asteroids drop coins consistently; ships rarely do.  |
| Overdrive Cooldown           | Press `Space` repeatedly during cooldown      | Input ignored with visual/audio feedback.            |
| Player Boundary Movement     | Move ship beyond screen edges                 | Ship wraps to opposite side of the screen.           |