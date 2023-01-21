import pprint as pp
import ifcopenshell.util.element

model = ifcopenshell.open("AC-20-Smiley-West-10-Bldg.ifc")

walls = model.by_type("IfcWall")

print(f'Liczba ścian w modelu: {len(walls)}')

ext_walls = []
for w in walls:
    psets = ifcopenshell.util.element.get_psets(w)
    if psets.get("Pset_WallCommon"):
        if bool(psets.get("Pset_WallCommon").get("IsExternal")):
            ext_walls.append(w)
            
print(f'Liczba ścian zewnętrznych: {len(ext_walls)}')

totalvolume = 0

for w in ext_walls:
    psets = ifcopenshell.util.element.get_psets(w)
    for psetname, pset_dict in psets.items():
        for name, value in pset_dict.items():
            if name == "NetVolume":
                totalvolume += float(value)
print(f'Objętość całkowita: {totalvolume:.2f}')