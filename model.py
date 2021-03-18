from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random

class Scientist(Agent):

    def __init__(self, unique_id, model, energy, justice, expertise):
        super().__init__(unique_id, model)
        self.energy = energy
        self.justice = justice
        self.expertise = expertise
        print("Energy", energy)
        print("Justice", justice)
        print("Expertise", expertise)
    

class Environment(Model):

    def __init__(self, N, width, height):
        self.num_agents = 10
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = Scientist(i,self, 
            energy=random.normalvariate(10, 2), 
            justice=random.normalvariate(10, 2), 
            expertise=random.normalvariate(10, 2))

            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
