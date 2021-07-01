def about():
    messagebox.showinfo('About'," \n CALCULATOR \n Created by NOT A PRO CODERS")

def click_button(item):                                           # 'click_button' function continuously updates the input field whenever you enters a number
    global expression
    inputText.set(inputText.get()+(str(item)))

def clear_button():                                               # 'clear_button' function clears the last input item
    global expression
    expression = " "
    inputText.set(inputText.get()[0:-1])

def clear_all():                                                  # 'clear_all' function clears the input field
    inputText.set(" ")
