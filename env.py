import subprocess
import os

current_directory = os.getcwd()
directory_path = r'"C:\Your\Directory\Path"'
command = f'setx PATH "%PATH%;{current_directory}" /M'
subprocess.run(command, shell=True, check=True)
