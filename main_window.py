import tkinter as tk
import tkinter.ttk as ttk
from User_interface import main_window, homeFrame, StandingsFrame, PlayersFrame, statsFrame, adminFrame
from userUtilities import Login, Register
from tkinter import messagebox


class MyApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title("PSHS FIFA Database")
        # Create instance of DefaultFrame
        self.main_window = main_window(self.master)
        self.main_window.grid(row=0, column=0, sticky="nsew")
        self.disable_navigation_buttons()

        # Store a reference to the content frame in the MyApp instance
        self.main_window.admin_button.configure(command=self.show_admin)
        self.main_window.standings_button.configure(command=self.show_standings)
        self.main_window.player_button.configure(command=self.show_players)
        self.main_window.stats_button.configure(command=self.show_stats)
        
        # Store login settings
        def login_button():
            username = self.main_window.username_entry.get()
            password = self.main_window.password_entry.get()
            
            # Validate the login
            login = Login()
            if login.check_Login(username, password):
                # Login successful, show the catalogue frame
                self.show_home()
                self.enable_navigation_buttons()
                self.main_window.standings_button.configure(state="normal")
                self.main_window.player_button.configure(state="normal")
                self.main_window.stats_button.configure(state="normal")
                
                if login.is_admin:
                    self.main_window.admin_button.configure(state="normal")
                    print("Admin Recongnised")
                else:
                    self.main_window.admin_button.configure(state="disabled")
            else:
                messagebox.showerror("error", "Invalid Login Credentails")
                        
        def signup_button_clicked():
            username = self.main_window.username_entry.get()
            password = self.main_window.password_entry.get()

            # Check if username and password are not empty
            if username and password:
                # Create a Register instance
                register = Register()
                # Attempt to register the user
                if register.register_user(username, password):
                    # Registration successful
                    messagebox.showinfo("Success", "User registered successfully")
                else:
                    # User already exists
                    messagebox.showerror("Error", "User already exists.")
            else:
                # Username or password is empty
                messagebox.showerror("Error", "Please enter a username and password.")
                
        self.main_window.login_button.configure(command=login_button)
        self.main_window.signup_button.configure(command=signup_button_clicked)
    
        # Check if the user is an admin and enable the admin button if necessary
        # Navigation buttons and additions to the default_frame.content_frame
    def disable_navigation_buttons(self):
        # Disable all navigation buttons
        self.main_window.standings_button.configure(state="disabled")
        self.main_window.player_button.configure(state="disabled")
        self.main_window.stats_button.configure(state="disabled")
        self.main_window.admin_button.configure(state="disabled")
        ("Navigation Disabled")
        
    def enable_navigation_buttons(self):
        # Enable all navigation buttons
        self.main_window.standings_button.configure(state="normal")
        self.main_window.player_button.configure(state="normal")
        self.main_window.stats_button.configure(state="normal")
        #self.main_window.admin_button.configure(state="normal")
        print("Navigation Enabled")
        
    def show_home(self):
        self.main_window.contentFrame.grid_remove()
        self.main_window.contentFrame = homeFrame(self.main_window)
        self.main_window.contentFrame.grid(column=1, row=1, sticky="nsew")
        
    def show_standings(self):
        self.main_window.contentFrame.grid_remove()
        self.main_window.contentFrame = StandingsFrame(self.main_window)
        self.main_window.contentFrame.grid(column=1, row=1, sticky="nsew")
        
    def show_players(self):
        self.main_window.contentFrame.grid_remove()
        self.main_window.contentFrame = PlayersFrame(self.main_window)
        self.main_window.contentFrame.grid(column=1, row=1, sticky="nsew")
        
    def show_stats(self):
        self.main_window.contentFrame.grid_remove()
        self.main_window.contentFrame = statsFrame(self.main_window)
        self.main_window.contentFrame.grid(column=1, row=1, sticky="nsew")
        
    def show_admin(self):
        self.main_window.contentFrame.grid_remove()
        self.main_window.contentFrame = adminFrame(self.main_window)
        self.main_window.contentFrame.grid(column=1, row=1, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
