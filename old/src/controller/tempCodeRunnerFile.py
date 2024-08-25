import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

# Add the 'src' directory to sys.path
sys.path.append(os.path.join(current_directory, '..'))
sys.path.insert(0, os.path.join(current_directory, '..'))
print(sys.path)