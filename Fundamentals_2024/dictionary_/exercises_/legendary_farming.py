materials = {"shards": 0, "fragments": 0, "motes": 0 }
obtained = False
while not obtained:
    material_list = input().split()
    for index in range(0, len(material_list), 2):
        quantity = int(material_list[index])
        material = material_list[index + 1].lower()
        if material not in materials:
            materials[material] = 0
        materials[material] += quantity

        if materials["shards"] >= 250:
            materials["shards"] -= 250
            print("Shadowmourne obtained!" )
            obtained = True
        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            print("Valanyr obtained!")
            obtained = True

        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            print("Dragonwrath obtained!")
            obtained = True
        if obtained:
            break

for material, quantity in materials.items():
    print(f"{material}: {quantity}")