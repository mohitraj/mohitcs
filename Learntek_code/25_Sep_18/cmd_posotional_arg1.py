import argparse

parser = argparse.ArgumentParser() 

#parser.add_argument("Learntek")  # Add arguments Positional 

parser.add_argument("Learntek", help="Get the square of the number ", type = int)  # Add arguments Positional 


arg = parser.parse_args()  # All arguments 

print (arg.Learntek**2)  # Positional arguments