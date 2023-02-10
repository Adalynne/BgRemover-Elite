# Image Processing Tools
## Description
- The code only works with image files that have extensions of .jpg, .jpeg, and .png.
- The function assumes that the input images are in BGR color space.
- The function uses Otsu's thresholding to automatically determine the threshold value for the binary mask. This method may not work well for all images, and a manual - threshold value may need to be set in some cases.
This script contains 3 functions to perform different image processing tasks.

## Function 1: `remove_background`

This function removes the background of an image. The input is a directory containing the images, and the output is a directory where the processed images will be saved. The function takes 3 arguments:

`input_path`: Path to the directory containing the images.

`output_path`: Path to the directory where the processed images will be saved.

## Function 2: `change_output_format`

This function changes the format of the output images. The input is a directory containing the images, and the output is a directory where the processed images will be saved. The function takes 3 arguments:


`input_path`: Path to the directory containing the images.

`output_path`: Path to the directory where the processed images will be saved.

`format`: The format of the output images, including '.jpg', '.jpeg' or '.png'.

## Function 3: `add_watermark`

This function adds a watermark to the images. The input is a directory containing the images, and the output is a directory where the processed images will be saved. The function takes 4 arguments:


`input_path`: Path to the directory containing the images.

`output_path`: Path to the directory where the processed images will be saved.

`watermark_path`: Path to the watermark image.



## Contributing
Contributions are welcome and appreciated. If you have any ideas for new features or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

