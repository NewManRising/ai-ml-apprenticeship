#---------------------------------------------------------------------------------------#
# Python - File Input/Output                                                            #
# Text(.txt) and CSV (.csv) files                                                       #
#---------------------------------------------------------------------------------------#


# Reading text file
with open("notes.txt", 'r') as f:
    lines = f.readlines()
    print(lines)


print(len(lines))
print(lines[0]) # first line
print(lines[-1]) # last line


# Writing a copy of the original text file
with open("notes_copy.txt", "w") as nf:
    for line in lines:
        nf.write(line)


# Creating a copy of an image
with open("cat.jpg", "rb") as r_img:
    with open("cat_copy.jpg", "wb") as w_img:
        for line in r_img:
            w_img.write(line)


