import platform
import socket

from api import post
from storage import save_token


def register():

    data = {
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "operating_system": platform.platform(),
        "version": "1.0.0"
    }

    response = post(
        "agents/register",
        data,
    )

    save_token(
        response["agent_token"]
    )

    print("Registered")

    print(response)
