SUSPICIOUS_PROCESSES = {
    "nc",
    "netcat",
    "ncat",
    "socat",
    "hydra",
    "hashcat",
    "john",
    "mimikatz",
    "meterpreter",
}


def detect(processes):

    alerts = []

    for process in processes:

        name = process.get("name", "").lower()

        if name in SUSPICIOUS_PROCESSES:

            alerts.append(
                {
                    "rule": "SUSPICIOUS_PROCESS",
                    "severity": "HIGH",
                    "pid": process.get("pid"),
                    "process": process.get("name"),
                    "message": "Suspicious process detected",
                }
            )

    return alerts
