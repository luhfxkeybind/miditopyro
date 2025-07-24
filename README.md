# 🎹 MPK Mini to Roblox MIDI Bridge

This project bridges an **Akai MPK Mini** (or any MIDI controller) to **Roblox** using Python and Luau. It simulates key presses based on MIDI input so you can trigger in-game events like spotlights, effects, or anything else with real hardware.

> ✅ Built for Mac, works on Windows too.  
> 🎯 No external apps needed (pure Python solution).  
> 🔌 Pads = key presses = Roblox input detection.

---

## 🧰 Features

- Plug-and-play with **MPK Mini pads** (MIDI notes 60–67)
- Python-based MIDI input detection
- Simulates keyboard keys Roblox can detect
- Works with any Luau script using `UserInputService`
- Expandable to support more MIDI notes and modes

---

## 🔧 Requirements

- Python 3.8+
- Akai MPK Mini (or any MIDI controller)
- Roblox Studio
- macOS or Windows

---

## 📦 Installation

### 1. Clone or download this repo

```bash
git clone https://github.com/yourusername/mpk-mini-roblox-bridge.git
cd mpk-mini-roblox-bridge
