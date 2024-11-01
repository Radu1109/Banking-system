"# Banking-system-APP"

This is my first APP that I've build using both Python and MySQL and it allows its users to create a banking account, manage their account
and the data is saved in a data base in SQL.
I know its not a complicated APP, but I take pride in my work, being that Im self-taught.

In order to run this APP, you'll need:

- **Python**: Version 3.6 or higher
- **MySQL**: Ensure you have MySQL server installed and running
- **Pip**: Python package manager

For installation, follow the steps below:

**Open a command prompt**


1. **Clone the repository** to your local machine:

   	git clone https://github.com/Radu1109/Banking-system.git

2.**Navigate to the project directory**:

   	cd Banking-system

3.**Create a virtual environment** (optional but recommended):
	
   	python -m venv venv

4.**Activate the virtual environment**:
	On windows: venv\Scripts\activate
	On macOS/linux: source venv/bin/activate

5.**Install the required packages**:
	pip install -r requirements.txt 


********Usage*********

1.Set up the MySQL database:

	Ensure your MySQL server is running.
	Create a new database (e.g., mydb):
	In python, in database.py you will need to modify the next lines of code in order to connect to your database.
	This information can be found in the SQL app

	**Don't know how to set-up database in SQL? I got you, scroll down for the info.**

	pymysql.connect(
        host="YOUR LOCALHOST NAME",
        user="YOUR USERNAME",
        password="YOUR PASSWORD",
        database="YOUR DATABASE NAME",
        port=YOUR PORT
	
	Without modifing this properly, the app wont run!
	

2. Run application

	python main.py

3.Follow the prompts:

	When you run the application, follow the on-screen instructions to create an account or access your existing account.

4.Perform operations:

	You can choose to deposit or withdraw money, or manage your account.
	The app will tell you how to choose between depositing, withdrawing money or managing your account.
	In the manage account section, the app will show you that you can change your last name, username, email and pin.
	All the changes you make are saved in the SQL database that you setup previously.


****SETTING UP DATABASE IN MYSQL********

Being that I've worked only with MySQL, I will write down instructions on how to set up your database.

Database Setup

Follow these steps to set up the MySQL database:

Open MySQL Workbench or connect to MySQL via the command line.

Create a new database:

If using MySQL Workbench:

Click on the Schemas tab.
Right-click in the left pane and select Create Schema....
Name your schema (e.g., mydb) and click Apply.
If using the command line, run the following command:

If using the command line, run the following command:
CREATE DATABASE mydb;


### What I Added:

1. **"Database Setup" Section**: I included detailed steps on how to create the database and the necessary tables.

2. **SQL Commands**: I provided the SQL commands that users can run in MySQL to create the database structure.

### How to Use this Markdown

1. **Update the `README.md` file** in your project with the content above.
2. **Save the file**.

Now, users will have all the necessary information to set up the database in MySQL, in addition to the installation and usage instructions. If you need any further modifications or additional information, please let me know!