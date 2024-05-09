import subprocess
print(" _      _                   _ _   _") 
print("(_)_  _(_)  _  ___  _   _| | |_(_)")
print("| \ \/ / | | '_ ` _ \| | | | | | |")
print("| |>  <| | | | | | | | |_| | | |_| |")
print("|_/_/\_\_| |_| |_| |_|\__,_|_|\__|_|")
print("\n")

message=input("What would you like to do?(1 or 2)\n1. Multiple Firefox\n2. Multiple Chrome\n\n")
if message=="1":
    def open_firefox(website_link):
        subprocess.Popen(["firefox", website_link])

# Get the number of instances from the user
    num_instances = int(input("Enter the number of Firefox instances: "))

# Get the website link from the user
    website_link = input("Enter the website link: ")

# Open multiple Firefox instances
    for _ in range(num_instances):
        open_firefox(website_link)

elif message=="2":
    def open_chrome(website_link):
        subprocess.Popen(["google-chrome", website_link])

# Get the number of instances from the user
    num_instances = int(input("Enter the number of Chrome instances: "))

# Get the website link from the user
    website_link = input("Enter the website link: ")

# Open multiple Chrome instances
    for _ in range(num_instances):
        open_chrome(website_link)
