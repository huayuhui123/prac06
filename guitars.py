from prac_06.guitar import Guitar

guitars = []
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
i = 0
for guitar in guitars:
    vintage_string = "It is a vintage!" if guitar.get_age() >= 50 else "Not a vintage."
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    i += 1