from detection.rules.suspicious_process import SuspiciousProcessRule
from detection.rules.reverse_shell import ReverseShellRule

RULES = [
    SuspiciousProcessRule(),
    ReverseShellRule(),
]


def detect(system, processes, connections):

    alerts = []

    for rule in RULES:
        alerts.extend(
            rule.detect(
                system,
                processes,
                connections,
            )
        )

    return alerts
