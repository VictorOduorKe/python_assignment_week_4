try:
    with open("original.txt","r") as original_file:
        content=original_file.read()
        modify_content=content.upper()
        new_file_name="modified.txt"
        with open(new_file_name, "w") as new_file:
            new_file.write(modify_content)
            if new_file:
                print("File written successfully")
except FileNotFoundError:
    print("File not found")


#user file name input
try:
    user_input_file=input("Enter the file Name")
    if user_input_file:
        with open(user_input_file,"r") as user_file:
            user_content=user_file.read()
            print("Content of the file:")
            print(user_content)
            user_file.close()
except FileNotFoundError:
    print("The file name entered does not exist")
finally:
    print("End of file handling operations")
    if 'user_file' in locals():
        user_file.close()