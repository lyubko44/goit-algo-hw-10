from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="optimal_production", sense=LpMaximize)

A = LpVariable(name="limonad_units", lowBound=0, cat='Integer')
B = LpVariable(name="fruit_juice_units", lowBound=0, cat='Integer')

water = 2*A + B <= 100
sugar = A <= 50
lemon = A <= 30
fruit_puree = 2*B <= 40

model += water
model += sugar
model += lemon
model += fruit_puree

model += A + B

model.solve()

print("Результати оптимізації:")
print(f"Кількість виробленого лимонаду: {A.varValue} одиниць")
print(f"Кількість виробленого фруктового соку: {B.varValue} одиниць")
