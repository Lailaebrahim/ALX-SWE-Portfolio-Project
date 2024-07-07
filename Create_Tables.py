from PersonalBlogWebApp import db
from run import app

def create_tables():
  """
  This function creates the necessary tables in the database for the PersonalBlogWebApp.

  It uses the SQLAlchemy `create_all()` method to create the tables based on the defined models  only if they aren't created yet.

  Note: This function should be executed once to create the tables. Subsequent executions will not create duplicate tables.
  """

  # Create an application context
  with app.app_context():
    # Check if tables already exist
    if not db.metadata.tables:
      # Create all the tables
      db.create_all()
      print("Tables created successfully.")
    else:
      print("Tables already exist.")

# Call the create_tables function to create the tables
create_tables()
