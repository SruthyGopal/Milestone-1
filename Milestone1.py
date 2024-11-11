import pandas as pd
from collections import Counter
import re

# Load the CSV file to DataFrame
df = pd.read_csv(r'C:\Users\Administrator\Desktop\UST_Training\Assessment\sample_csv.csv','r')

text_data = ' '.join(df.astype(str).values.flatten())
format_text = re.sub(r'[^\w\s]','', text_data.lower())

# Split the text into individual words
words = format_text.split()

# Count the frequency of each word
word_frequencies = Counter(words)

# Convert the frequencies to a pandas DataFrame for easier viewing
word_freq_df = pd.DataFrame(word_frequencies.items(), columns=['Word', 'Frequency'])

print(word_freq_df)
