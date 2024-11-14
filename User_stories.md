# User Stories and Acceptance Criterion Frame

Title: Each user story gets a brief name 
As a [type of user],
	•	Who is the user or role you’re focusing on? (e.g., player, admin, guest)
I want to [do something],
	•	What is the user trying to do or accomplish? (e.g., “save my game progress,” “choose a character”)
So that [I can achieve a goal or benefit].
	•	Why is this important for the user? What benefit or outcome will the user get from this feature? (e.g., “so I can continue my game later,” “so I can play as my favorite character”)


Acceptance Criteria (used to build the Definition of Done):
	•	What must happen for the user story to be complete?
	•	(e.g., “The player must be able to log in with their username and password.”)
	•	(e.g., “If login fails, the player sees an error message.”)



Instructions for Writing User Stories:
For each feature you want to create, write a new user story. After each user story, include two acceptance criteria that explain how you’ll know when that story is complete.
Do this until you have 5 user stories in total.
Make sure each story clearly describes:
Who the user is.
What the user wants to do.
Why it’s important to them.
Then, for each story, list two specific things that must happen for it to be considered "done."





Examples for Power-Up Tetris Mayhem

User Story 1: Player Starts the Game
As a player,
I want to start a new game by pressing a “Start” button,
So that I can begin playing Power-Up Tetris Mayhem and enjoy the game.
Acceptance Criteria:
	•	The player must be able to click a visible “Start Game” button.
	•	Upon clicking, the game must transition from the main menu to the gameplay screen without delay.
	•	The game screen must display a timer or score tracker as soon as the game begins.

User Story 2: Player Clears Lines in Game
As a player,
I want to clear lines by correctly positioning the falling tetrominoes,
So that I can score points and progress in the game.
Acceptance Criteria:
	•	The player must be able to complete a line when the tetrominoes fill a row without gaps.
	•	When a line is cleared, the game should update the score.
	•	The cleared lines should disappear from the grid and other blocks should fall down to fill the space.
	•	The score should be visible and updated after each line cleared.
User Story 3: Player Uses Power-Ups
As a player,
I want to collect power-ups during the game,
So that I can temporarily enhance my gameplay with special abilities.
Acceptance Criteria:
	•	Power-ups should appear at random intervals during gameplay.
	•	The player must be able to activate a power-up by pressing a designated key.
	•	Each power-up must have a unique effect, such as slowing time, clearing random blocks, or increasing score multipliers.
	•	The power-up should only last for a limited time, and its effect must be clear to the player through visual or audio cues.

User Story 4: Player Avoids Obstacle Blocks
As a player,
I want to avoid falling obstacle blocks while placing tetrominoes,
So that I don’t block my game progress and can continue to clear lines.
Acceptance Criteria:
	•	Obstacle blocks should be randomly placed on the grid and stay fixed.
	•	The player must be able to see the obstacle blocks clearly.
	•	If a tetromino touches an obstacle block, it must be prevented from moving into that space.
	•	If an obstacle blocks the path, the player should lose a life or face a penalty in the game (depending on the design decision).

User Story 5: Player Saves Game Progress
As a player,
I want to save my progress during the game,
So that I can resume playing from where I left off if I exit or pause the game.
Acceptance Criteria:
	•	The game must allow the player to save the current game state at any point during gameplay.
	•	When the player reopens the game, they must be able to resume from the saved progress, including score, level, and game grid state.
	•	The game must prompt the player with a “Save Game” option in the pause menu.

User Story 6: Player Reaches Higher Levels
As a player,
I want to progress to higher levels as I clear more lines,
So that I can face more challenging gameplay with faster falling blocks and new features.
Acceptance Criteria:
	•	The game must increase the speed at which the tetrominoes fall as the player clears a certain number of lines.
	•	New game elements, such as faster obstacle blocks or additional power-ups, should appear at higher levels.
	•	The level should be displayed clearly on the screen, updating with each level increase.
