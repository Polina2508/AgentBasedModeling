from mesa import Model, Agent
from mesa.space import SingleGrid
from mesa.time import RandomActivation


class Scientist(Agent):
      def __init__(self, unique_id, model, pos, energy ,expertise_level ,fairness_level):

        super().__init__(unique_id, model)
        self.pos = np.array(pos)
        self.energy = energy
        self.expertise_level = expertise_level
        self.fairness_level = fairness_level




class Environment(Model):
      def __init__(self, height=100, width=100):
        self.height = height
        self.width = width


        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(width, height, torus=True)

      # def step(self):
      #   """
      #   Run one step of the model. If All agents are happy, halt the model.
      #   """
      #   self.happy = 0  # Reset counter of happy agents
      #   self.schedule.step()
      #   # collect data
      #   self.datacollector.collect(self)

      #   if self.happy == self.schedule.get_agent_count():
      #       self.running = False
