import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(100, 100)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess a State", prompt="What's the state name").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            text_turtle = turtle.Turtle()
            text_turtle.hideturtle()
            text_turtle.penup()
            state_data = data[data.state == answer_state]
            text_turtle.goto(int(state_data.x), int(state_data.y))
            text_turtle.write(answer_state)
            guessed_states.append(answer_state)

    num_of_guessed_state = len(guessed_states)
    scoreboard.clear()
    scoreboard.write(f"{num_of_guessed_state} / 50")

states_to_learn = []
# States to learn csv
for states in all_states:
    if states not in guessed_states:
        states_to_learn.append(states)


# Convert the list to a DataFrame
states_to_learn_df = pandas.DataFrame(states_to_learn, columns=["State"])

# Save the DataFrame to a CSV file
states_to_learn_df.to_csv("states_to_learn.csv")


screen.mainloop()