import requests

from config import load_config


def post(endpoint, data):

    config = load_config()

    url = f"{config['server']}/{endpoint}"

    headers = {}

    if endpoint == "agents/register":
        headers["Authorization"] = (
            f"Bearer {config['admin_token']}"
        )

    response = requests.post(
        url,
        json=data,
        headers=headers,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()
