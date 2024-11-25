import logging
from models import User  # Import the User class
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# Database connection
DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/wincon"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# CRUD operations for User table

# Create
def create_user(name, email, is_admin=False):
    new_user = User(ne=name, email=email, isadmin=is_admin)
    session.add(new_user)
    session.commit()
    print(f"User '{name}' created successfully!")

# Read
def read_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.idxuser}, Name: {user.ne}, Email: {user.email}, Admin: {user.isadmin}")

# Update
def update_user(user_id, new_name=None, new_email=None):
    user = session.query(User).filter_by(idxuser=user_id).first()
    if user:
        if new_name:
            user.ne = new_name
        if new_email:
            user.email = new_email
        session.commit()
        print(f"User ID {user_id} updated successfully!")
    else:
        print(f"User ID {user_id} not found.")

# Delete
def delete_user(user_id):
    user = session.query(User).filter_by(idxuser=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User ID {user_id} deleted successfully!")
    else:
        print(f"User ID {user_id} not found.")

# Test the CRUD operations
if __name__ == "__main__":
    # Create a user
    create_user("John Doe", "john.doe@example.com")

    # Read all users
    print("All users:")
    read_users()

    # Update a user
    update_user(1, new_name="Jane Doe")

    # Delete a user
    delete_user(1)
