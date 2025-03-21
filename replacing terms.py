with open('data.csv', 'r') as file:
    content = file.readlines()

content = [line.replace(";", ",") for line in content]

with open('data.csv', 'w') as file:
    file.writelines(content)

print("Replacement complete!")

