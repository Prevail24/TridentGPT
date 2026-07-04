from core.agents.cartographer import Cartographer
from core.renderers.graph_renderer import GraphRenderer


def map_mission(mission_id: str):

    graph = Cartographer().map_mission(mission_id)

    GraphRenderer().render(graph)