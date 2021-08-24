import os
from subprocess import *
import subprocess
 
os.chdir(os.path.dirname(__file__))
process1 = subprocess.Popen(["python", "hand tracking/hand_tracking.py"]) # Create and launch process pop.py using python interpreter
process2 = subprocess.Popen(["python", "game flappy bird/flappy_update.py"])

process1.wait() # Wait for process1 to finish (basically wait for script to finish)
process2.wait()
