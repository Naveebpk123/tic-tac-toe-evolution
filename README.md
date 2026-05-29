# Tic-Tac-Toe Evolution

A Python Tic-Tac-Toe project that grows in phases from a simple terminal game into a fuller game experience.

- Repository: [Naveebpk123/tic-tac-toe-evolution](https://github.com/Naveebpk123/tic-tac-toe-evolution)
- Author: Naveeb Pacheerikkuth

## Current Release

Phase 1 is the current public release.

This version is a local 2-player CLI Tic-Tac-Toe game where two people can play on the same computer through the terminal.

## Current Development

Phase 2 is now being rebuilt on the `feature/minimax` branch.

This phase adds a minimax-based AI opponent while keeping the CLI version available.

## Project Roadmap

### Phase 1: CLI Local Multiplayer
- Status: Released
- Two local players
- Terminal-based gameplay
- Marker selection (`X` or `O`)
- Input validation for rows and columns
- Win and draw detection

### Phase 2: CLI With Minimax AI
- Status: In progress
- Play against a minimax-based AI opponent
- Keep the CLI experience while adding single-player mode

### Phase 3: Tkinter GUI
- Status: Planned
- Desktop graphical interface using Tkinter
- Easier interaction and cleaner visual gameplay

### Phase 4: Full Website
- Status: Planned
- Local browser-based play
- Play against minimax AI
- Online multiplayer support

## Project Structure

```text
tic-tac-toe-evolution/
|- .gitignore
|- 01-CLI-version/
|- 02-minimax-version/
|- LICENSE
|- README.md
```

## Phase Guides

- [Phase 1 README](./01-CLI-version/README.md)
- [Phase 2 README](./02-minimax-version/README.md)

## Running The Current Release

Phase 2 is the current release

```bash
cd 01-CLI-version
python main.py
```

## Tech Stack

- Python
- Command-line interface

## License

This project is licensed under the terms of the [LICENSE](./LICENSE).

## Notes

This repository is being built and published step by step so each phase reflects real progress over time.
