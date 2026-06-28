from detection.base import DetectionRule


class SuspiciousProcessRule(DetectionRule):

    name = "Suspicious Process"

    severity = "high"

    BAD_PROCESSES = {
        "mimikatz",
        "nc",
        "netcat",
        "ncat",
        "hydra",
        "john",
        "hashcat",
        "aircrack-ng",
    }

    def detect(
        self,
        system,
        processes,
        connections,
    ):

        alerts = []

        for process in processes:

            if process["name"].lower() in self.BAD_PROCESSES:

                alerts.append({
                    "rule": self.name,
                    "severity": self.severity,
                    "message": f"Suspicious process: {process['name']}",
                    "process": process["name"],
                    "pid": process["pid"],
                })

        return alerts
