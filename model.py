from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from mesa.datacollection import DataCollector
from random_walk import RandomWalker

class Scientist(RandomWalker):

    def __init__(self, unique_id, model, energy, justice, expertise):
        
        self.energy = energy
        self.justice = justice
        self.expertise = expertise
        print("Energy", energy)
        print("Justice", justice)
        print("Expertise", expertise)

    def step(self):
        living = true

        if living and self.random.random() < self.model.scientist_reproduce:
            # Create a new sheep:
            lamb = Scientist(
                self.model.next_id(), self.pos, self.model, self.energy, self.justice, self.expertise
            )
            self.model.grid.place_agent(lamb, self.pos)
            self.model.schedule.add(lamb)
        


        


class Content(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
    

    

class Environment(Model):

    def __init__(self, height, width, N, O, scientist_reproduce=0.04):
        super().__init__()
        self.heidht = height
        self.width = width
        self.num_agents = 10
        self.scientist_reproduce = scientist_reproduce
        
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(self.width, self.height, torus = True)
     
       

        # for i in range(self.num_agents):
        #     a = Scientist(i,self,
        #     energy=random.normalvariate(10, 2), 
        #     justice=random.normalvariate(10, 2), 
        #     expertise=random.normalvariate(10, 2))
        #     x = self.random.randrange(self.grid.width)
        #     y = self.random.randrange(self.grid.height)
        #     self.grid.place_agent(a, (x, y))
        for i in range(self.num_agents):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy=random.normalvariate(10, 2)
            justice=random.normalvariate(10, 2)
            expertise=random.normalvariate(10, 2)
            a = Scientist(self.next_id(), (x, y), self, energy, justice, expertise)
            self.grid.place_agent(a, (x, y))
            self.schedule.add(a)


        
        self.num_object = 5
        for a in range(self.num_object):
            b = Content(a, self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (x, y))


        
        self.running = True

        


    def step(self):
        
        self.schedule.step()

    




 





