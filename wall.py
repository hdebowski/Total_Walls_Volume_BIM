import pprint as pp
import ifcopenshell.util.element

model = ifcopenshell.open("AC-20-Smiley-West-10-Bldg.ifc")

walls = model.by_type("IfcWall")

print(f'Liczba ścian w modelu: {len(walls)}')


