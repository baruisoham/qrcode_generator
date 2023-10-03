import qrcode

def generate_qr_code(text, location, name, size):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=size,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data (text) to the QR code
    qr.add_data(text)
    qr.make(fit=True)

    # Create an Image object from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to the specified location with the given name
    file_path = f"{location}/{name}.png"
    qr_image.save(file_path)
    print(f"QR code saved as {file_path}")

if __name__ == "__main__":
    text_input = input("Enter the text you want to encode in the QR code: ")
    location_input = input("Enter the location where you want to save the QR code: ")
    name_input = input("Enter the name for the QR code file (without extension): ")
    #size_input = int(input("Enter the size of the QR code (1 to 40, with 1 being 21x21): "))
    size_input = int(4)

    generate_qr_code(text_input, location_input, name_input, size_input)
