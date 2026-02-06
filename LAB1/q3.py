import random
from agents import Thing, Agent, Environment

class Person(Thing):
    """A person with a visible mood."""
    def __init__(self, mood='Neutral'):
        self.mood = mood
    
    def __repr__(self):
        return f'<Person: {self.mood}>'

class TherapyEnvironment(Environment):
    """An environment where the agent encounters people."""
    
    def percept(self, agent):
        people = self.list_things_at(agent.location, tclass=Person)
        if people:
            return people[0].mood
        return None

    def execute_action(self, agent, action):
        print(f"TherapyBot action: {action}")