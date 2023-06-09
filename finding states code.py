import turtle
import pandas

#creating a screen and map for game
screen = turtle.Screen()
screen.title("u.s. states game")
image = "states.gif"
screen.addshape(image)
turtle.shape(image)
state_loc = turtle.Turtle()
state_loc.hideturtle()

#using states csv file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []


#checking the state is in the 50 states and locating the states

while len(guessed_state) < 50:
    answer_state = screen.textinput(f"{len(guessed_state)}/50 states correct", "What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        state1 = data[data.state == answer_state]
        state_x = int(state1.x)
        state_y = int(state1.y)
        state_loc.penup()
        state_loc.goto(state_x, state_y)
        state_loc.write(answer_state, align="center", font=("Courier", 11, "normal"))
