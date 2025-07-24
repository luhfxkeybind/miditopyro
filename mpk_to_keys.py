import mido
import pyautogui

NOTE_TO_KEY = {
    60: 'b',  # Pad 1
    61: 'n',  # Pad 2
    62: 'm',  # Pad 3
    63: 'k',  # Pad 4
    64: 'l',  # Pad 5
    65: 'j',  # Pad 6
    66: 'h',  # Pad 7
    67: 'g',  # Pad 8
}

DEVICE_NAME = "MPK mini"

def find_input_port():
    for name in mido.get_input_names():
        if DEVICE_NAME.lower() in name.lower():
            return name
    raise RuntimeError("MPK Mini not found")

with mido.open_input(find_input_port()) as inport:
    print("Listening for MIDI input...")
    for msg in inport:
        if msg.type == 'note_on' and msg.velocity > 0:
            key = NOTE_TO_KEY.get(msg.note)
            if key:
                print(f"Simulating key: {key}")
                pyautogui.press(key)
