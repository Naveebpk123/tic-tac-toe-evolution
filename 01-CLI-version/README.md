# Phase 1: CLI Local Multiplayer

This is the first released phase of **Tic-Tac-Toe Evolution**.

It is a simple terminal-based Tic-Tac-Toe game for 2 local players sharing the same computer.

## Features

- 2-player local gameplay
- Runs in the terminal
- Player 1 chooses `X` or `O`
- Player 2 gets the remaining marker automatically
- Validates row and column input
- Prevents moves on already occupied spaces
- Detects wins and draws
- Offers replay after each match

## How To Run

Make sure Python is installed, then run:

```bash
python main.py
```

If you are in the project root:

```bash
cd 01-CLI-version
python main.py
```

## How To Play

1. Start the game in the terminal.
2. Player 1 chooses `X` or `O`.
3. Players take turns entering a row number (`1` to `3`) and a column number (`1` to `3`).
4. The game announces a winner or a draw.
5. Choose whether to play again.

## Example Board

```text
X|O|_
_|X|O
_|_|X
```

## File

- `main.py`: main game loop and CLI logic

## Part Of The Bigger Project

This phase is the foundation that led into the later project releases:

- Phase 2: CLI with minimax AI
- Phase 3: Tkinter GUI
- Phase 4: Full web version with local, AI, and online play
