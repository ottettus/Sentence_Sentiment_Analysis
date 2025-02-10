from pathlib import Path 

base_dir = Path(__file__).resolve().parent

POSITIVE_FILES_DIR = base_dir / "testdata" / "train" / "pos"
NEGATIVE_FILES_DIR = base_dir / "testdata" / "train" / "neg"

positive_files = list(POSITIVE_FILES_DIR.glob("*.txt"))
negative_files = list(NEGATIVE_FILES_DIR.glob("*.txt"))

positive_reviews = []
negative_reviews = []

for file in positive_files:
    with open (file, mode='r', encoding='utf-8') as stream:
        content = stream.read()
        words = content.lower().replace('<br />', ' ').replace('.', ' ').split()
        positive_reviews.append(words)



for file in negative_files:
    with open (file, mode='r', encoding='utf-8') as stream:
        content = stream.read()
        words = content.lower().replace('<br />', ' ').replace('.', ' ').split()
        negative_reviews.append(words)

user_content = input("Wprowadź tekst do analizy: ")
words = user_content.lower().replace('<br />', ' ').replace('.', ' ').split()

sentence_sentiment = 0

for word in words:
    positive = 0
    negative = 0
    for pos_rev in positive_reviews:
        if word in pos_rev:
            positive +=1
    for neg_rev in negative_reviews:
        if word in neg_rev:
            negative +=1

    all_ = positive + negative
    if all_ != 0:
        word_s = (positive - negative) / all_
    else:
        word_s = 0.0
    print(word, word_s)

    sentence_sentiment += word_s

print("")
sentence_sentiment = sentence_sentiment / len(word)

result = ''

if sentence_sentiment > 0:
    result = 'positive'
else:
    result = 'negative'

print(f'This sentence is {result}, sentiment = {sentence_sentiment}')