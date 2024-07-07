# [Personal Blog]


## Introduction

This is the final project for the Software Engineering Foundations Phase of ALX Software Engineering Course. It showcases the knowledge and skills I have acquired over the span of 9 months.

- **Deployed Site:** [Personal Blog](http://www.personalblog.lailaebrahim.tech/Landing-Page)
- **Author:**
  - [Laila Ebrahim] - [My LinkedIn](www.linkedin.com/in/laila-ebrahim-574890241)

### Project Overview

In this project, I have implemented a web application using the Flask framework. The application allows users to create an account, log in, and perform various actions such as creating, updating, and deleting posts. It also includes features like user authentication, password reset, and email notifications.

### Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python with Flask
- Database: MySQL
- ORM: SQLAlchemy

### Web Infrastructure

I have established a robust web infrastructure for my project, implementing the following components:

- Nginx serves as a reverse proxy in front of the Gunicorn WSGI application server.
- Acting as a proxy server, Nginx listens to client requests on port 80. It efficiently serves static files and seamlessly forwards dynamic requests to port 8000 through the proxy pass mechanism.
- Gunicorn, functioning as an application server, listens for proxied requests on port 8000. It then dutifully forwards these requests to the Flask application.
- The Flask application executes essential back-end logic, interacts with the database, and skillfully renders templates.
- Once the response is processed, Gunicorn promptly returns it to Nginx, which in turn sends it back to the client.

This meticulously designed setup ensures the efficient handling of client requests and facilitates seamless communication between the various components of the web application.

Additionally, I deployed my project on the server and domain provided by ALX.


## Installation 

This section provides detailed instructions for setting up the project environment and running the application locally.

### Prerequisites

- Python 3.x
- MySQL Server
- Git

### Setup Process
1. Clone the repository to your local machine:
  ```
  git clone https://github.com/Lailaebrahim/ALX-SWE-Portfolio-Project.git
  ```
2. Navigate to the project directory:
  ```
  cd ALX-SWE-Portfolio-Project
  ```
3. Create and activate a Python virtual environment:
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  ```
4. Install the necessary dependencies:

  ```
  pip install -r requirements.txt
  ```

5. Database Setup:

- Ensure that MySQL server is installed on your machine and that the root user has been created.

- Run the script "Create_Test_DB_User.sql" using the root user. This script will create a test database  and a test databse user:

  ```
  mysql -u root -p < Create_Test-DB_User.sql
  ```

- Next, run the script "Create_Tables.py" using Python. This script will create the necessary tables in the database:

  ```
  python Create_Tables.py
  ```

6. Create Create a JSON configuration file with the following structure:

```
{
  "SECRET_KEY": "your_app_secret_key_here",
  "SQLALCHEMY_DATABASE_URI": "mysql+mysqlclient://TestPersonalBlog:TestPersonalBlogPwd@localhost/TestPersonalBlogDB",
  "MAIL_SERVER": "smtp.gmail.com",
  "MAIL_PORT": 587,
  "MAIL_USERNAME": "youremail@example.com",
  "MAIL_PASSWORD": "youremail_password_here"
}
```

- Update the PersonalBlogWebApp/config.py file with the path to your configuration file:

```
with open('path/to/your/configuration/file') as f:
  config = json.load(f)
```
7. Run the Application, Start the Flask development server:

```
python run.py
```

8. Open your web browser and visit [http://localhost:5000](http://localhost:5000) to view the application.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


Feel free to explore the project and provide any feedback or suggestions. Thank you for your time! 😊
