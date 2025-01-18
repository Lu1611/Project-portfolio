sandwich_orders = ['cheese', 'sausage', 'mozarella', 'ham and cheese', 'turkey']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)