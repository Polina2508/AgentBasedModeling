from mesa import Agent


class RandomWalker(Agent):


    grid = None
    x = None
    y = None
   

    def __init__(self, unique_id, pos, model):
     
        super().__init__(unique_id, model)
        self.pos = pos
     

    def random_move(self):
      
      
        next_moves = self.model.grid.get_neighborhood(self.pos, True)
        next_move = self.random.choice(next_moves)
    
        self.model.grid.move_agent(self, next_move)