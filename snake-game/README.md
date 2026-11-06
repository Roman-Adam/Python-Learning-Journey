# 🐍 Snake Game (Python Turtle)

A classic Snake game built with Python's built-in `turtle` module. The project is split into small, single-responsibility classes, each in its own file, and `main.py` ties everything together.

## Features

- Create and grow a snake body
- Smooth snake movement
- Arrow-key controls (the snake can't reverse into itself)
- Food spawning at random positions
- Live scoreboard
- Game over on wall collision
- Game over on tail collision

## Project Structure

```
snake_game/
├── main.py         # Entry point: sets up the screen and runs the game loop
├── snake.py        # Snake class: create body, move, extend
├── controls.py     # Controls class: arrow-key bindings
├── food.py         # Food class: spawn food, detect collision with food
├── scoreboard.py   # Scoreboard class: score display and game over text
├── wall.py         # Wall class: detect collision with wall
├── tail.py         # Tail class: detect collision with tail
└── README.md
```

## Requirements

- Python 3.6 or newer
- `turtle` (included with the standard Python installation, no extra packages needed)

> On some Linux systems you may need to install Tkinter first:
> `sudo apt install python3-tk`

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. Start the game:
   ```bash
   python main.py
   ```

## How to Play

| Key | Action |
|-----|--------|
| ⬆️ Up | Move up |
| ⬇️ Down | Move down |
| ⬅️ Left | Move left |
| ➡️ Right | Move right |

- Eat the orange food to grow and earn points.
- Avoid hitting the walls and your own tail.
- When the game ends, click the window to close it.

## How It Works

| Class | File | Responsibility |
|-------|------|----------------|
| `Snake` | `snake.py` | Builds the snake from square segments and moves them so each follows the one ahead |
| `Controls` | `controls.py` | Listens for key presses and changes the snake's heading |
| `Food` | `food.py` | Places food randomly and checks if the head is close enough to eat it |
| `Scoreboard` | `scoreboard.py` | Displays and updates the score, shows "GAME OVER" |
| `Wall` | `wall.py` | Checks whether the head has crossed the screen boundary |
| `Tail` | `tail.py` | Checks whether the head has hit any body segment |

## Ideas for Improvement

- Save and display a high score
- Restart option after game over
- Increase speed as the score grows
- Add sound effects

## License

This project is open source and available under the [MIT License](LICENSE).
