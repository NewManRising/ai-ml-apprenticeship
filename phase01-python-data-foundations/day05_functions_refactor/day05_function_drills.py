# Simple Functions Warm-up


# Is the words even
def is_even(num):
    return num % 2 == 0

number = is_even(4)
print(number)

number2 = is_even(7)
print(number2)

# Calculating Average From List of Numbers
def calc_avg(x):
    return sum(x) / len(x)

digits = [2, 4, 1, 2, 5]
print(calc_avg(digits))

# Stripping Trailing And Leading Whitespace From a String and Converting To Lowercase
def clean_string(word):
    word = word.lower()
    word = word.strip()
    return word

print(clean_string("    HAPPY BIRTHDAY  "))

# Dictionary Of Word Counts

input_str = "Python is really cool"
input_str2 = "I am what I am and that is all that I am"

def count_words(text):
    words = text.lower().split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


print(count_words(input_str))
print(count_words(input_str2))


def normalize_scores(scores):
    if not scores:
        return []
    min_score, max_score = min(scores), max(scores)
    if min_score == max_score:
        return [0.0] * len(scores)
    return [(score - min_score) / (max_score - min_score) for score in scores]

raw_scores = [88, 77, 100, 82, 92, 95, 63]
print(normalize_scores(raw_scores))
