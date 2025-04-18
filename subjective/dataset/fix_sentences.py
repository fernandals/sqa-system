import re

def reshape_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            parts = line.strip().split('|')
            
            filepath = parts[0]
            text = parts[1]
            
            match = re.match(r'.*/(\d+_\d+_\d+_\d+)\.wav', filepath)
            if match:
                new_id = match.group(1) 
                outfile.write(f"{new_id}|{text}\n")

input_file = 'dev_clean_400_samples.tsv'
output_file = 'test_sentences.txt'

reshape_file(input_file, output_file)
