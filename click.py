import sys
from termcolor import colored, cprint
import subprocess
cprint(" _      _                   _ _   _", attrs=["reverse", "blink"]) 
cprint("(_)_  _(_)  _  ___  _   _| | |_(_)", "blue",  attrs=["reverse", "blink"])
cprint("| \ \/ / | | '_ ` _ \| | | | | | |", "white",  attrs=["reverse", "blink"])
cprint("| |>  <| | | | | | | | |_| | | |_| |", "white",  attrs=["reverse", "blink"])
cprint("|_/_/\_\_| |_| |_| |_|\__,_|_|\__|_|", "blue",  attrs=["reverse", "blink"])
cprint("coded by: ixink(Rayhan Ahmed)", "blue",  attrs=["reverse", "blink"])
cprint("contact me: linkedin.com/in/rayah-ahmed-uiu", "blue",  attrs=["reverse", "blink"])
cprint("____________________________________________", "blue",  attrs=["reverse", "blink"])
print("\n")
cprint("What would you like to start? Choose 1 or 2\n\n ", "white", "on_green")
textq1 = colored("1 Multi FireFox\n\n2 Multi Chrome\n\n", "green", "on_white") 
texti = colored(" How many time:\n  ", "white", "on_blue")
textj = colored(" Enter the website link:\n", "white", "on_green")
message = input(textq1)
if message=="1":
    def open_firefox(website_link):
        subprocess.Popen(["firefox", website_link])

# Get the number of instances from the user
    num_instances = int(input(texti))

# Get the website link from the user
    website_link = input(textj)

# Open multiple Firefox instances
    for _ in range(num_instances):
        open_firefox(website_link)

elif message=="2":
    def open_chrome(website_link):
        subprocess.Popen(["google-chrome", website_link])

# Get the number of instances from the user
    num_instances = int(input(texti))

# Get the website link from the user
    website_link = input(textj)

# Open multiple Chrome instances
    for _ in range(num_instances):
        open_chrome(website_link)
