def generate_paths(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            file_id = line.split('|')[0]
            paths = [
                f"datasets/ground_truth/{file_id}.wav",
                f"datasets/tts1/{file_id}.wav",
                f"datasets/tts2/{file_id}.wav",
                f"datasets/tts3/{file_id}.wav"
            ]
            outfile.write(f"{file_id}|{'|'.join(paths)}\n")

input_file = 'test_sentences.txt'
output_file = 'metadata.txt'

generate_paths(input_file, output_file)
