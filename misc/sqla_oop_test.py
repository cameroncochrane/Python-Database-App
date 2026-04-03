# SQL Alchemy (OOP Approach)

import sqlalchemy as sa
from sqlalchemy.orm import Mapped,mapped_column,sessionmaker,declarative_base

db = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=db)
Base = declarative_base() # Construct a base class for declarative class definitions.


# Creating a new table as an object:

class Users(Base):
    __tablename__ = "users" # Name the table

    # Define columns:
    id: Mapped[int] = mapped_column(primary_key=True) #Make this the primary column
    username: Mapped[str]
    email: Mapped[str]

    def __repr__(self) -> str: # Table 'representation'
        return f"<Users(id={self.id},username={self.username},email={self.email})>" # Map column names to the defined columns above


# Main function which runs when the script is executed:

def main():
    Base.metadata.create_all(db) # Create the db
    user_1 = Users(username="Cameron",email="cameron@mail.com") # Define a new row for the 'User' table
    user_2 = Users(username="John",email="john@mail.com") # Define a second new row for the 'User' table

    with Session() as session:
        session.add(user_1) # Add the first row
        session.add(user_2) # Add the second row
        session.commit()
        print(session.query(Users).all())


if __name__=="__main__":
    main()
