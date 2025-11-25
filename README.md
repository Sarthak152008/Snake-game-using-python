# Snake game using pygame

This repository contains a simple snake game written in Python and using pygame. The playable script is `main.py`.

How to run
1. Make sure you have Python 3.8+ and pip installed.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the game locally (recommended):
```bash
python main.py
```

Note about displays and containers
- If you're running this in a Linux container without a display (headless) you'll need either an X server forwarded or use `xvfb-run`:
```bash
sudo apt-get update && sudo apt-get install -y xvfb
xvfb-run -s "-screen 0 600x400x24" python main.py
```

Common issues
- If the game does not open a window, ensure your development environment has access to a display.
- If pygame fails to import, make sure you installed `pygame` from `requirements.txt`.
- If you see zero or low framerate, increase FPS in `main.py`.

Improvements made in `main.py`:
- The code was moved to `main.py` (instead of README).
- Restart now reinitialises the game without recursion.
- Food and movement are grid-aligned to the snake size to avoid collision detection mismatches.
- Wall collision checks are corrected (>= width/height).














 









