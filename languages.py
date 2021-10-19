from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(ruby)
print(python)
print(visual_basic)
lists = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for kind in lists:
    if kind.is_dynamic():
        print(kind.field, end='\n')
