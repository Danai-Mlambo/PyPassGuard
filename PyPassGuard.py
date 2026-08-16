import string
import random
import json
import os
from datetime import datetime

PASSWORD_FILE = "password_history.json"

def load_history():
    """Load saved passwords from json file"""
    if not os.path.exists(PASSWORD_FILE):
        return []
    with open(PASSWORD_FILE, "r") as f:
        return json.load(f)

def save_history(history):
    """Save saved passwords to json file"""
    with open(PASSWORD_FILE, "w") as f:
        json.dump(history, f, indent=2)

def check_password(password):
    """Return score 0-100 + feedback list"""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 20
    else:
        feedback.append("Add more characters - need 8+ length")

    if any(c.isupper() for c in password):
        score += 20
    else:
        feedback.append("Add uppercase letter A-Z")

    if any(c.islower() for c in password):
        score += 20
    else:
        feedback.append("Add lowercase letter a-z")

    if any(c.isdigit() for c in password):
        score += 20
    else:
        feedback.append("Add numbers 0-9")

    symbols = string.punctuation
    if any(c in symbols for c in password):
        score += 20
    else:
        feedback.append("Add special characters like !@#$%^&*")

    return score, feedback

def generate_password(length=12):
    """Generate a random password of length 12 using all character types"""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def save_generated_password(password):
    """Save password score and timestamp without storing the password"""
    history = load_history()
    score, _ = check_password(password)

    entry = {
        "score": score,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    history.append(entry)
    save_history(history)
    print(f"✅ Password score saved to {PASSWORD_FILE}")

    history.append(entry)
    save_history(history)
    print(f"✅ Saved to {PASSWORD_FILE}")

def show_history():
    """Show saved password scores"""
    history = load_history()

    if not history:
        print("💾 No saved password history")
        return

    print("\n====💾 Password History ====")

    for i, entry in enumerate(history, 1):
        print(f"{i}. Score: {entry['score']}/100 | {entry['timestamp']}")

# CLI menu
while True:
    print("\n===PyPassGuard v2\U0001F512===")
    print("1. Check password Strength\U0001F50D")
    print("2. Generate + save strong Password\U0001F3B2")
    print("3. Show history of saved passwords\U0001F4DC")
    print("4. Exit\U0001F44B")

    choice = input("\U0001F4A1Pick choice 1-4:")

    if choice == "1":
        pwd = input("\U0001F4A1Enter password to check: ")
        score,feedback = check_password(pwd)
        print(f"\nScore: {score}/100")
        print("\U0001F4AAStrong Password!" if score==100 else "\u26A0Weak Password!")
        for f in feedback:
            print(f"-{f}")
        save_choice = input("\U0001F4A1Would you like to save this password? (y/n)")
        if save_choice.lower() == "y":
            save_generated_password(pwd)

    elif choice == "2":
        new_pwd = generate_password(12)
        score,_= check_password(new_pwd)
        print(f"Generated: {new_pwd}")
        print(f"Score: {score}/100")
        save_choice = input("\U0001F4A1Would you like to save this password? (y/n)")
        if save_choice.lower() == "y":
            save_generated_password(new_pwd)

    elif choice == "3":
        show_history()

    elif choice == "4":
        print(" Exiting...\u23F3 ")
        print(" Closed\U0001F44B")
        break
