from processes import collect as get_processes
from network import get_connections
from systeminfo import collect as get_system_info


def collect():
    return {
        "system": get_system_info(),
        "processes": get_processes(),
        "connections": get_connections(),
    }
