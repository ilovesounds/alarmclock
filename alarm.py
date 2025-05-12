import os
import platform
import threading
import time
from datetime import datetime

# === CONFIGURATION ===
# Path to your alarm file (update if needed)
alarm_file = r"C:\Users\Soham\Downloads\alarm_fixed3.wav"

# === DETECT OS AND AUDIO LIBRARY ===
system = platform.system()

# Try to import playsound (for cross-platform) and winsound (for Windows)
try:
    from playsound import playsound
    playsound_available = True
except ImportError:
    playsound_available = False

try:
    import winsound
    winsound_available = True
except ImportError:
    winsound_available = False

# === CHECK FILE EXISTENCE ===
if not os.path.exists(alarm_file):
    print(f"Alarm sound file not found at: {alarm_file}")
    print("Please check the path and make sure the file exists.")
    exit(1)
else:
    print(f"Using alarm sound: {alarm_file}")

# === ALARM SOUND FUNCTION ===
def play_alarm_loop():
    print("Playing alarm sound in a loop. Press Enter to stop.")
    while True:
        try:
            if system == 'Windows' and winsound_available:
                winsound.PlaySound(alarm_file, winsound.SND_FILENAME)
            elif playsound_available:
                playsound(alarm_file)
            else:
                print("No suitable audio library found. Please install playsound or use Windows.")
                break
        except Exception as e:
            print("Error playing sound:", e)
            break

# === MAIN ALARM LOGIC ===
alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")
print(f"Alarm is set for {alarm_time}")

while True:
    now = datetime.now().strftime("%H:%M:%S")
    if alarm_time < now:
        print("Alarm time has already passed. Please set a new time.")
        alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")
        print(f"Alarm is set for {alarm_time}")
        continue
    if now == alarm_time:
        
        print("⏰ Time to wake up!")
        alarm_thread = threading.Thread(target=play_alarm_loop)
        alarm_thread.daemon = True
        alarm_thread.start()
        input("Press Enter to stop the alarm...\n")
        print("Alarm stopped.")
        break
    time.sleep(1)