# qrcode_generator
Generate QR code that encodes a user-defined input. The QR code generated is stored in a PNG format.

## Functionalities:
  1. Generates QR for any string given by the user.
  2. Saves the QR in a user-specified location.
  3. Allows you to change the size of QR code's image generated.

## Getting Started

### Prerequisites

Before you can use this script, you need to have Python installed on your computer. Additionally, you'll need to install the `qrcode` library. You can install it using pip:
`pip install qrcode[pil]`


### Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script by executing the following command:

`python qrcode_generator.py`


4. Follow the prompts to enter the text you want to encode in the QR code, the location where you want to save the QR code image, and the name for the QR code file (without the extension).

5. The script will generate the QR code with the specified information and save it as a PNG file in the specified location.

### QR Code Size

You can customize the size by entering a size between 1 and 40, where 1 is the smallest and 40 is the largest. You will be asked to enter a size input whenever you try to generate a QR.

## Dependencies

- `qrcode`: A Python library for generating QR codes.

## Acknowledgments

- The `qrcode` library used in this script is maintained by [lincolnloop](https://github.com/lincolnloop/python-qrcode).
