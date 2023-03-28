String = "Palavra"
StringInvertida = ""

for i in range(len(String)-1, -1, -1):
    StringInvertida += String[i]

print(StringInvertida)