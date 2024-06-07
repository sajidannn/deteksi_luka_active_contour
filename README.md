# Wound Classification

## Overview

This project provides a Python program to classify wounds using image segmentation techniques such as Active Contour and Mask Fill Poly, and a Decision Tree model for classification. The main steps involve image segmentation to identify wound areas, extracting relevant features, and using these features to classify wounds into different types such as cuts, burns, punctures, and bruises.

## Features

- **Image Segmentation:** Using Active Contour to isolate wound areas from the background.
- **Masking:** To accurately obtain the entire wound area, extracting features like average RGB values, area size, and shape.
- **Classification:** Utilizing a Decision Tree model to classify the wound types based on the extracted features.

## Usage

### Clone the repository:

```bash
git clone https://github.com/sajidannn/deteksi_luka_active_contour.git
```

### Installation

To run this project, you need to have Python installed on your system. Follow these steps to install the necessary libraries:

```bash
pip install opencv-python matplotlib numpy pandas scikit-image scikit-learn
```

## Example

Here's an example of how the segmentation works. On the left, you see the original wound image. On the right, the result of the segmentation using Active Contour, with the white curve following the wound's edge.

![Example Segmentation](https://drive.google.com/file/d/1XZS96-y68lbu7LcmMvMbpTYlUX4f_nQO/view?usp=drive_link)

After segmentation, the image is masked using the fillpoly mask technique.

![Example Masking](https://drive.google.com/file/d/1XgZxPE-WTIXAbAII61KoXGcQlGymtL8_/view?usp=drive_link)

## Steps

1. **Segment the wound area:** Using Active Contour to differentiate the wound from the background.
2. **Masking and feature extraction:** Apply masking to get the wound area, and extract features like average RGB values, area size, and shape.
3. **Classification:** Use the Decision Tree model to classify the wound based on extracted features.


## License

This project is licensed under the MIT License.
