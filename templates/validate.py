import os
import re
import yaml

# Define folder path
folder_path = "."


def validate_file():
    # Load YAML file
    with open(os.path.join(folder_path, filename), "r") as f:
        data = yaml.safe_load(f)
    # Find all keys in square brackets in strings
    keys_in_strings = set(
        re.findall(
            r"\[(\w+)\]", data["to"] + data["opening"] + data["subject"] +
            data["body"] + data["closing"]))
    # Check that all keys in strings are listed in params
    for key in keys_in_strings:
        if not any(param.get("key") == key for param in data["params"]):
            raise ValueError(
                f"Error in {filename}: placeholder [{key}] in strings but not listed in params."
            )

    # Check that all keys listed in params occur in strings above
    for param in data["params"]:
        key = param.get("key")
        if key not in keys_in_strings:
            raise ValueError(
                f"Error in {filename}: parameter {key} defined but not found in strings."
            )


# Loop through all YAML files in folder
for filename in os.listdir(folder_path):
    if filename.endswith(".yaml"):
        validate_file()
