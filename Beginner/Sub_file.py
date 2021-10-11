# importing os module 
import os
import pprint
  
# Get the list of user's
# environment variables
env_var = os.environ
  
# Print the list of user's
# environment variables
home = os.environ['HOME']
  
# Print the value of
# 'HOME' environment variable
print("HOME:", home)