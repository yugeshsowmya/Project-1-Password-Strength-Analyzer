PASSWORD STRENGTH ANALYZER

PROJECT OVERVIEW

This project is a Password Strength Analyzer built using Python.
It checks how strong a password is by performing both basic rule-based checks and advanced strength analysis using the zxcvbn library.
Additionally, it can generate a custom wordlist based on user-provided personal details for security awareness purposes.

This project was developed as part of my internship to understand password security, Python scripting, and command-line tools.

FEATURES

1.Checks password length and character types (uppercase, lowercase, digits, special characters)
2.Uses zxcvbn to estimate password strength and crack time
3.Displays clear strength results (Weak / Medium / Strong)
4.Generates a custom wordlist using name, pet name, and year
5.Supports command-line arguments using argparse
6.Allows exporting wordlists to a .txt file

TECHNOLOGIES USED

1.Python 3
2.zxcvbn library
3.argparse module
4.Command Line Interface (CLI)

PROJECT STRUCTURE

Password strength Analyzer
 - main.py
 - wordlist.py
 - requirements.txt
 - README.md
 - wordlist.txt

INSTALLATION & SETUP

1.Clone the repository or download the project folder
2.stall required dependencies:
	pip install -r requirements.txt

HOW TO RUN THE PROJECT

1.Analyze password using command line
	python main.py --password "YourPassword123!"
2.Generate wordlist and export it
	python main.py --export
3.Run in interactive mode
	python main.py

SAMPLE OUTPUT

 - Password length and character checks
 - Strength score (0–4)
 - Estimated crack time
 - Final strength label (e.g., STRONG)
 - Wordlist generated and saved as wordlist.txt

LEARNING OUTCOMES

 - Learned how password strength is evaluated
 - Gained hands-on experience with Python modules and libraries
 - Understood argument parsing using argparse
 - Improved understanding of cybersecurity basics
 - Built a real-world CLI-based Python project

AUTHOR
Sowmya S
Intern – Cybersecurity








