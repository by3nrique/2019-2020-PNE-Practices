import pathlib

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Open and read the file
file_contents = pathlib.Path(FILENAME).read_text().split("\n")[1:]
body = "".join(file_contents)
# -- Print the contents on the console

print(len(body))

