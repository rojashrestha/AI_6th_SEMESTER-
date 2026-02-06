
import random
from modules.agents import Thing, Agent, Environment



# -------------------- Person --------------------
class Person(Thing):
    """A person with a visible mood."""

    def __init__(self, mood='Neutral'):
        self.mood = mood

    def __repr__(self):
        return f'<Person: {self.mood}>'


# -------------------- Environment --------------------
class TherapyEnvironment(Environment):
    """An environment where the agent encounters people."""

    def percept(self, agent):
        people = self.list_things_at(agent.location, tclass=Person)
        if people:
            return people[0].mood
        return None

    def execute_action(self, agent, action):
        print(f"TherapyBot action: {action}")


# -------------------- Simple Reflex Agent --------------------
def MoodReflexAgent():
    """Simple Reflex Agent for mood-based actions."""

    def program(percept):
        mood = percept

        if mood == 'Happy':
            return 'Smile'
        elif mood == 'Sad':
            return 'Comfort'
        elif mood == 'Angry':
            return 'Apologize'
        else:
            return 'Ignore'

    return Agent(program)


# -------------------- Simulation --------------------
if __name__ == "__main__":

    # Create environment
    env = TherapyEnvironment()

    # Change mood here: Happy, Sad, Angry, Neutral
    person = Person(mood='Sad')
    env.add_thing(person, (0, 0))

    # Add the agent
    agent = MoodReflexAgent()
    env.add_thing(agent, (0, 0))

    # Run test
    percept = env.percept(agent)
    print("Percept:", percept)

    action = agent.program(percept)
    env.execute_action(agent, action)
