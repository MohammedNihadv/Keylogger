# Keylogger
 
# Keylogger with Keystrokes, Screenshots, and Audio Recording

This project is an advanced keylogger that records keystrokes, takes screenshots, and records audio. It is intended for ethical use cases, such as security monitoring and testing, within the bounds of legality and user consent.

## Features

- **Keystroke Logging**: Records all keystrokes to a log file.
- **Screenshot Capture**: Takes screenshots at regular intervals.
- **Audio Recording**: Continuously records audio until the `Esc` key is pressed.
- **Stop Condition**: Pressing the `Esc` key stops all activities (keylogging, screenshot capturing, audio recording).

## Requirements

- Python 3.6+
- Required Python libraries: `pynput`, `Pillow`, `pyaudio`

## Setup

1. **Clone the Repository**: 

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Required Libraries**: 

    Make sure you are in a virtual environment or use the `--user` flag to install packages without needing administrative rights.

    ```bash
    pip install pynput Pillow pyaudio
    ```

3. **Directory Structure**: Ensure the following directories exist:

    - `screenshots`: To store the captured screenshots.
    - `audio`: To store recorded audio files.

    These directories will be created automatically by the script if they do not exist.

## Usage

1. **Run the Script**:

    Run the Python script using:

    ```bash
    python keylogger.py
    ```

2. **Stopping the Script**:

    - Press the `Esc` key to stop the keylogger, screenshot capturing, and audio recording.
    - This will finalize and save the current audio recording, stop taking screenshots, and exit the program.

3. **Viewing Logs and Captures**:

    - **Keystrokes Log**: All recorded keystrokes are saved in `key_log.txt`.
    - **Screenshots**: Saved in the `screenshots` directory, with filenames including the timestamp of capture.
    - **Audio Recordings**: Saved in the `audio` directory, with filenames including the timestamp of when recording started.

## Code Overview

- `on_press` and `on_release` functions handle keystroke logging and stopping conditions.
- `capture_screenshots(interval=5)`: Takes a screenshot every 5 seconds. Adjust the interval as needed.
- `record_audio()`: Starts continuous audio recording. Stops when the `Esc` key is pressed.

## Notes

- **Ethical Usage**: This tool should only be used for ethical purposes, with the knowledge and consent of those being monitored.
- **Performance Considerations**: Prolonged use of audio recording and frequent screenshots can consume considerable resources. Adjust the screenshot interval and manage audio file sizes as needed.

## Disclaimer

This tool is provided for educational and ethical purposes only. The author is not responsible for any misuse of this software. Always ensure you have permission to monitor devices and follow applicable laws and regulations.

