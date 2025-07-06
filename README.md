Password Strength & Breach Checker

A Python-based command-line tool that checks the strength of a user's password based on common security rules and verifies if the password has been exposed in real-world data breaches 
using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords).

---

Weak or reused passwords are one of the most common causes of security breaches. 
This tool helps you evaluate and improve your password hygiene using industry best practices and real-world breach data.

---

Features:

Minimum length check (12 characters)
+ Checks for:
  - At least 2 uppercase letters
  - At least 4 lowercase letters
  - At least 3 digits
  - At least 3 special characters
+ Uses `pwnedpasswords` API to check for data breaches
+ Provides password strength rating: **Weak**, **Moderate**, or **Strong**
+ Suggests improvements to insecure passwords
+ Looping option to check multiple passwords

---

Requirements
Python 3.6+
`pwnedpasswords` Python library

---

Usage: 
+ Install the library (if you haven’t already):
bash
pip install pwnedpasswords

+ Run the file:
bash
python password_checker.py


---


Made with Python by DonieRad (Dorota Radecka)
If you found this useful, feel free to star the repo!
