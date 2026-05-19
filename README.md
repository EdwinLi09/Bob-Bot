# Bob's Discount Furniture: A Turtle Adventure

A surreal interactive fiction game built in Python using the `turtle` graphics module. You wake up in a dark, unfamiliar room with no memory of how you got there. A robot named **BobBot** (designation X AE A-12) introduces itself, turns the lights on, and ushers you through a doorway — straight into Bob's Discount Furniture, where things take a turn.

Part text adventure, part live-drawn cartoon, part existential crisis.

## Story

The game unfolds in three acts:

1. **The Dark Room.** You wake up. BobBot greets you, asks your name, and runs a "parametric analysis" before restoring power to your chambers. The room is drawn around you in real time.
2. **The Showroom.** You step through the door and meet Bob himself (rendered as a stick figure). Bob is determined to sell you furniture — a sofa, a chair, or a table — each one drawn on screen as you browse, complete with a pitch lifted straight from Bob's Discount Furniture advertising.
3. **The Ejection.** After you pay (with the exact amount of money that mysteriously appears in your wallet), Bob walks you to the door. The door does not lead where you expect.

## Features

- Live turtle graphics: the room, the furniture, and the stick-figure salesman are all drawn on screen as the story progresses
- Branching dialogue that loops until you give a valid response, so you can't soft-lock yourself
- Three drawable furniture items: sofa, chair, and table
- Fullscreen black-background presentation for maximum dramatic effect
- A name-personalized ending you probably weren't expecting

## Requirements

- Python 3
- The `turtle` module (included in Python's standard library, requires Tk)

## Running the Game

The project uses a small driver script that sets up the fullscreen turtle screen and loads the game module:

```bash
python driver.py game.py
```

The driver opens a fullscreen turtle window, then drops you into an interactive Python REPL while the game runs. Close the window or exit the REPL to end the session.

## File Structure

| File | Purpose |
|------|---------|
| `driver.py` | Sets up the turtle screen in fullscreen mode, loads the game module, and opens an interactive REPL. |
| `game.py` | The game itself — story, prompts, and all the drawing routines (`room`, `draw_chair`, `draw_table`, `draw_sofa`, `draw_stick_figure`). |

## How to Play

The game runs in the terminal where you launched it. Read each prompt, type your response, and watch the turtle window for visuals.

- When BobBot asks what you want to do, try **"open"** (the door).
- When Bob asks what you'd like to buy, try **"sofa"**, **"chair"**, or **"table"**.
- Answer **"yes"** or **"no"** when Bob asks if you want to purchase something.

The game will gently nudge you back on track if it doesn't understand your input.

## Notes

- The game file is named `game.py`, which shadows Python's built-in `turtle` module if you try to run it directly from its own directory without the driver. Running it via `driver.py` (which imports turtle first) avoids this.
- Drawing speed is set to instant for most operations, with brief slowdowns during furniture drawing for dramatic flair.
- All text output uses `time.sleep()` pacing so the story has room to breathe — be patient between prompts.

## Credits

Created as a creative-coding project. Bob's Discount Furniture product descriptions are paraphrased from the real chain's marketing copy. No actual furniture was harmed (or sold) in the making of this game.
