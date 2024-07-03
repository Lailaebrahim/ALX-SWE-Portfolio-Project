from flask import Flask
from PersonalBlogWebApp.config import Configuration
from PersonalBlogWebApp import db, bcrypt, login_manager, mail, scheduler
from PersonalBlogWebApp.scheduler import schedule_posts


def create_app(config_class=Configuration):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    scheduler.init_app(app)

    @scheduler.task('interval', id='schedule_posts', seconds=60)
    def scheduled_task():
        schedule_posts(app)

    scheduler.start()

    from PersonalBlogWebApp.users.routes import users
    from PersonalBlogWebApp.posts.routes import posts
    from PersonalBlogWebApp.main.routes import main
    from PersonalBlogWebApp.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
