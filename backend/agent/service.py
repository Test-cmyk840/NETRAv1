from registration import register
from heartbeat import heartbeat
from storage import get_token


def run():

    token = get_token()

    if not token:

        print("Registering...")

        register()

    heartbeat()
