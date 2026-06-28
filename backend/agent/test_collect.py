from collector import collect

data = collect()

print("=" * 50)
print("SYSTEM")
print("=" * 50)
print(data["system"])

print()

print("=" * 50)
print("PROCESSES")
print("=" * 50)
print(len(data["processes"]))

print()

print("=" * 50)
print("NETWORK CONNECTIONS")
print("=" * 50)
print(len(data["connections"]))
