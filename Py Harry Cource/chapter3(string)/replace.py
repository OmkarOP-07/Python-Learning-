letter = '''Hello <Name>, 
You are selected <Name>, on <date>
Your sincerely, 
<hr name>'''

print(letter.replace("<Name>", "Omkar").replace("<date>", "23/04/2025").replace("<hr name>", "Sonali Mhatre")
)

str = "Harry is a good  boy "  # strings are immutable
print(str.find("  "))

print(str.replace("  ", " ")) # remove double white spaces