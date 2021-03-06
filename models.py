from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


# class Team(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     headquarters: str

#     heroes: List["Hero"] = Relationship(back_populates="team")


# class Hero(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     secret_name: str
#     age: Optional[int] = Field(default=None, index=True)

#     team_id: Optional[int] = Field(default=None, foreign_key="team.id")
#     team: Optional[Team] = Relationship(back_populates="heroes")


class Team (SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    headquarter: str
    heroes: List["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional["Team"] = Relationship(back_populates="heroes")
