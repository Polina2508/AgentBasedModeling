from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class Scientist(Agent):

    def __init__(self, unique_id, model, energy, justice, expertise):
        super().__init__(unique_id, model)
        self.energy = energy
        self.justice = justice
        self.expertise = expertise

class Environment(Model):

    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = Scientist(i, self, energy=1, justice=2, expertise=3)
            self.schedule.add(a)

            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
