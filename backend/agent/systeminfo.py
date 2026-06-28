import getpass
import platform
import socket
import time
import uuid

import psutil


def get_lan_ip():
    """
    Returns the primary LAN IP (192.168.x.x / 10.x.x.x / etc.)
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Doesn't actually connect
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()

    return ip


def get_mac():
    return ":".join(
        f"{(uuid.getnode() >> shift) & 0xff:02x}"
        for shift in range(40, -1, -8)
    )


def collect():
    vm = psutil.virtual_memory()
    du = psutil.disk_usage("/")

    return {
        "hostname": socket.gethostname(),
        "fqdn": socket.getfqdn(),
        "ip": get_lan_ip(),
        "mac": get_mac(),
        "user": getpass.getuser(),
        "os": platform.system(),
        "platform": platform.platform(),
        "kernel": platform.release(),
        "architecture": platform.machine(),
        "cpu": platform.processor(),
        "physical_cores": psutil.cpu_count(False),
        "logical_cores": psutil.cpu_count(True),
        "memory_total_gb": round(vm.total / 1024**3, 2),
        "memory_available_gb": round(vm.available / 1024**3, 2),
        "memory_percent": vm.percent,
        "disk_total_gb": round(du.total / 1024**3, 2),
        "disk_used_gb": round(du.used / 1024**3, 2),
        "disk_free_gb": round(du.free / 1024**3, 2),
        "disk_percent": du.percent,
        "boot_time": time.strftime(
            "%Y-%m-%d %H:%M:%S",
            time.localtime(psutil.boot_time()),
        ),
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(collect())
