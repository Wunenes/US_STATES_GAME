import pandas
import turtle
import state_display

display = state_display.StateName()
screen = turtle.Screen()
screen.title("US States game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
counter = 0
answers = []

game_is_on = True
while game_is_on:
    prompt = screen.textinput(title=f"{counter}/50 states correct", prompt="Enter state name")
    answer = prompt.title()

    # check answer and print in correct state
    for state_q in data["state"]:
        if answer == state_q:
            f_state = data[data.state == f"{state_q}"]
            xcor = int(f_state.x.item())
            ycor = int(f_state.y.item())
            display.answered(state_q, xcor, ycor)

            # prevent previously selected state activating counter
            if answer in answers:
                counter += 0
            else:
                counter += 1
            answers.append(answer)
            print(answers)

    # exit and displaying missing states
    if answer == "Exit":
        for unknown_state in data["state"]:
            if unknown_state not in answers:
                final_us = data[data.state == f"{unknown_state}"]
                xcor = int(final_us.x.item())
                ycor = int(final_us.y.item())
                display.color("red")
                display.answered(unknown_state, xcor, ycor)
        break

turtle.mainloop()
