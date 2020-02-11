from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text().split("\n")[1:]
body = "\n".join(file_contents)
# -- Print the contents on the console

print(body)
