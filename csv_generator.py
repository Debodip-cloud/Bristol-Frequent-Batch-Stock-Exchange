import os
import itertools
import csv

# Generate all possible combinations of 6 integers between 0 and 5
combinations = itertools.product(range(6), repeat=6)

# Define the number of rows per file
rows_per_file = 1000

# Initialize the row counter and file counter
row_count = 0
file_count = 0

# Create the output directory if it doesn't exist
if not os.path.exists('possible_combinations'):
    os.makedirs('possible_combinations')

# Loop through each combination and write to a CSV file
for combination in combinations:
    # Create a new file if the row count exceeds the threshold
    if row_count % rows_per_file == 0:
        # Close the previous file if it exists
        if file_count > 0:
            csvfile.close()

        # Open a new file for writing
        file_name = f'possible_combinations/combinations_{file_count}.csv'
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
