#!/bin/bash

FILE="input_file.txt"  # Update with your input file path
COMMAND="python run_model.py -mode cli -task joint -model_checkpoint kevinscaria/joint_tk-instruct-base-def-pos-neg-neut-combined -test_input"  # Update with your desired command

while IFS= read -r line; do
    $COMMAND "$line"
done < "$FILE"
