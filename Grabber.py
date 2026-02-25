import subprocess
import os

cmd = "netsh wlan show profile key=clear"
result = subprocess.run(cmd, capture_output=True, text=True, shell=True, check=True)

lines = result.stdout.splitlines()

for line in lines:
    if "All User Profile" in line:
        print(f"You can find the Password of: "+line.split(":")[1].strip())

while True:
    try:
        wifi = input("Enter the Wifi name you want to find the Password of: ")
        cmd = f"netsh wlan show profile name="+wifi+" key=clear"
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True, check=True)
        break
    except subprocess.CalledProcessError:
        print("Wifi isn't saved!")

lines = result.stdout.splitlines()

for line in lines:
    if "Key Content" in line:
        password = line.split(":")[1].strip()
        print(f"The Password is: "+password)
        break
else:
    pass

while True:
    try:
        perm = int(input(f"Do you want to create a .txt file in "+"( "+os.getcwd()+" )"+" for "+wifi+"(1 for Yes, 2 for No): "))
        break
    except ValueError:
        print("1 for Yes, 2 for No")

if perm == 1:
    f = wifi+"_Password"
    with open(f,"w") as file:
        file.write(password)
        print("File Created!")
else:
    print("Thank You!")
