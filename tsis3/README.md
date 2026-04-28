# TSIS 3: Racer Game — Completed Tasks

In this project, I completed the advanced Racer Game according to the “You Must Complete” requirements.

First, I added lane hazards and dynamic road events. I created random obstacles on the road, including oil spills and speed bumps. Oil spills make the player change lanes, and speed bumps slow the player down for a short time. This makes the road more challenging because the player has to choose safer lanes and react quickly.

Second, I added dynamic traffic cars and random road obstacles. Enemy cars spawn on the road and move downward. If the player collides with a traffic car, the game ends. Obstacles also appear randomly and affect the player’s movement or speed. I also added safe spawn logic, so traffic cars and obstacles do not appear directly on top of the player.

Third, I added three collectible power-ups: Nitro, Shield, and Repair. Nitro temporarily increases the player’s speed. Shield protects the player from one collision. Repair works instantly and clears one obstacle. Power-ups appear on the road and disappear after a timeout if the player does not collect them.

Fourth, I implemented difficulty scaling. The game has Easy, Normal, and Hard difficulty levels. Each difficulty changes the base speed, finish distance, traffic spawn interval, and obstacle spawn interval. On harder difficulty, the game becomes faster and more challenging.

Fifth, I created a persistent leaderboard saved to a local JSON file. The leaderboard is stored in `leaderboard.json`. It saves the player’s username, score, coins, distance, and date. The game loads the leaderboard from the file and displays only the top 10 results.

Sixth, I added username entry and a top 10 leaderboard screen. Before starting the race, the player enters a username. After the game ends, the result is saved with this username. The leaderboard screen shows the best results with rank, username, score, and distance.

Seventh, I added a settings screen with sound toggle, car color selection, and difficulty options. The player can turn sound on or off, choose the difficulty level, and change the car color. These preferences are saved and used immediately in the game.

Eighth, I implemented saving and loading settings using `settings.json`. When the game starts, it loads saved settings from the JSON file. When the player changes settings, the game saves them back to `settings.json`.

Ninth, I added all required game screens: Main Menu, Game Over, Leaderboard, and Settings. The Main Menu contains Play, Leaderboard, Settings, and Quit buttons. The Game Over screen shows score, coins, and distance, and gives the player options to retry or return to the menu.

Finally, I organized the project for GitHub with a clean file structure: `main.py`, `racer.py`, `ui.py`, `persistence.py`, `settings.json`, `leaderboard.json`, and the `assets/` folder. I separated responsibilities between files: `main.py` controls screens, `racer.py` contains gameplay logic, `ui.py` contains buttons and text drawing, and `persistence.py` handles JSON saving and loading.

Overall, I completed lane hazards, dynamic road events, traffic cars, obstacles, power-ups, difficulty scaling, persistent leaderboard, username entry, settings screen, JSON saving/loading, and all main game screens required for TSIS 3.
