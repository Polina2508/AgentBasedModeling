from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random

from random_walk import RandomWalker

class Scientist(Agent):

    def __init__(self, unique_id, pos, model, energy, justice, expertise):
        super().__init__(unique_id, model)
        self.energy = energy
        self.justice = justice
        self.expertise = expertise
        print("Energy", energy)
        print("Justice", justice)
        print("Expertise", expertise)

    def step(self):
        
        living = True
        

        if living and self.random.random() < self.model.scientist_reproduce:
            # Create a new sheep:
            lamb = Content(
                self.model.next_id(), self.model
            )
            self.model.grid.place_agent(lamb, self.pos)
            self.model.schedule.add(lamb)
        


        


class Content(RandomWalker):

    def __init__(self, unique_id, model):
        super().__init__(unique_id,self, model)

    def step(self):
        self.random_move()
        
    

    

class Environment(Model):
    height = 30
    width = 30

    def __init__(self, height = 20, width = 20 , num_agents = 10,  scientist_reproduce=0.04):
        super().__init__()
        self.heidht = height
        self.width = width
        self.num_agents = num_agents
        # self.num_content = num_content
        self.scientist_reproduce = scientist_reproduce
        
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(self.height, self.width, torus = True)
     
       

        for i in range(self.num_agents):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy=random.normalvariate(10, 2)
            justice=random.normalvariate(10, 2)
            expertise=random.normalvariate(10, 2)
            a = Scientist(self.next_id(), (x, y), self, True, justice, expertise )
            self.grid.place_agent(a, (x, y))
            self.schedule.add(a)


        
        
        # for a in range(self.num_content):
        #     b = Content(a, self)
        #     x = self.random.randrange(self.grid.width)
        #     y = self.random.randrange(self.grid.height)
        #     self.grid.place_agent(b, (x, y))


        
        self.running = True

        


    def step(self):
        
        self.schedule.step()