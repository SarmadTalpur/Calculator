import tkinter as tk


class Calc:
    # constructor that creates an object and uses that master object fields
    def __init__(self, master):
        # calling parent constructor, to make a tkinter window
        super().__init__()
        self.master = master

        # variables to get value from widgets
        self.input_variable1 = tk.DoubleVar(master)
        self.input_variable2 = tk.DoubleVar(master)
        self.format_value = tk.IntVar(master)
        self.result_value = tk.StringVar(master)
        self.calc_result1 = tk.IntVar(master)
        self.calc_result2 = tk.IntVar(master)

        # using trace method to perform an action through calculate method when
        # any of the below variable's value is changed
        self.input_variable1.trace("w", self.calculate)
        self.input_variable2.trace("w", self.calculate)
        self.format_value.trace("w", self.calculate)

        self.header1 = tk.Label(self.master, text="************************************", padx=20)
        self.header2 = tk.Label(self.master, text="Created by Sarmad Talpur", padx=20)
        self.header3 = tk.Label(self.master, text="************************************", padx=20)
        self.header1.pack()
        self.header2.pack()
        self.header3.pack()

        # creating a frame for input entries and labels that fits master frame
        input_frame = tk.Frame(self.master)
        input_frame.pack()

        # creating widgets for inputs
        self.label1 = tk.Label(input_frame, text="Enter first number").grid(
            row=0, column=0, padx=(10, 10))
        self.entry1 = tk.Entry(input_frame, textvariable=self.input_variable1).grid(
            row=0, column=1, padx=(10, 10))
        self.label2 = tk.Label(input_frame, text="Enter second number").grid(
            row=1, column=0, padx=(10, 10))
        self.entry2 = tk.Entry(input_frame, textvariable=self.input_variable2).grid(
            row=1, column=1, padx=(10, 10))

        # creating a frame for radio buttons that fits master frame
        format_frame = tk.Frame(self.master)
        format_frame.pack()

        # creating radio buttons
        self.add_button = tk.Radiobutton(
            format_frame, variable=self.format_value, value=0, text="Add"
        ).grid(row=0, column=0)

        self.sub_button = tk.Radiobutton(
            format_frame, variable=self.format_value, value=1, text="Subtract"
        ).grid(row=0, column=1)

        self.mult_button = tk.Radiobutton(
            format_frame, variable=self.format_value, value=2, text="Multiply"
        ).grid(row=0, column=2)

        self.div_button = tk.Radiobutton(
            format_frame, variable=self.format_value, value=3, text="Divide"
        ).grid(row=0, column=3)

        # creating a label for result
        self.result = tk.Label(self.master, pady=10, textvariable=self.result_value)
        self.result.pack()

        # method to quit application when Exit button is clicked
        def end_calc():
            exit()

        # creating a button to exit program
        self.quit = tk.Button(self.master, text="Exit", padx=30, pady=8, command=end_calc)
        self.quit.pack()

        # calling method calculate
        self.calculate()

    # to make a loop so application runs until events occur
    def start(self):
        self.master.mainloop()

    # calculate method working definition
    def calculate(self, *args):

        # try if the values entered are numbers
        try:
            self.calc_result1 = self.input_variable1.get()
            self.calc_result2 = self.input_variable2.get()

        # or throw an error message
        except tk.TclError:
            self.result_value.set("Invalid input!")

        # if numbers are correct access this code
        else:
            if self.format_value.get() == 0:
                self.result_value.set("Result: "+f"{round(self.calc_result1+self.calc_result2, 2)}")
            elif self.format_value.get() == 1:
                self.result_value.set("Result: "+f"{round(self.calc_result1-self.calc_result2, 2)}")
            elif self.format_value.get() == 2:
                self.result_value.set("Result: "+f"{round(self.calc_result1*self.calc_result2, 2)}")
            else:
                self.result_value.set("Result: "+f"{round(self.calc_result1/self.calc_result2, 2)}")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Calculator")
    app = Calc(root)
    app.start()
