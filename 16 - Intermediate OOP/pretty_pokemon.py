from prettytable import PrettyTable

table = PrettyTable()

table.align = "l" #aligns text left
table.field_names = ["Pokemon Name", "Type"]

pokemon = [
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
]

table.add_rows(pokemon)
print(table)