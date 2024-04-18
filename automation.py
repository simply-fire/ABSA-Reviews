import subprocess
import os


def run_commands_from_file(file_path, command):
    with open(file_path, "r") as file:
        statements = file.read().splitlines()
        for statement in statements:
            os.system(command + f'"{statement}"')


# if __name__ == "__main__":
file_path = "input_file.txt"  # Update with your input file path
command = "python run_model.py -mode cli -task joint -model_checkpoint kevinscariajoint_tk-instruct-base-def-pos-neg-neut-combined -test_input "  # Update with your desired command
run_commands_from_file(file_path, command)
