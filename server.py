from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from model import Agent



def draw(agent):
    """
    Portrayal Method for canvas
    """
    #Во-первых, мы определяем базовый потраял. Изображение - это словарь (который можно легко превратить в объект JSON), который сообщает стороне JavaScript, как его рисовать.
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0}

    #Мы меняем цвет и обводку изображения в зависимости от типа агента. В этом случае у нас будет красный и синий агент.
    # if agent.type == 0:
    #     portrayal["Color"] = ["#FF0000", "#FF9999"]
    #     portrayal["stroke_color"] = "#00FF00"
    # else:
    #     portrayal["Color"] = ["#0000FF", "#9999FF"]
    #     portrayal["stroke_color"] = "#000000"
    # return portrayal

#Инициализируйте холст и диаграмму.
canvas_element = CanvasGrid(draw, 100, 100, 500, 500)


#Задайте параметры модели. UserSettableParameter означает, что пользователь может изменять этот параметр на веб-странице. Он принимает 6 параметров (тип, имя, начальное значение, минимальное значение, максимальное значение, значение на шаг).
# model_params = {
#     "height": 100,
#     "width": 100,

# }

#инициализируем сервер со всеми конфигурациями, которые мы определили выше.
server = ModularServer(
    Agent, [canvas_element], "Environment"
)