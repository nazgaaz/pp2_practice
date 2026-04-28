Completed TSIS 4: Snake Game — Database Integration & Advanced Gameplay

In this update, I extended the Snake Game project according to all required TSIS 4 tasks.

First, I added PostgreSQL database integration using psycopg2. I created two main tables: players and game_sessions. The players table stores unique usernames, and the game_sessions table stores each game result, including player_id, score, level_reached, and played_at timestamp.

Second, I implemented username entry on the main menu. The player can type a username directly in the Pygame window before starting the game. The game checks that the username is not empty before allowing the player to start.

Third, I added automatic score saving after game over. When the game finishes, the final score and reached level are returned from the game logic and saved into the PostgreSQL database using the save_score function.

Fourth, I implemented a leaderboard screen. The game fetches the Top 10 scores from the database using a SQL query with ORDER BY score DESC and LIMIT 10, then displays the results inside the Pygame window.

Fifth, I added personal best tracking. When a player starts the game, the program finds their highest previous score using MAX(score) and displays it during gameplay together with the current score and level.

Sixth, I added poison food as a new gameplay feature. Poison appears randomly on the field. If the snake eats it, the snake becomes shorter by 2 segments. If the snake length becomes 1 or less, the game ends.

Seventh, I implemented three power-ups: speed boost, slow motion, and shield. Speed boost temporarily increases the snake speed, slow motion temporarily decreases the speed, and shield protects the player from one wall, obstacle, or self-collision. I used pygame.time.get_ticks() to control power-up duration and disappearance time.

Eighth, I added obstacle blocks starting from Level 3. Obstacles are placed randomly on the field when the level increases. Food and power-ups cannot spawn on obstacle blocks. The obstacle generation keeps the center area clear so the snake is not trapped immediately.

Ninth, I added JSON settings using settings.json. The game stores and loads user preferences such as snake color, grid overlay, and sound. Settings are loaded when the game starts and saved whenever the player changes them in the Settings screen.

Tenth, I implemented multiple game screens using a state system in main.py. The project includes Main Menu, Playing, Game Over, Leaderboard, and Settings screens. The player can start the game, retry after losing, return to the menu, view the leaderboard, and change settings.

Finally, I organized the project into separate files: main.py for screens and program flow, game.py for game logic, db.py for PostgreSQL functions, config.py for JSON settings, and settings.json for saved preferences.

All required TSIS 4 features were completed: PostgreSQL schema, username entry, auto-save to database, leaderboard, personal best, poison food, timed power-ups, obstacles from Level 3, JSON settings, game screens, and GitHub-ready project structure.
