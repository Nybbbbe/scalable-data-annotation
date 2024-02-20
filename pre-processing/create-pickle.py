import os
import pickle
from PIL import Image
import numpy as np

def create_cifar_like_pickle(data_folder):
    labels_file_path = os.path.join(data_folder, 'labels.txt')
    image_files_with_labels = []

    # Read labels and filenames
    with open(labels_file_path, 'r') as file:
        for line in file:
            filename, label = line.strip().split(',')
            image_files_with_labels.append((filename, int(label)))

    # Process images and labels for the dataset
    data = []
    labels = []
    for filename, label in image_files_with_labels:
        image_path = os.path.join(data_folder, f'{filename}.jpg')
        image = Image.open(image_path)
        # image = image.resize((32, 32))  # Resizing to CIFAR-10 image dimensions
        np_image = np.array(image)
        if len(np_image.shape) == 2:  # Convert grayscale to RGB if necessary
            np_image = np.stack([np_image]*3, axis=-1)
        np_image = np_image.transpose((2, 0, 1)).reshape(-1)
        data.append(np_image)
        labels.append(label)

    data = np.array(data, dtype=np.uint8)
    labels = np.array(labels, dtype=np.uint8)

    # Create a dictionary like CIFAR-10's structure
    cifar_like_dict = {
        'data': data,
        'labels': labels.tolist(),
    }

    # Save as a pickle file
    output_pickle_path = os.path.join(data_folder, 'custom_cifar_like_dataset.pickle')
    with open(output_pickle_path, 'wb') as f:
        pickle.dump(cifar_like_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"Dataset created and saved to {output_pickle_path}")

if __name__ == "__main__":
    data_folder = '/scratch/cs/imagedb/Jan/customdata/elsaesserstr1'
    create_cifar_like_pickle(data_folder)