from tkinter import *

# import messagebox from tkinter module
import tkinter.messagebox
  
# create a tkinter root window
root = tkinter.Tk(className=' HEXAWARE LOGIN')
  
# root window title and dimension

root.geometry('500x300')
#root.configure(bg='#C2DFFF')
#root.configure(bg='#FF69B4')
root.configure(bg='#7FFFD4')



# the label for user_name
user_name = Label(root,
                  text = "Username").place(x = 40,
                                           y = 60) 
# the label for user_password 
user_password = Label(root,
                      text = "Password").place(x = 40,
                                               y = 100)  

# Create a messagebox showinfo
  
def onClick():
    tkinter.messagebox.showinfo("Welcome to Hexaware",  "Log In Successfull!")
    messagebox.geometry('250x250')
    
# Create a Button
submit_button = Button(root,
                       text = "Log In", command=onClick).place(x = 110,
                                              y = 150)
user_name_input_area = Entry(root,
                             width = 30).place(x = 110,
                                               y = 60) 
   
user_password_entry_area = Entry(root,
                                 width = 30, show="*****").place(x = 110,
                                                   y = 100)
  
# Set the position of button on the top of window.
button.pack(side='bottom')

root.mainloop()
