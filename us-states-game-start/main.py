import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv") 
state_names = data.state.to_list()
guessed_state_list = []


for i in range(len(state_names)):
    answer_state = screen.textinput(title=f"{len(guessed_state_list)}/50 State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [n for n in state_names if n not in guessed_state_list]
        # for i in state_names:
        #     if i not in guessed_state_list:
        #         missing_states.append(i)
        new_data_to_learn = pandas.DataFrame(missing_states)
        new_data_to_learn.to_csv("States_to_learn_data4.csv")
        break

    

    if answer_state in state_names:
        guessed_state_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()     # to hide turtle shape
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
   
