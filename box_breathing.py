import time
import os
import sys
import threading

def clear_screen():
    # Clear the terminal screen if possible
    if os.name == 'nt':
        os.system('cls')
    elif os.environ.get('TERM'):
        os.system('clear')
    else:
        # TERM not set; do not attempt to clear
        pass

def play_sound(phase_type):
    # Play a different beep/ding sound depending on phase_type and OS
    try:
        if sys.platform.startswith('win'):
            import winsound
            # Use higher frequencies and longer duration for louder, glass-like effect
            freq_map = {
                "inhale": 1800,
                "hold1": 1600,
                "exhale": 1400,
                "hold2": 1200,
                "finish": 2000
            }
            freq = freq_map.get(phase_type, 1500)
            winsound.Beep(freq, 300)
        elif sys.platform == 'darwin':
            # Use only the loudest, most glass-like system sounds
            sound_map = {
                "inhale": "Funk",
                "hold1": "Ping",
                "exhale": "Submarine",
                "hold2": "Ping",
                "finish": "Hero"
            }
            sound = sound_map.get(phase_type, "Glass")
            os.system(f'afplay /System/Library/Sounds/{sound}.aiff')
        else:
            # For Linux, recommend using beep if available for louder sound
            # Otherwise, print bell character multiple times for emphasis
            try:
                import shutil
                if shutil.which("beep"):
                    freq_map = {
                        "inhale": 1800,
                        "hold1": 1600,
                        "exhale": 1400,
                        "hold2": 1200,
                        "finish": 2000
                    }
                    dur_map = {
                        "inhale": 200,
                        "hold1": 200,
                        "exhale": 200,
                        "hold2": 200,
                        "finish": 400
                    }
                    freq = freq_map.get(phase_type, 1500)
                    dur = dur_map.get(phase_type, 200)
                    os.system(f'beep -f {freq} -l {dur}')
                else:
                    # Fallback: multiple bells for emphasis
                    bell_count = {
                        "inhale": 2,
                        "hold1": 3,
                        "exhale": 4,
                        "hold2": 5,
                        "finish": 8
                    }.get(phase_type, 2)
                    print('\a' * bell_count, end='', flush=True)
            except Exception:
                print('\a', end='', flush=True)
    except Exception as e:
        pass  # If sound fails, ignore

def animate_phase(phase_name, duration, symbol, phase_type, single_line_mode=False):
    # Play sound in a separate thread so it doesn't block the counter
    sound_thread = threading.Thread(target=play_sound, args=(phase_type,))
    sound_thread.start()
    if single_line_mode:
        print(f"{phase_name} ({duration} seconds)")
        for i in range(1, duration + 1):
            bar = symbol * i + ' ' * (duration - i)
            print(f"\r[{bar}]  {i}/{duration} seconds", end='', flush=True)
            time.sleep(1)
        print('\r' + ' ' * 40 + '\r', end='', flush=True)  # Clear the line after phase
    else:
        print(f"{phase_name} ({duration} seconds)")
        for i in range(1, duration + 1):
            bar = symbol * i + ' ' * (duration - i)
            print(f"[{bar}]  {i}/{duration} seconds")
            time.sleep(1)
        print()  # Move to next line after phase for readability

def box_breathing_cycle(duration=4, single_line_mode=False):
    phases = [
        ("Inhale", duration, "#", "inhale"),
        ("Hold", duration, "-", "hold1"),
        ("Exhale", duration, "#", "exhale"),
        ("Hold", duration, "-", "hold2")
    ]
    for phase_name, phase_duration, symbol, phase_type in phases:
        clear_screen()
        animate_phase(phase_name, phase_duration, symbol, phase_type, single_line_mode=single_line_mode)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Box Breathing Animation")
    parser.add_argument('--single-line', action='store_true', help='Show only one line at a time')
    args = parser.parse_args()

    print("Box Breathing Animation\nPress Ctrl+C to stop.\n")
    rounds = 10  # Number of cycles
    try:
        for i in range(rounds):
            print(f"Cycle {i+1}/{rounds}\n")
            box_breathing_cycle(single_line_mode=args.single_line)
        play_sound("finish")
        print("Finished!")
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()