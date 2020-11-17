import sys
from src.Render import RenderResult
from src.RegisteryManager import RegisteryManager

user_input = sys.argv[1]

items = []

RegisteryManager = RegisteryManager()
Render = RenderResult()
port_registrated = RegisteryManager.port_registrated(user_input)
data = RegisteryManager.data

if port_registrated == True:
    if not isinstance(data[user_input], list):
        items.append(
            RegisteryManager.retrieve_port_info(
                data[user_input])
            )
    else:
        for x in data[user_input]:
            items.append(
                RegisteryManager.retrieve_port_info(x)
                )
    Render.display_result(items)
else:
    print("Port " + user_input + ": Not found in registry")