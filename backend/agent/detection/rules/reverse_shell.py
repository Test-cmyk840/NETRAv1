from detection.base import DetectionRule


class ReverseShellRule(DetectionRule):

    name = "Reverse Shell"

    severity = "critical"

    SHELLS = {
        "bash",
        "sh",
        "zsh",
        "python",
        "python3",
        "perl",
        "php",
        "ruby",
        "nc",
        "netcat",
        "ncat",
    }

    def detect(
        self,
        system,
        processes,
        connections,
    ):

        alerts = []

        process_map = {
            p["pid"]: p
            for p in processes
        }

        for connection in connections:

            if connection["status"] != "ESTABLISHED":
                continue

            pid = connection["pid"]

            if pid not in process_map:
                continue

            process = process_map[pid]

            if process["name"].lower() in self.SHELLS:

                alerts.append(
                    {
                        "rule": self.name,
                        "severity": self.severity,
                        "message": (
                            f"{process['name']} established "
                            f"an outbound connection"
                        ),
                        "process": process["name"],
                        "pid": pid,
                        "remote_ip": connection["remote_ip"],
                        "remote_port": connection["remote_port"],
                    }
                )

        return alerts
