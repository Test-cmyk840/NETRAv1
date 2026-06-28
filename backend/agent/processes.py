import datetime
import time

import psutil


def collect(sort_by="cpu"):
    # Prime CPU counters
    for p in psutil.process_iter():
        try:
            p.cpu_percent(None)
        except Exception:
            pass

    time.sleep(0.1)

    processes = []

    for proc in psutil.process_iter():
        try:
            with proc.oneshot():
                try:
                    mem = proc.memory_info()
                    rss = round(mem.rss / 1024**2, 2)
                    vms = round(mem.vms / 1024**2, 2)
                except Exception:
                    rss = 0.0
                    vms = 0.0

                try:
                    threads = proc.num_threads()
                except Exception:
                    threads = 0

                try:
                    started = datetime.datetime.fromtimestamp(
                        proc.create_time()
                    ).strftime("%Y-%m-%d %H:%M:%S")
                except Exception:
                    started = None

                processes.append(
                    {
                        "pid": proc.pid,
                        "ppid": proc.ppid(),
                        "name": proc.name(),
                        "user": proc.username(),
                        "status": proc.status(),
                        "exe": proc.exe() or "",
                        "cmdline": " ".join(proc.cmdline()),
                        "cpu": round(proc.cpu_percent(None), 2),
                        "memory_percent": round(
                            proc.memory_percent(), 2
                        ),
                        "rss_mb": rss,
                        "vms_mb": vms,
                        "threads": threads,
                        "nice": proc.nice(),
                        "started": started,
                    }
                )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            continue

    if sort_by == "cpu":
        processes.sort(key=lambda p: p["cpu"], reverse=True)
    elif sort_by == "memory":
        processes.sort(
            key=lambda p: p["memory_percent"],
            reverse=True,
        )
    elif sort_by == "pid":
        processes.sort(key=lambda p: p["pid"])

    return processes


if __name__ == "__main__":
    from pprint import pprint

    pprint(collect()[:10])
