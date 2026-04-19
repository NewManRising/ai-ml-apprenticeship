# Reading, cleaning, and saving messy file

with open("raw_log.txt") as f:
    file_contents = f.readlines()
    print(file_contents)


print(len(file_contents))


# A new list, removing leading/trailing whitespace, spaces between words, and empty strings
new_list = []

for line in file_contents:
    cleaned_line = " ".join(line.strip().replace("\t"," ").split())
    if cleaned_line != "":
        new_list.append(cleaned_line)

print(new_list)

# Saving cleaned file
with open("cleaned_log.txt", "w") as nf:
    for line in new_list:
        nf.write(line + "\n")
        print(line)
