import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:\\Users\\mdabr\\OneDrive\\Desktop\\udemy\\us game\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

answer_input= screen.textinput(title="Guess the State", prompt="What's another state's name?")


turtle.mainloop()

#screen.exitonclick()