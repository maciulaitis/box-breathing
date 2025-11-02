# Box Breathing Animation Script

## What is Box Breathing?

Box breathing (also known as square breathing) is a simple, powerful relaxation technique that involves inhaling, holding, exhaling, and holding your breath for equal counts. It is used to reduce stress, improve focus, and promote calmness. Each phase typically lasts 4 seconds, forming a "box" pattern.

## About This Script

This Python script provides a terminal-based animated guide for practicing box breathing. It visually displays each phase with a progress bar and plays distinct sounds for each step to help you stay on track. The script supports two display modes:
- **Default:** Shows a new line for each second.
- **Single-line mode:** Only one progress line is visible at a time (useful for minimal distraction).

## Usage

1. **Run the script:**
   ```bash
   python box_breathing.py
   ```

2. **Optional:** Use the `--single-line` flag for single-line animation:
   ```bash
   python box_breathing.py --single-line
   ```

3. **Stop anytime:** Press `Ctrl+C` to exit early.

## Features

- Animated progress for each breathing phase (inhale, hold, exhale, hold)
- Unique sound cues for each phase and session completion
- Cross-platform support (Windows, macOS, Linux)
- Customizable display mode

## Requirements

- Python 3.x
- On macOS: Uses built-in system sounds
- On Linux: For best sound experience, install the `beep` utility (`sudo apt-get install beep`)

## Why Use Box Breathing?

Box breathing can help:
- Reduce anxiety and stress
- Improve concentration and performance
- Promote mindfulness and relaxation

Practice daily for best results!