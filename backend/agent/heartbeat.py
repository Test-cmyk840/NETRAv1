from api import post
from storage import get_token


def heartbeat():

    token = get_token()

    if not token:
        return

    response = post(
        "agents/heartbeat",
        {
            "agent_token": token
        },
    )

    print(response)
