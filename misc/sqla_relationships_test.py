# SQL Alchemy (Relationships)
# Creating multiple tables and defining the relationships between them

import sqlalchemy as sa
from sqlalchemy.orm import Mapped,mapped_column,sessionmaker,declarative_base,relationship

db = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=db)
Base = declarative_base()


class User(Base):
    __tablename__ = "users" # Name the table

    
    id: Mapped[int] = mapped_column(primary_key=True) #Make this the primary column



# Other tables in the db
class UserAuth(Base):
    __tablename__ = "user_auth"



class UserPost(Base):
    __tablename__ = "user_post"
