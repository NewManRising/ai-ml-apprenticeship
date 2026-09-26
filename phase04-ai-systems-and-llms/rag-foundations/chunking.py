with open("docs/mountains.txt", "r") as f:
    text = f.read()

with open("docs/mountains.txt", "r") as f:
    text = f.read()


def chunk_text(text, chunk_size=300, overlap=50):
    list_of_chunks = []
    start = 0

    while start < len(text):
        chunk = text[start: start + chunk_size]
        list_of_chunks.append(chunk)
        start = start + (chunk_size - overlap)

    return list_of_chunks


print(chunk_text(text))


#text = "Hello, World!"
# Iterate over characters from index 0 to 5 ("Hello")
#for char in text[0:5]:
    #print(char)