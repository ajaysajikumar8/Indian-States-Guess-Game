import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("India States Game")
screen.setup(height=750)
image = "india-outline-map.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()
t.penup()


data = pd.read_csv("state_cordinates.csv")
state_list = data["State"].to_list()
guessed_state = []

#code for finding the coordinates of the states
    # def find_coor(x,y):
    #     print(x,y)
    # turtle.onscreenclick(find_coor)
    # turtle.mainloop()

while len(guessed_state) < 37:
    answer_state = (screen.textinput(title= f"{len(guessed_state)}/37 States and UT Correct", prompt="Name a State or Union Territory      ")).title().strip()
    if answer_state == "Exit":
        states_to_learn = [state for state in state_list if state not in guessed_state]
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in state_list:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
        state_data = data[data["State"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

