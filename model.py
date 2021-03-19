from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from mesa.datacollection import DataCollector

class Scientist(Agent):

    def __init__(self, unique_id, model, energy, justice, expertise):
        super().__init__(unique_id, model)
        self.energy = energy
        self.justice = justice
        self.expertise = expertise
        print("Energy", energy)
        print("Justice", justice)
        print("Expertise", expertise)

    def step(self):
        living = true
    
        if living and self.random.random() < self.model.sheep_reproduce:
            # Create a new sheep:
            lamb = Scientist(
                self.model.next_id(), self.pos, self.model, self.energy
            )
            self.model.grid.place_agent(lamb, self.pos)
            self.model.schedule.add(lamb)



        
        


        


class Content(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        

    
 
        
        

    

class Environment(Model):

    def __init__(self, N, O, width, height):
        self.num_agents = 10
        self.running = True
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        for i in range(self.num_agents):
            a = Scientist(i,self, 
            energy=random.normalvariate(10, 2), 
            justice=random.normalvariate(10, 2), 
            expertise=random.normalvariate(10, 2))
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
        
        self.num_object = 5
        for a in range(self.num_object):
            b = Content(a, self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (x, y))

        


    def step(self):
        self.schedule.step()




 





