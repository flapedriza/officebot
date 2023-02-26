from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    channel_id: str = Field(unique=True, index=True)
    is_admin: bool = False
    wants_prompts: Optional[bool] = None
    assistances: list["PersonAssistance"] = Relationship(back_populates="person")


class PersonAssistance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.id")
    person: Person = Relationship(back_populates="assistances")
    day: date
    brought_lunch: bool = Field(default=False, index=True)
    lunch_outside: bool = Field(default=False, index=True)
    in_for_beers: bool = Field(default=False, index=True)
