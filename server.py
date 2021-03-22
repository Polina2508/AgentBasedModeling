from model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

OBJECT_COLOR = "#FF66FF"
SCIENTIST_COLOR = "#660066"

def scientist_object_portrayal(agent):
    if agent is None:
        return

    portrayal = {
        "Shape": "circle",
        "x": agent.pos[0],
        "y": agent.pos[1],
        "Filled": "true",
    }

    if isinstance(agent, Scientist):

        portrayal["Color"] = SCIENTIST_COLOR
        portrayal["r"] = 0.8
        portrayal["Layer"] = 1

    elif isinstance(agent, Content):
        portrayal["Color"] = OBJECT_COLOR
        portrayal["r"] = 0.5
        portrayal["Layer"] = 1
    return portrayal




grid = CanvasGrid(scientist_object_portrayal, 30, 30, 500, 500)
server = ModularServer(Environment,
                       [grid],
                       "ScientistModel",
                       { "num_agents":10, "num_content":5, "width":30, "height":30})
server.port = 8521 # The default
server.launch()
