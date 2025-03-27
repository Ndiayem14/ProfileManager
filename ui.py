import tkinter as tk
class Profile:
    '''
    Uses the constructor method to construct instance variables that the user's profile is going to be made of
    :return: none
    '''
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

class Application(tk.Tk):
    def __init__(self):
        '''
        Constructs the GUI using Tkinter
        '''
        super().__init__()      #  initializes the Tkinter library and sets up the main window for the GUI
                                # before the Application class customizes it.

        # define the window geometry
        self.title("Sign Up")
        self.geometry("600x500")

        # create the window frame
        self.frame = tk.Frame(self, bg='#6997EE')
        self.frame.place(relx= 0, rely=0, relheight= 3, relwidth=2)

        # Creating widgets
        self.big_label = tk.Label(self.frame, text = "Sign Up", font='Helvetica 20 bold', bg= 'light gray')
        self.big_label.place(relx=0.09, rely=0.01,  relheight=0.03, relwidth=0.3)
        self.name_label = tk.Label(self.frame, text="Names:", font = "Helvetica 10 bold")
        self.name_label.place(relx= 0.01, rely=0.0509)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.place(relx= 0.085, rely=0.0509)
        self.age_label = tk.Label(self.frame, text="Age:", font = "Helvetica 10 bold")
        self.age_label.place(relx= 0.01, rely=0.066)
        self.age_entry = tk.Entry(self.frame)
        self.age_entry.place(relx= 0.085, rely=0.066)
        self.gender_label = tk.Label(self.frame, text="Gender:", font = "Helvetica 10 bold")
        self.gender_label.place(relx= 0.01, rely=0.081)
        self.gender_entry = tk.Entry(self.frame)
        self.gender_entry.place(relx= 0.085, rely=0.081)
        self.occupation_label = tk.Label(self.frame, text="Email:", font = "Helvetica 10 bold" )
        self.occupation_label.place(relx= 0.01, rely=0.0965)
        self.occupation_entry = tk.Entry(self.frame)
        self.occupation_entry.place(relx= 0.085, rely=0.0965)
        self.submit_button = tk.Button(self.frame, text="Submit", font = "Helvetica 10 bold", bd = 3, command=self.save_profile)
        self.submit_button.place(relx= 0.15, rely=0.14)
        self.view_button = tk.Button(self.frame, text="View", font = "Helvetica 10 bold", bd = 3, command=self.search_profile)
        self.view_button.place(relx= 0.23, rely=0.14)

    def save_profile(self):
        '''
        Saves the user's input
        :return: None
        '''
        name = self.name_entry.get()    # gets whatever is inputted in the entry box
        age = self.age_entry.get()       # gets whatever is inputted in the entry box
        gender = self.gender_entry.get()   # gets whatever is inputted in the entry box
        occupation = self.occupation_entry.get()  # gets whatever is inputted in the entry box

        profile = Profile(name, age, gender, occupation)
        with open('profiles.txt', 'a') as info:           # opens a empty txt file append the user's input every time they hit "submit"
                                                          # And the file is closed automatically
            info.write(f"{profile.name},{profile.age},{profile.gender},{profile.occupation}\n")  # the user's entries are saved as one long string

    # tk.End clears the entry box when the user hits the save button
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.occupation_entry.delete(0, tk.END)

    def popupmsg(self):
        '''
        Creates a pop-up message asking the user to enter a valid keyword to be searched
        :return:none
        '''
        self.popup = tk.Tk()      #
        self.popup.wm_title('Warning!')
        self.label = tk.Label(self.popup, text= "Please enter a valid keyword: a name, age,...!", fg= "Red", font="Helvetica 10 bold")
        self.label.pack(side="top", fill="x", pady=10)
        self.B1 = tk.Button(self.popup, text="Okay", font ="Helvetica 10 bold", bg = 'Yellow', bd = 3, command=self.popup.destroy)
                                                                    # the pop up window gets destroyed when the user hits the "okay" bitton
        self.B1.pack()             # puts the pop-up on the screen


    def view_profile(self):
        '''
        pulls up the user profile based on the entered keyword
        :return: None
        '''

        self.top2 = tk.Toplevel(self)               # create a new window
        self.top2.title("Your Profile")
        self.top2.geometry('600x500')
        with open('profiles.txt', 'r') as f:
            for line in f:
                if self.button_entry.get() in line:
                        name, age, gender, occupation = line.split(',')
                        profile_label = tk.Label(self.top2, text=f"Name: {name} \n Age: {age}\n Gender: {gender} \n Occupation: {occupation}", font= 10)
                        profile_label.pack()
                        return None
            if self.button_entry.get() not in f:
                self.popupmsg()
                self.top2.destroy()


    def search_profile(self):
        '''
         searches the user's profile by keywords.
        :return: None
        '''

        self.top = tk.Toplevel(self)              # creates a new screen
        self.top.title("Search")
        self.top.geometry('600x50')
        self.button_label= tk.Label(self.top, text = "Keyword:", font = "Helvetica 10 bold")
        self.button_label.place(relx=0.03, rely=0.01)
        self.button2_label = tk.Label(self.top, text="", font="Helvetica 10 bold")
        self.button2_label.place(relx=0.15, rely=0.47)
        self.button_entry = tk.Entry( self.top, width=22)
        self.button_entry.place(relx=0.19, rely=0.01)
        self.okay = tk.Button(self.top, text="OK", font = "Helvetica 10 bold", command=self.view_profile)
        self.okay.place(relx=0.43, rely=0.01)                  # the view_profile method is triggerd when the "ok" buttin is clicked.

def main():
    '''
    Creates the app object
    :return: None
    '''
    if __name__ == '__main__':
        app = Application()
        app.mainloop()

main()

