from pathlib import Path

if __name__ == "__main__":
    # Path to the labels.txt file uploaded by the user - assuming a hypothetical path for demonstration
    labels_file_path = '/scratch/cs/imagedb/Jan/data/train/elsaesserstr1/labels.txt'

    # Read the intervals from the labels.txt file
    intervals = []
    with open(labels_file_path, 'r') as file:
        for line in file:
            start, end = map(int, line.strip().split(','))
            intervals.append((start, end))

    # Generate the dictionary with filenames as keys and class labels as values
    label_dict = {}
    for start, end in intervals:
        for i in range(start, end + 1):
            filename = f'{i:09d}'  # Pad the filename to have 9 digits
            label_dict[filename] = 1

    # Assuming we need to label all images up to a certain number, we find the max number
    max_image_number = 3895

    # Fill in the rest of the images with class 0
    for i in range(0, max_image_number + 1):
        filename = f'{i:09d}'
        if filename not in label_dict:
            label_dict[filename] = 0

    # Save the dictionary to a new txt file
    output_file_path = '/scratch/cs/imagedb/Jan/customdata/elsaesserstr1/labels.txt'
    with open(output_file_path, 'w') as file:
        for filename, label in sorted(label_dict.items(), key=lambda x: int(x[0])):
            file.write(f'{filename},{label}\n')

    print(f'Wrote new labels in {output_file_path}')