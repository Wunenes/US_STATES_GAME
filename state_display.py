import turtle


class StateName(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def answered(self, state, x, y):
        self.goto(x, y)
        self.write(f"{state}", align="center", font=('Arial', 8, 'normal'))
