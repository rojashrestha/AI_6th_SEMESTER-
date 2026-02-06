
# -------------------- Base Classes --------------------
class Thing:
    pass


class Agent(Thing):
    def __init__(self, program):
        self.program = program
        self.location = None


class Environment:
    def __init__(self):
        self.things = []

    def add_thing(self, thing, location):
        thing.location = location
        self.things.append(thing)

    def delete_thing(self, thing):
        if thing in self.things:
            self.things.remove(thing)

    def list_things_at(self, location, tclass=None):
        result = []
        for thing in self.things:
            if thing.location == location:
                if tclass is None or isinstance(thing, tclass):
                    result.append(thing)
        return result

    def run(self, steps=1):
        for _ in range(steps):
            for thing in self.things:
                if isinstance(thing, Agent):
                    percept = self.percept(thing)
                    action = thing.program(percept)
                    self.execute_action(thing, action)


# -------------------- Person --------------------
class Person(Thing):
    """A person who exists in the hallway."""
    def __repr__(self):
        return "<Person>"


# -------------------- Hallway Environment --------------------
class HallwayEnvironment(Environment):
    """Environment representing a hallway."""

    def percept(self, agent):
        people = self.list_things_at(agent.location, Person)
        return 'Present' if len(people) > 0 else 'Absent'

    def execute_action(self, agent, action):
        print(f"GreeterBot perceives {self.percept(agent)} and does: {action}")


# -------------------- Model-Based Reflex Agent --------------------
def ModelBasedGreeterAgent():
    """
    Model-Based Reflex Agent that remembers
    whether it has already greeted the person.
    """

    # Internal State (Memory)
    model = {
        'has_greeted': False
    }

    def program(percept):
        if percept == 'Present':
            if not model['has_greeted']:
                model['has_greeted'] = True
                return 'Say Hello'
            else:
                return 'Wait'

        elif percept == 'Absent':
            model['has_greeted'] = False
            return 'Wait'

    return Agent(program)


# -------------------- Broken Agent (No Memory) --------------------
def BrokenGreeterAgent():
    def program(percept):
        if percept == 'Present':
            return 'Say Hello'
        return 'Wait'
    return Agent(program)


# -------------------- Simulation --------------------
if __name__ == "__main__":
    env = HallwayEnvironment()

    # Choose ONE agent at a time
    agent = ModelBasedGreeterAgent()
    # agent = BrokenGreeterAgent()

    env.add_thing(agent, (0, 0))

    print("\n--- Simulation Start ---")

    # Step 1: Empty hallway
    print("\nStep 1: Empty Hallway")
    env.run(steps=1)

    # Step 2: Person enters
    print("\nStep 2: Person Enters")
    p1 = Person()
    env.add_thing(p1, (0, 0))
    env.run(steps=1)

    # Step 3: Person stays
    print("\nStep 3: Person Stays")
    env.run(steps=1)

    # Step 4: Person leaves
    print("\nStep 4: Person Leaves")
    env.delete_thing(p1)
    env.run(steps=1)

    # Step 5: Person returns
    print("\nStep 5: Person Returns")
    env.add_thing(p1, (0, 0))
    env.run(steps=1)
