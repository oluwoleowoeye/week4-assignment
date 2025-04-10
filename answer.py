# Step 1: Open the original file and read its content
input_file = open("original.txt", "r")  # Open for reading
content = input_file.read()             # Read the text
input_file.close()                      # Close the file

# Step 2: Modify the content (add "MODIFIED!")
new_content = content + "\nMODIFIED!"

# Step 3: Save to a new file
output_file = open("modified.txt", "w")  # Open for writing
output_file.write(new_content)           # Write the new text
output_file.close()                      # Close the file

print("File modified and saved as 'modified.txt'!")

filename = input("Enter a filename (e.g., 'test.txt'): ")

try:
    # Try to open and read the file
    file = open(filename, "r")
    content = file.read()
    file.close()
    print("\nFile content:")
    print(content)

except FileNotFoundError:
    print("Oops! That file doesn't exist.")
except:
    print("Something went wrong (maybe the file is corrupted?).")

print("Program finished.")