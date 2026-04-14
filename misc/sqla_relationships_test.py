# SQL Alchemy (Relationships)
# Creating multiple tables and defining the relationships between them

import sqlalchemy as sa
from sqlalchemy.orm import Mapped,mapped_column,sessionmaker,declarative_base,relationship
import hashlib

db = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=db)
Base = declarative_base()


class Users(Base):
    __tablename__ = "users" # Name the table

    # Columns:
    id: Mapped[int] = mapped_column(primary_key=True) #Make this the primary column
    auth: Mapped["UserAuth"] = relationship("UserAuth", uselist=False, back_populates="user") # Relate to UserAuth table below (1:1 relationship between auth and user columns)
    posts: Mapped[list["UserPost"]] = relationship("UserPost", back_populates="user") # Relate to UserPost table below (1:many relationship)

    def __init__(self, username:str, email:str, password:str):
        super().__init__()
        self.auth = UserAuth(username=username, email=email) # Authentication to access the table is determined by the UserAuth table below
        self.auth.set_password(password) #Custom method defined in the UserAuth object
    
    def __repr__(self) -> str:
        return f"<Users(username={self.auth.username}, email={self.auth.email})>"
    


# Other tables in the db
class UserAuth(Base):
    __tablename__ = "user_auth"

    # Columns:
    id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey("users.id"), primary_key=True) #Make this the primary column (likened to user_id in UserPost)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(index=True, unique=True)
    password_hash: Mapped[str]
    user: Mapped["Users"] = relationship("Users", back_populates="auth")

    def __init__(self, username:str, email:str):
        self.username = username
        self.email = email
    
    def __repr__(self) -> str:
        return f"<UserAuth(username={self.username}, email={self.email})>"
    
    # Bespoke methods attached to this object:

    def set_password(self, password: str) -> None:
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password: str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    

class UserPost(Base):
    __tablename__ = "user_post"

    id: Mapped[int] = mapped_column(primary_key=True) #Make this the primary column. This is the id of an individual post, not the user id
    user_id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True) #likened to id in UserAuth
    content: Mapped[str]
    user: Mapped["Users"] = relationship("Users", back_populates="posts")

    def __repr__(self) -> str:
        return f"<UserPost(user={self.user}, content={self.content})>"
