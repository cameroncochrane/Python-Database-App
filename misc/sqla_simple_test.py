# SQL Alchemy (Simple Approach)

import sqlalchemy as sa

# Create an engine and then connect to it:
engine = sa.create_engine("sqlite:///:memory:") # An 'engine' is the 'home-base' for the database and its API. Can connect to internet DB or a local one. Add 'echo=True' to output db messages/details.
connection = engine.connect()

# Define the schema of the DB via a metadata object:
metadata = sa.MetaData()

# Create a table
user_table = sa.Table(
    "user", # Name the table
    metadata, # Pass the above metadata object
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("username", sa.String),
    sa.Column("email", sa.String) # Add columns. Positional arguments so add in the desired order
)

# Interact with the table using functions:

def insert_user(username:str, email:str) -> None: #Add a new row to the table
    query = user_table.insert().values(username=username, email=email)
    connection.execute(query)

def select_user(username:str) -> sa.engine.Result: #Fetch a rown from the table based on username
    query = user_table.select().where(user_table.c.username == username)
    result = connection.execute(query)
    return result.fetchone()


# Main function which runs when the script is executed:
def main() -> None:
    metadata.create_all(engine) #Create the table
    insert_user("Cameron","cameron@mail.com")
    print(select_user("Cameron"))
    connection.close()


if __name__=="__main__":
    main()

#Output: (1, 'Cameron', 'cameron@mail.com')
