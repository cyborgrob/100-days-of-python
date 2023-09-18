import turtle
import pandas

# Creates the game screen and background
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

# Reads "50 states" csv file and converts it to a pandas DataFrame object
state_data = pandas.read_csv("50_states.csv")
# Converts the 'state' colum series to a list called 'state_list'
state_list = state_data.state.to_list()
# Creates a list of states the user has guessed correctly
correct_answers = []

# Runs the game while the player has guessed less than all 50 states
while len(correct_answers) < 50:
    # Creates a variable to track the user's score, based on the length of the correct_answers list
    score = len(correct_answers)
    # Prompts user to name a state and converts it to Title case
    answer = screen.textinput(f"{score}/50", "What's another state?").title()

    # Exits program if player types 'exit'
    if answer == "Exit":
        break

    # Checks if player's answer is in the list of states. If it is, it moves the turtle to the correct coordinates and
    # writes the state's name
    if answer in state_list:
        turtle.hideturtle()
        turtle.penup()
        state = state_data[state_data.state == answer]
        # Pulls the x and y coordinates from the guessed state's row and converts them into integers
        x_coord = int(state.x.iloc[0])
        y_coord = int(state.y.iloc[0])
        turtle.goto(x=x_coord, y=y_coord)
        turtle.write(answer)
        # Adds the answer to the correct_answers list and removes it from the state_list to prevent repeating the same
        # state over and over and increasing score. Also, to populate a list of missed states when exiting the program
        correct_answers.append(answer)
        state_list.remove(answer)

# Converts the remaining state_list into a pandas Dataframe object and converts that Dataframe into a csv file
missing_states = pandas.DataFrame(state_list)
missing_states.to_csv("states_to_learn.csv")


