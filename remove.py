from rembg import remove
from PIL import Image

input_patch = 'bojack.jpg'
output_patch = 'bojack.png'

input = Image.open(input_patch)

output = remove(input)

output.save(output_patch)

print(f"Imagen sin fondo guardada en {output_patch}")