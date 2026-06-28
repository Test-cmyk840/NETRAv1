import socket
import psutil


def get_connections():

    connections = []

    for conn in psutil.net_connections(kind="inet"):

        try:

            local_ip = conn.laddr.ip if conn.laddr else None
            local_port = conn.laddr.port if conn.laddr else None

            remote_ip = conn.raddr.ip if conn.raddr else None
            remote_port = conn.raddr.port if conn.raddr else None

            process = ""

            if conn.pid:
                try:
                    process = psutil.Process(conn.pid).name()
                except Exception:
                    process = "Unknown"

            connections.append(
                {
                    "pid": conn.pid,
                    "process": process,
                    "local_ip": local_ip,
                    "local_port": local_port,
                    "remote_ip": remote_ip,
                    "remote_port": remote_port,
                    "status": conn.status,
                }
            )

        except Exception:
            continue

    return connections
