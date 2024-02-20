from PIL import Image
import os

def create_combined_image(n_size, folder):
    """
    Combines an RGB image with 6 related spectrogram images into a single nxn image.

    Parameters:
    - n_size: The size of the combined nxn image.
    - folder: Folder name where RGB images are stored.

    The function expects filenames to be in a sequential format like 000000000, 000000001, etc.
    """
    # Create a new blank image with the specified size n_size x n_size
    combined_image = Image.new('RGB', (n_size, n_size), (255, 255, 255))

    # Load the RGB image and resize it to fit n/2 width and n/2 height
    rgb_image_list = os.listdir(folder + '/cam0_rectified')

    for image in rgb_image_list:
        image_number = image.split('_')[1]
        rgb_image_path = os.path.join(folder, 'cam0_rectified', image)
        rgb_image = Image.open(rgb_image_path).resize((n_size, n_size//3))
        combined_image.paste(rgb_image, (0, 0))
        print(image_number)
        print(rgb_image_path)

        for i in range (0, 6):
            spec_image_path = os.path.join(folder, f'spec{i + 1}-1.0', f'{image_number}.png')
            spec_image = Image.open(spec_image_path).resize((n_size, n_size//9))
            combined_image.paste(spec_image, (0, (n_size//3 ) + ((n_size//9) * i)))

        output_folder_path = f'/scratch/cs/imagedb/Jan/customdata/{folder.split("/")[-1]}'
        os.makedirs(output_folder_path, exist_ok=True)
        combined_image.save(f'{output_folder_path}/{image_number}.jpg')



    # rgb_image_path = os.path.join(rgb_folder, rgb_image_list[0])  # Assume first image for demonstration
    # rgb_image = Image.open(rgb_image_path).resize((n_size//2, n_size//2))

    # # Place the RGB image in the top-left corner
    # combined_image.paste(rgb_image, (0, 0))

    # # Calculate each spectrogram's target size (n/2 width, n/4 height) and position
    # spec_width = n_size // 2
    # spec_height = n_size // 4 // 6  # Divide the height equally among 6 spectrograms
    # for index, folder in enumerate(spectrogram_folders):
    #     spectrogram_image_list = os.listdir(folder)
    #     spectrogram_image_path = os.path.join(folder, spectrogram_image_list[0])  # Assume first image for demo
    #     spectrogram_image = Image.open(spectrogram_image_path).resize((spec_width, spec_height))

    #     # Calculate y position for each spectrogram
    #     y_position = n_size // 2 + (spec_height * index)

    #     # Place each spectrogram image in the bottom half, stacked vertically
    #     combined_image.paste(spectrogram_image, (n_size // 2, y_position))

    # # For demonstration purposes, we'll return the combined image without saving it
    # return combined_image


if __name__ == "__main__":
    rgb_dir = "/scratch/cs/imagedb/Jan/data/train/elsaesserstr1"
    create_combined_image(256, rgb_dir)