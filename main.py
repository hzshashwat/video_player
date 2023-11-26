import RPi.GPIO as GPIO
import webbrowser

# Define the file paths
file_paths = ["/home/pi3/link/data/box1.txt", "/home/pi3/link/data/box2.txt", "/home/pi3/link/data/box3.txt", "/home/pi3/link/data/box4.txt"]

# Define the GPIO pins for buttons
button_pins = [17, 18, 22, 23]

def setup():
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set up button pins as inputs with pull-down resistors
    for pin in button_pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def play_youtube_video(file_path):
    try:
        with open(file_path, 'r') as file:
            youtube_link = file.read().strip()
            webbrowser.open(youtube_link)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def button_callback(channel):
    file_path = file_paths[channel - 17]  # Adjust if button_pins start from a different value
    play_youtube_video(file_path)

def main():
    setup()

    # Add event detection for each button
    for pin in button_pins:
        GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback, bouncetime=300)

    try:
        print("Press Ctrl+C to exit...")
        while True:
            # Keep the program running
            pass
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up GPIO
        GPIO.cleanup()

if __name__ == "__main__":
    main()
