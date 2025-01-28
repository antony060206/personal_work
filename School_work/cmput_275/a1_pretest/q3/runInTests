#!/usr/bin/bash

command_arg="$1"
test_set_file="$2"

while read -r stem; do 
    # Run the command and capture its output
    x=$(${command_arg} < "${stem}.in")

    # Create a temporary file
    temp_file=$(mktemp)

    # Write the command's output to the temporary file
    echo "$x" > "$temp_file"

    # Compare the temporary file with the expected output
    if diff "$temp_file" "${stem}.out" > /dev/null; then
        echo "Test ${stem} passed"
    else
        echo "Test ${stem} failed"
        echo "Expected output:"
        cat "${stem}.out"
        echo "Actual output:"
        cat "$temp_file"
    fi

    # Remove the temporary file
    rm "$temp_file"
done < "$test_set_file"


