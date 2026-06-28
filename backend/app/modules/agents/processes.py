import psutil


def collect():
    processes = []

    for proc in psutil.process_iter(
        [
            "pid",
            "ppid",
            "name",
            "username",
            "exe",
            "cmdline",
            "create_time",
        ]
    ):
        try:
            info = proc.info

            processes.append(
                {
                    "pid": info["pid"],
                    "ppid": info["ppid"],
                    "name": info["name"] or "",
                    "user": info["username"] or "",
                    "exe": info["exe"] or "",
                    "cmdline": " ".join(info["cmdline"] or []),
                    "cpu": round(proc.cpu_percent(interval=None), 2),
                    "memory": round(proc.memory_percent(), 2),
                    "started": info["create_time"],
                }
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            continue

    return sorted(processes, key=lambda p: p["cpu"], reverse=True)
