readme_file = open("readme.txt", "r+")

print(readme_file.read())

readme_file.write("I'm outside the door")

readme_file.close()

