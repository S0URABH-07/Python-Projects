import os
import qrcode
from PIL import Image

class QRGenerator:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_qr(self, data, file_name, fill_color="black", back_color="white"):

        if not file_name.endswith(".png"):
            file_name = file_name + ".png"

        # 1. Initialize the Advanced QR Engine Configuration boundaries
        qr_matrix = qrcode.QRCode(
            version=1,  # Version 1 creates a baseline 21x21 module box grid
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High 30% error toleration
            box_size=10,  # Sets each matrix grid module square block to 10x10 pixels wide
            border=4      # Sets the outer silent zone padding white border thickness boundary
        )

        # 2. Feed raw text payload data into the matrix math compiler
        qr_matrix.add_data(data)
        qr_matrix.make(fit=True)  # Automatically expands grid version size if text data is long

        # 3. Compile the matrix modules directly onto a Pillow Image pixel bitmap canvas
        img_canvas = qr_matrix.make_image(
            fill_color=fill_color,
            back_color=back_color
        )

        # 4. Export the rendered pixel graphic map from RAM out to your hard drive file path
        target_path = os.path.join(self.output_dir, file_name)
        img_canvas.save(target_path)
        
        print(f"Canvas rendered! QR Code image successfully exported to: {target_path}")
        return target_path