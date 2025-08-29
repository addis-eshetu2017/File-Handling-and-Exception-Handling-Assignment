def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.readlines()

        # Modify the content (for example, convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")
    except IOError:
        print(f"An error occurred while reading or writing files.")

# Example usage
input_file = 'input.txt'  # replace with your input file
output_file = 'output.txt'  # replace with your desired output file
read_and_modify_file(input_file, output_file)


# Error Handling Lab
def get_filename_from_user():
    filename = input("Please enter the filename: ")
    return filename

def read_user_file():
    filename = get_filename_from_user()
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError:
        print(f"An error occurred while trying to read the file.")

# Example usage
read_user_file()




