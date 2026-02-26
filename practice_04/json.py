#1 Python program to parse sample-data.json and format output
import json

# Open and load JSON file
with open("sample-data.json", "r") as file:
    data = json.load(file)

# Print header
print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
print("-" * 80)

# Navigate through JSON (adjust keys if structure is different)
interfaces = data["imdata"]

for item in interfaces:
    attributes = item["l1PhysIf"]["attributes"]

    # Extract required fields
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")

    # Print formatted row
    print(f"{dn:50} {descr:20} {speed:8} {mtu:6}")