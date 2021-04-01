from tkinter import *

def miles_to_kilometer():
    miles = float(miles_input.get())
    km = miles * 1.609

    kilometer_result.config(text =f"{km}")



window = Tk()
window.title("Miles to kilometer Converter")
window.config(padx= 25,pady = 25)

miles_input = Entry(width = 9)
miles_input.grid(column =1 ,row = 0)

miles_label = Label(text = "Miles")
miles_label.grid(column =2 ,row = 0)

is_equal_to = Label(text="is_equal_to")
is_equal_to.grid(column =0 ,row = 1)

kilometer_result = Label(text = "0")
kilometer_result.grid(column =1,row =1)

kilometer = Label(text = "Km")
kilometer.grid(column =2 ,row =2 )

calculate_button = Button(text = "Calculate", command = miles_to_kilometer)
calculate_button.grid(column = 1,row = 2 )


window.mainloop()

# tim = turtle.Turtle()



