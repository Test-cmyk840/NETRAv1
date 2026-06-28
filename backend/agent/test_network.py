from pprint import pprint

from network import get_connections

connections = get_connections()

print(f"Connections: {len(connections)}")

pprint(connections[:10])
