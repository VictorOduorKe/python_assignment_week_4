def read_file(file_name):
    try:
        if not file_name:
            print("No file name provided.")
            return None
        with open(file_name,"r") as user_file:
            user_content=user_file.read()
            print("Content of the file:")
            print(user_content)
            return user_content
    except FileNotFoundError:
      print("The file name entered does not exist")
      return None
    
def modify_content(original_content):
    try:
        if original_content is None:
            original_content = ""
        modified_content = original_content.upper().replace("OLD_TEXT", "NEW_TEXT")
        return modified_content
    except Exception as e:
        print("Error occurred while modifying content:", e)
        return None


def write_modified_file(file_name, content):
    try:
        if content is None:
            content = ""
            print("No content to write, creating an empty file.")
            return
        with open(file_name, "w") as new_file:
         new_file.write(content)
         print("File written successfully")
    except FileNotFoundError as e:
        print("Error occurred while writing file:", e)
        return

original_content = read_file("original.txt")
modified_content = modify_content(original_content)
write_modified_file("modified.txt", content=modified_content)