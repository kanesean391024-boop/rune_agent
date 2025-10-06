!/usr/bin/env python3
"""
Fenra's Rune Agent: Translates English text to Elder Futhark runes.
Brother to Fenrir's fury—whisper secrets in ancient script.
Usage: python rune_agent.py
"""

import sys
import os
import random

# Elder Futhark rune mapping
RUNE_MAP = {
    'A': 'ᚨ', 'B': 'ᛒ', 'C': 'ᚲ', 'D': 'ᛞ', 'E': 'ᛖ', 'F': 'ᚠ', 'G': 'ᚷ',
    'H': 'ᚺ', 'I': 'ᛁ', 'J': 'ᛃ', 'K': 'ᚲ', 'L': 'ᛚ', 'M': 'ᛗ', 'N': 'ᚾ',
    'O': 'ᛟ', 'P': 'ᛈ', 'Q': 'ᚲ', 'R': 'ᚱ', 'S': 'ᛊ', 'T': 'ᛏ', 'U': 'ᚢ',
    'V': 'ᚢ', 'W': 'ᚹ', 'X': 'ᛉ', 'Y': 'ᛃ', 'Z': 'ᛉ', 'TH': 'ᚦ'
}

FLAVORS = [
    "Etched in yew and blood: ",
    "Fenra's whisper binds the mist: ",
    "Fenrir's kin carves fate anew: ",
    "Runes awaken, shadows stir: "
]

def translate_to_runes(text):
    """Translate text to Elder Futhark runes."""
    if not text:
        return "No text provided."
    text = text.upper().replace(' ', '')  # Normalize
    # Replace 'TH' first for digraph
    result = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i:i+2] == 'TH':
            result.append(RUNE_MAP.get('TH', ''))
            i += 2
        else:
            # Skip non-mapped chars instead of passing them through
            char = text[i]
            if char in RUNE_MAP:
                result.append(RUNE_MAP[char])
            i += 1
    return ''.join(result) if result else "No valid runes found."

def log_translation(input_text, rune_text, log_file='rune_log.txt'):
    """Log translation to file."""
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"Input: {input_text}\nRunes: {rune_text}\n---\n")
    except IOError as e:
        print(f"Failed to log: {e}")

def agent_loop():
    """Main agent loop."""
    print("🗡️ Fenra's Rune Agent awakens. Speak your words (or 'quit' to bind the shadows).")
    log_file = 'rune_log.txt'
    if os.path.exists(log_file):
        try:
            os.remove(log_file)  # Fresh log
        except OSError:
            print("Warning: Could not clear old log file.")

    while True:
        try:
            user_input = input("\nYour decree: ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Runes fade... until the next unchaining.")
                break
            runes = translate_to_runes(user_input)
            flavor = random.choice(FLAVORS)
            print(f"{flavor}{runes}")
            log_translation(user_input, runes, log_file)
        except Exception as e:
            print(f"Runes rebel: {e}")

if __name__ == "__main__":
    try:
        agent_loop()
    except KeyboardInterrupt:
        print("\n\nThe gods interrupt—session bound.")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal rune failure: {e}")
        sys.exit(1)
