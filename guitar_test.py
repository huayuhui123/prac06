from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 20000.0)
print(guitar1.get_age())
print(guitar2.get_age())
print(guitar1.is_vintage())
print(guitar2.is_vintage())


