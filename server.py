from model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


def agent_portrayal(a):
    port = {"Shape": "circle",
                 "Filled": "false",
                 "Layer": 0,
                 "Color": "green",
                 "r": 0.5}
    return port



grid = CanvasGrid(agent_portrayal, 30, 30, 500, 500)
server = ModularServer(Environment,
                       [grid],
                       "ScientistModel",
                       { "N":10, "O":5, "width":30, "height":30})
server.port = 8521 # The default
server.launch()
