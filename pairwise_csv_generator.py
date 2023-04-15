import itertools
import csv
import os
# Generate all possible combinations of 2 integers between 1 and 19 that sum to 20
combinations = []
for i in range(1, 10):
    j = 20 - i
    combinations.append((i, j))
for i in range(10, 20):
    j = 20 - i
    combinations.append((i, j))

# Define the number of rows per file
rows_per_file = 300

# Initialize the row counter and file counter
row_count = 0
file_count = 0

# Create the output directory if it doesn't exist
if not os.path.exists('pairwise_csvs'):
    os.makedirs('pairwise_csvs')

# Loop through each combination and write to a CSV file
for combination in combinations:
    ZIC = 0
    ZIP = 0
    GDX = 0
    AA = 0
    SHVR = combination[1]
    GVWY =  combination[0]
    combination = (ZIC,ZIP,GDX,AA,GVWY,SHVR)
    # Create a new file if the row count exceeds the threshold
    if row_count % rows_per_file == 0:
        # Close the previous file if it exists
        if file_count > 0:
            csvfile.close()

        # Open a new file for writing
        file_name = f'pairwise_csvs/GVWYvsSHVR.csv'
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
