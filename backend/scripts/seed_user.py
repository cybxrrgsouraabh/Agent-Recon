# this script is used to a add a user to the database


import sys
import os

# Add the root directory to the Python path
# This allows us to import from `db` and `models`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlmodel import Session, select
from db import engine, init_db
from models.user import User

def create_demo_user():
    print("Initializing database...")
    init_db() # Make sure tables exist
    

    demo_email = "investigator@demo.com"
    demo_name = "Sourabh"
    with Session(engine) as session:
        # Check if the user already exists
        user = session.exec(select(User).where(User.email == demo_email)).first()
        
        if user:
            print("Demo user {demo_email} already exists.")
        else:
            print("Creating demo user 'investigator@demo.com'...")
            demo_user = User(
                email=demo_email,
                name=demo_name,
                role="investigator"
                # We don't save a password since login is mocked
            )
            session.add(demo_user)
            session.commit()
            print("Demo user created successfully.")

if __name__ == "__main__":
    create_demo_user()