# 🏓 Pong Game (Python Turtle)

A classic two-player Pong game built with Python's built-in `turtle` module. Every feature lives in its own class and file, and `main.py` ties everything together.

## Features

- Two paddles (left and right player)
- Bouncing ball that speeds up after every paddle hit
- Bounce off top and bottom walls
- Live scoreboard for both players
- Ball resets to the center when a player misses

## Project Structure

```
pong_game/
├── main.py         # Entry point: sets up the screen and runs the game loop
├── paddle.py       # Paddle class: create paddle, move up/down
├── ball.py         # Ball class: move, bounce, reset
├── scoreboard.py   # Scoreboard class: score of both players
├── court.py        # Court class: draws the center line
├── controls.py     # Controls class: keyboard bindings
├── collision.py    # Collision class: wall, paddle and miss detection
└── README.md
```

## Requirements

- Python 3.6 or newer
- `turtle` (included with Python, no extra packages needed)

> On some Linux systems: `sudo apt install python3-tk`

## How to Run

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python main.py
```

## Controls

| Player | Up | Down |
|--------|----|------|
| Left | W | S |
| Right | ⬆️ Up arrow | ⬇️ Down arrow |

Click the window to close the game.

## How It Works

| Class | File | Responsibility |
|-------|------|----------------|
| `Paddle` | `paddle.py` | Creates a paddle and moves it up and down within the screen |
| `Ball` | `ball.py` | Moves the ball, bounces it and resets it after a point |
| `Scoreboard` | `scoreboard.py` | Displays and updates both scores |
| `Court` | `court.py` | Draws the dashed line in the middle |
| `Controls` | `controls.py` | Connects keys to the paddles |
| `Collision` | `collision.py` | Detects wall hits, paddle hits and missed balls |

## Ideas for Improvement

- Add a winning score (e.g. first to 10)
- Add a single-player mode with a computer opponent
- Add sound effects

## License

MIT License
