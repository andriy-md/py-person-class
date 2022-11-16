from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def connect_marriages(cls, person: dict) -> None:
        if "wife" in person and person["wife"]:
            cls.people[person["name"]].wife = cls.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            cls.people[person["name"]].husband = cls.people[person["husband"]]


def create_person_list(people: list) -> list:
    # iterate through list of people and add each to Person.people
    [Person(person["name"], person["age"]) for person in people]
    # iterate through Person.people and find marriage connections
    [Person.connect_marriages(person) for person in people]
    return [person for person in Person.people.values()]
