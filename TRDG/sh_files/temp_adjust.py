import re

def update_image_count(line, new_count):
    return re.sub(r'--image_count\s+\d+', f'--image_count {new_count}', line)

def update_c_value(line, c_value):
    return re.sub(r'-c\s+\d+', f'-c {c_value}', line)

def process_file(input_file, output_file, c_value):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        image_count = 0
        for line in infile:
            if line.strip().startswith('python trdg/run.py'):
                line = update_c_value(line, c_value)
                updated_line = update_image_count(line, image_count)
                outfile.write(updated_line)
                image_count += c_value
            else:
                outfile.write(line)

def main():
    # You can modify these values directly in the code
    input_file = '/home/scai/mtech/aib232080/scratch/trdg_2/sh_files/sample.sh'
    output_file = 'val_script_1.sh'
    c_value = 325  # Change this value as needed

    process_file(input_file, output_file, c_value)
    print(f"Processing complete. Updated script saved to {output_file}")

if __name__ == "__main__":
    main()