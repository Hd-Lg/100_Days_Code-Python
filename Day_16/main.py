# import turtle

# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(300)

# print(timmy)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokkemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = 'l'

print(table)
