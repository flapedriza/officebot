from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    channel_id: str = Field(unique=True)
    is_admin: bool = Field(default=False, index=True)
    wants_prompts: bool = Field(default=False, index=True)
    attendances: list["PersonAttendance"] = Relationship(back_populates="person")


class PersonAttendance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.id")
    person: Person = Relationship(back_populates="attendances")
    day: date = Field(index=True)
    brought_lunch: bool = Field(default=False, index=True)
    lunch_outside: bool = Field(default=False, index=True)
    in_for_beers: bool = Field(default=False, index=True)
