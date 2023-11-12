import os
import sys

def delete_self():
    try:
        os.remove(sys.argv[0])
    except Exception as e:
        print(f"Failed to delete the executable: {e}")

# Your script logic here

# After completing your script logic, call the delete_self function to delete the executable.
delete_self()
