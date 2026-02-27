# Refactoring code from log_cleaner using Functions



def read_file(filename):
    with open(filename) as f:
        file_content = f.readlines()
        return file_content



def clean_lines(lines):
    new_lines = []
    for line in lines:
        clean = " ".join(line.strip().replace("\t", " ").split())
        if clean != "":
            new_lines.append(clean)
    return new_lines


def generate_report(original_lines, cleaned_lines):
    total_lines_read = len(original_lines)
    total_lines_cleaned = len(cleaned_lines)
    total_lines_removed = len(original_lines) - len(cleaned_lines)
    if total_lines_read == 0:
        percent_removed = 0
    else:
        percent_removed = round((total_lines_removed / total_lines_read *100), 2)
    info = {
        "read_lines": total_lines_read,
        "cleaned_lines": total_lines_cleaned,
        "removed_lines": total_lines_removed,
        "percent_removed": percent_removed,
    }
    return info



def write_file(filename, new_lines):
    with open(filename, "w") as f:
        for line in new_lines:
           f.write(line + "\n")






original = read_file("../day04/raw_log.txt")
cleaned = clean_lines(original)
report = generate_report(original, cleaned)
write_file("cleaned_log.txt", cleaned)
print(report)

