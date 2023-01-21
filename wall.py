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

