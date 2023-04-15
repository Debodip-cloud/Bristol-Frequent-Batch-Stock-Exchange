import itertools
import csv
import os

# Generate all possible combinations of 4 integers between 0 and 5
combinations = itertools.product(range(6), repeat=2)

# Define the number of rows per file
rows_per_file = 300

# Initialize the row counter and file counter
row_count = 0
file_count = 0

# Create the output directory if it doesn't exist
# if not os.path.exists('possible_combinations'):
#     os.makedirs('possible_combinations')

# Loop through each combination and write to a CSV file
for combination in combinations:
    # Add 3 trailing 0s to the combination
    ZIC = 0
    ZIP = 0
    GDX = combination[0]
    AA = 0
    SHVR = 0 
    GVWY = combination[1]
    combination = (ZIC,ZIP,GDX,AA,GVWY,SHVR)

    # Check if the sum of the combination is greater than or equal to 2
    if sum(combination) >= 2:
        # Create a new file if the row count exceeds the threshold
        if row_count % rows_per_file == 0:
            # Close the previous file if it exists
            if file_count > 0:
                csvfile.close()

            # Open a new file for writing
            file_name = f'test_combinations.csv'
            csvfile = open(file_name, 'w', newline='')
            writer = csv.writer(csvfile)

            # Increment the file counter
            file_count += 1

        # Write the combination as a row in the CSV file
        writer.writerow(combination)

        # Increment the row counter
        row_count += 1

# Close the last file
csvfile.close()
