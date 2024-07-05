import turtle
from pointer import Pointer
import pandas 
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:\\Users\\mdabr\\OneDrive\\Desktop\\udemy\\us game\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
point= Pointer()
score= Scoreboard()

file= pandas.read_csv("C:\\Users\\mdabr\\OneDrive\\Desktop\\udemy\\us game\\50_states.csv")

all_states = file.state.to_list()

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
game_on= True
while game_on:
    answer_input = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if answer_input is None:  # If cancel is clicked
        break
    for state in all_states:
        if answer_input.lower() == state.lower():
            state_data = file[file.state == state].iloc[0]  # Get the row corresponding to the state
            x_value = state_data['x']  # Access x value
            y_value = state_data['y']  # Access y value
            point.write_name(state, (x_value, y_value))  # Ensure (x, y) are passed as tuple
            all_states.remove(state)
            score.increase_score()
            if len(all_states) == 0:
                game_on = False


turtle.mainloop()

#screen.exitonclick()