# this script is used to a add a user to the database


import sys
import os

# Add the root directory to the Python path
# This allows us to import from `db` and `models`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlmodel import Session
from db import engine, init_db
from models.user import User

def create_demo_user():
    print("Initializing database...")
    init_db() # Make sure tables exist
    
    with Session(engine) as session:
        # Check if the user already exists
        user = session.exec(select(User).where(User.email == "investigator@demo.com")).first()
        
        if user:
            print("Demo user 'investigator@demo.com' already exists.")
        else:
            print("Creating demo user 'investigator@demo.com'...")
            demo_user = User(
                email="investigator@demo.com",
                name="Demo Investigator",
                role="investigator"
                # We don't save a password since login is mocked
            )
            session.add(demo_user)
            session.commit()
            print("Demo user created successfully.")

if __name__ == "__main__":
    create_demo_user()