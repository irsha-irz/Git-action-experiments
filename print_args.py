import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read arguments from environment variables
args = os.getenv("ARGS", "")

# Split into list (assuming space-separated values)
args_list = args.split()

print("Arguments from .env file:", args_list)
