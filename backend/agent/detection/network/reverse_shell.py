SUSPICIOUS_PROCESSES = {
    "bash",
    "sh",
    "zsh",
    "python",
    "python3",
    "perl",
    "ruby",
    "php",
    "nc",
    "netcat",
    "ncat",
    "socat",
}

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

        process = conn.get("process", "").lower()

        if process not in SUSPICIOUS_PROCESSES:
            continue

        if conn.get("status") != "ESTABLISHED":
            continue

        if conn.get("remote_ip") is None:
            continue

        if conn.get("remote_port") not in SUSPICIOUS_PORTS:
            continue

        alerts.append(
            {
                "rule": "REVERSE_SHELL",
                "severity": "HIGH",
                "process": conn.get("process"),
                "pid": conn.get("pid"),
                "remote_ip": conn.get("remote_ip"),
                "remote_port": conn.get("remote_port"),
                "message": "Possible reverse shell detected",
            }
        )

    return alerts
