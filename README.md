# Personal Blog


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

## Usage


1. Register: Begin by creating an account on the platform. Fill in the required information and click on the "Register" button. You will be redirected to a confirmation page.

![Registration Page](PersonalBlogWebApp/static/landing_page/register.png)

2. Login: After registering, you can log in to your account using your credentials. Enter your username and password and click on the "Login" button. Upon successful login, you will be directed to the homepage.

![Login Page](PersonalBlogWebApp/static/landing_page/login.png)

3. Create a Blog: Once logged in, you can create a blog post. Click on the "New Post" button to start writing your blog. You can either publish it immediately or schedule it for a later date.

![New Post Page](PersonalBlogWebApp/static/landing_page/new_post.png)

4. Update or Delete Blogs: If you wish to make changes to your existing blogs, navigate to the "Update/Delete" section. Here, you can edit the content of your blog posts or delete them entirely.

![Update/Delete Page](PersonalBlogWebApp/static/landing_page/update_delete.png)

5. Update Account Information: To update your account details, go to the "Account" section. Here, you can modify your username, email address, and other personal information.

![Account Page](PersonalBlogWebApp/static/landing_page/account.png)

6. Reset Password: In case you forget your password, you can reset it by clicking on the "Forgot Password" link. Follow the instructions provided to regain access to your account.

![Reset Password Page](PersonalBlogWebApp/static/landing_page/reset_password.png)

7. Search Blogs: If you are looking for specific blog posts, you can use the search feature. Enter relevant keywords in the search bar, and the application will display matching results.

![Search Page](PersonalBlogWebApp/static/landing_page/search.png)

8. Delete Account: If you decide to delete your account, including all your posted blogs, you can do so in the "Delete Account" section. Confirm your decision, and your account will be permanently removed.

![Delete Account Page](PersonalBlogWebApp/static/landing_page/delete_account.png)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to explore the project and provide any feedback or suggestions. Thank you for your time! 😊

## Blog Post

I have written a blog post about the project titled "The print(‘Hello World!’) of web development". In this blog post, I discuss the development process and key features of the application. You can read the blog post [here](https://medium.com/@lailaebrahiem108/the-print-hello-world-of-web-development-06784e6fdb60).

Feel free to check it out and leave any comments or feedback. Thank you for your interest!