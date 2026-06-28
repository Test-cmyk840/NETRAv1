SUSPICIOUS_PORTS = {
    4444,
    4445,
    5555,
    6666,
    9001,
    1337,
    31337,
}


def detect(connections):

    alerts = []

    for conn in connections:

        port = conn.get("local_port")

        if port in SUSPICIOUS_PORTS:

            alerts.append(
                {
                    "rule": "SUSPICIOUS_PORT",
                    "severity": "MEDIUM",
                    "port": port,
                    "process": conn.get("process"),
                    "pid": conn.get("pid"),
                    "message": f"Listening on suspicious port {port}",
                }
            )

    return alerts
