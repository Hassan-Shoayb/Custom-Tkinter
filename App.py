import customtkinter
import os
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter")
        self.geometry("700x450")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "softlinks_logo.png")), size=(40, 40))
        self.large_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_image.png")), size=(500, 320))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chats_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.users_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "users_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "users_light.png")), size=(20, 20))
        
        # create navigation bar
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_label = customtkinter.CTkLabel(
            self.navigation_frame, 
            text="  Softlinks", 
            image=self.logo_image,
            compound="left", 
            font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.navigation_label.grid(row=0, column=0, padx=20, pady=20)
        
        self.home_button = customtkinter.CTkButton(
            self.navigation_frame, 
            corner_radius=0, 
            height=40, 
            border_spacing=10, 
            text="Home",
            fg_color="transparent", 
            text_color=("gray10", "gray90"), 
            hover_color=("gray70", "gray30"),
            image=self.home_image, 
            anchor="w"
        )
        self.home_button.grid(row=1, column=0, sticky="ew")
        
        self.chats_button = customtkinter.CTkButton(
            self.navigation_frame, 
            corner_radius=0, 
            height=40, 
            border_spacing=10, 
            text="Chats",
            fg_color="transparent", 
            text_color=("gray10", "gray90"), 
            hover_color=("gray70", "gray30"),
            image=self.chats_image, 
            anchor="w"
        )
        self.chats_button.grid(row=2, column=0, sticky="ew")
        
        self.users_button = customtkinter.CTkButton(
            self.navigation_frame, 
            corner_radius=0, 
            height=40, 
            border_spacing=10, 
            text="Users",
            fg_color="transparent", 
            text_color=("gray10", "gray90"), 
            hover_color=("gray70", "gray30"),
            image=self.users_image,
            anchor="w"
        )
        self.users_button.grid(row=3, column=0, sticky="ew")
        
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.navigation_frame, 
            text="Appearance Mode:", 
            anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0)
        
        self.appearance_mode = customtkinter.CTkOptionMenu(
            self.navigation_frame, 
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="s")
    
        # Create Frame for Design
        self.img_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.img_frame.grid(row=0, column=1, sticky="nsew")

        self.img_label = customtkinter.CTkLabel(
            self.img_frame, 
            text="", 
            image=self.large_image
        )
        self.img_label.grid(row=0, column=0)
    
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()