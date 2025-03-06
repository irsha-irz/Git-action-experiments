import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read arguments from environment variables
args = os.getenv("ARGS", "")

# Split into list (assuming space-separated values)
args_list = args.split()

output_text = f"Arguments from .env file: {args_list}\n"

# Write to a file
with open("output.txt", "w") as f:
    f.write(output_text)

print("Output saved to output.txt")
