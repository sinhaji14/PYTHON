try:
    with open('takinginput.py/text.text') as file:
          print(file.read())

except FileExistsError:
      print("That file was not found :(")