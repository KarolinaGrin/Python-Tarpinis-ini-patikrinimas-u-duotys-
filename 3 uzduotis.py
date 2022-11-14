# Turimas "audi" dict.

# Parašykite funkciją "show_object_values", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}

# def show_object_values(audi):
# for audi in audi:
#print (audi)

# show_object_values(audi)

show_object_values = audi.values()
print(show_object_values)
