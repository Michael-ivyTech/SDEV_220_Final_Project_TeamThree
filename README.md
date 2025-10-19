# SDEV_220_Final_Project_TeamThree

Hello! This is Team Three's Final Project for our Ivy Tech course SDEV 220 (As you could guess by the name).
The goal of this project, which was made by our professor, is to create a Python application that solves a problem for a real-world business that they could use.
The project that our team is working on is to be a Django-based online ordering app for a local business named Heyerly's Bakery in Indiana. Due to this app's nature, it'll negate the need for waiting on large bulk orders in-store. This Django app is planned to be completed by 10-18-2025.


Instructions:

1. Download the Repository from GitHub by clicking the green "Code" button, and extracting the files to desired file location.

2. Open Command Prompt (Win + R, Type "cmd", Hit Enter), navigate to the folder that the project is in (Type: cd "<Your file path here>"), then type the following commands:

venv\Scripts\activate   # For Windows
source venv/bin/activate    # For Mac and Linux

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

3. Open the website in the link provided by the runserver command.

4. Sign Up with a customer account or an employee account (Employee emails end with "@heyerlysbake.com").

5. Bingo! You should be seeing a welcome screen, once setup. Go ahead and make some orders!
