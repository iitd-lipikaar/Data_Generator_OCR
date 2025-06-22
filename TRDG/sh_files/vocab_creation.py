input_file = r"/home/scai/mtech/aib232080/scratch/trdg_2/trdg/dicts/hindi.txt"    # your input file
output_file = "unique_hindi.txt"  # output file with unique words

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Split text into words using whitespace and remove duplicates using set
words = set(text.split())

# Sort words (optional)
unique_words = sorted(words)

with open(output_file, "w", encoding="utf-8") as f:
    for word in unique_words:
        f.write(word + "\n")

print(f"Saved {len(unique_words)} unique words to {output_file}")
