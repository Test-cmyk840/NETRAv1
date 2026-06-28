from detection.engine import detect

system = {}

processes = [
    {
        "pid": 100,
        "name": "bash",
        "cpu_percent": 0,
        "memory_percent": 0,
        "username": "root",
    },
    {
        "pid": 200,
        "name": "netcat",
        "cpu_percent": 2,
        "memory_percent": 1,
        "username": "root",
    },
]

connections = [
    {
        "pid": 200,
        "process": "netcat",
        "local_ip": "192.168.1.10",
        "local_port": 54321,
        "remote_ip": "10.10.10.5",
        "remote_port": 4444,
        "status": "ESTABLISHED",
    }
]

alerts = detect(
    system,
    processes,
    connections,
)

print(alerts)
