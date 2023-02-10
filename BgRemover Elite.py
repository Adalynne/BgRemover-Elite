import cv2
import numpy as np
import os


def remove_background(input_path, output_path):
    """
    This function removes the background of all images in the input path
    and saves the result images in the output path with transparent background.

    :param input_path: The path of the input directory containing the images
    :param output_path: The path of the output directory to save the result images
    :return: None
    """
    for file in os.listdir(input_path):
        filename, ext = os.path.splitext(file)
        if ext in [".jpg", ".jpeg", ".png"]:
            img = cv2.imread(os.path.join(input_path, file))
            if img is None:
                continue
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            mask = cv2.medianBlur(mask, 5)
            mask_inv = cv2.bitwise_not(mask)

            bg = np.zeros(img.shape, np.uint8)
            bg = cv2.bitwise_and(bg, bg, mask=mask)

            fg = cv2.bitwise_and(img, img, mask=mask_inv)
            result = cv2.add(bg, fg)

            result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
            result[:, :, 3] = mask

            cv2.imwrite(os.path.join(output_path, filename + ".png"), result)


def change_output_format(input_path, output_path, format):
    for file in os.listdir(input_path):
        filename, ext = os.path.splitext(file)
        if ext in [".jpg", ".jpeg", ".png"]:
            img = cv2.imread(os.path.join(input_path, file))
            if img is None:
                continue
            cv2.imwrite(os.path.join(output_path, filename + format), img)


def add_watermark(input_path, output_path, watermark_path):
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)
    watermark_height, watermark_width, _ = watermark.shape

    for file in os.listdir(input_path):
        filename, ext = os.path.splitext(file)
        if ext in [".jpg", ".jpeg", ".png"]:
            img = cv2.imread(os.path.join(input_path, file))
            if img is None:
                continue
            img_height, img_width, _ = img.shape
            result = img.copy()
            for i in range(0, img_height, watermark_height):
                for j in range(0, img_width, watermark_width):
                    result[i:i+watermark_height, j:j+watermark_width] = cv2.addWeighted(
                        result[i:i+watermark_height, j:j+watermark_width], 1, watermark, 0.3, 0)
