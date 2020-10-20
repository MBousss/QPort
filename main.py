import sys
import re
from src.render import RenderResult
from src.registery_manager import RegisteryManager

user_input = sys.argv[1]

items = []

registery_manager = RegisteryManager()
render = RenderResult()
port_registrated = registery_manager.port_registrated(user_input)
data = registery_manager.data

if port_registrated == True:
    if not isinstance(data[user_input], list):
        items.append(
            registery_manager.retrieve_port_info(data[user_input])
            )
    else:
        for x in data[user_input]:
            items.append(
                registery_manager.retrieve_port_info(x)
                )
    render.display_result(items)
else:
    print("Port " + user_input + ": Not found in registry")