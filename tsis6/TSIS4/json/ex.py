import json

file_path = r"C:\Users\Asus\Desktop\PP2\tsis6\TSIS4\json\sample-data.json"

with open(file_path) as file:
    data = json.load(file)

print("Interface status")
print("=" * 85)
print("{:<50} {:<20} {:<7} {:<5}".format("DN", "Description", "Speed", "MTU"))
print("{:<50} {:<20} {:<7} {:<5}".format("-" * 50, "-" * 20, "-" * 7, "-" * 5))

for items in data["imdata"]:
    item = items["l1PhysIf"]["attributes"]
    descr = item.get("descr", "-" * 20)

    print("{:<50} {:<20} {:<7} {:<5}".format(item["dn"], descr, item["speed"], item["mtu"]))
