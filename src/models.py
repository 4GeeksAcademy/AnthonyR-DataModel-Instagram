from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(15), nullable=False)
    lastname: Mapped[str] = mapped_column(String(15), nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    comment: Mapped[list["Comment"]] = relationship(back_populates="author")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    comment_text: Mapped[str] = mapped_column(String(150), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="comment")


    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "user_id": self.user_id,
            "author": self.author,
            # do not serialize the password, its a security breach
        }

