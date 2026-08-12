# 🔐 PyPassGuard

PyPassGuard is a Python command-line password security tool that allows users to check password strength, generate strong passwords, and save password history locally.

## 🚀 Features

* 🔍 Check password strength
* 📊 Get a password score from 0–100
* 💡 Receive feedback on how to improve a password
* 🎲 Generate random passwords
* 💾 Save password history locally
* 📅 Store timestamps for saved passwords
* 📄 Store password history in JSON format

## 🛠️ Technologies Used

* Python
* JSON
* `random`
* `string`
* `os`
* `datetime`

## 📋 Password Strength Rules

A password receives points for:

| Requirement           | Points |
| --------------------- | -----: |
| At least 8 characters |     20 |
| Uppercase letter      |     20 |
| Lowercase letter      |     20 |
| Number                |     20 |
| Special character     |     20 |

A maximum score of **100/100** is possible.

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project directory:

```bash
cd PyPassGuard
```

Run the program:

```bash
python pypassguard.py
```

## ⚠️ Security Note

This project is intended for learning purposes.

Passwords saved by the program are stored locally in `password_history.json`. **Do not use this project to store real or important passwords.**

The password history file is excluded from Git using `.gitignore`.

## 📚 What I Learned

This project helped me practice:

* Python functions
* Conditional statements
* Loops
* Lists and dictionaries
* File handling
* JSON
* Random password generation
* Working with modules
* Command-line interfaces
* Git and GitHub

## 🔮 Future Improvements

Possible future improvements include:

* Add password hashing instead of storing passwords in plain text
* Add stronger password-generation rules
* Add password entropy calculation
* Add a graphical user interface
* Add unit tests
* Improve password history management
