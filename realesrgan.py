from PIL import Image

def enhance_image(input_path, output_path):
    img = Image.open(input_path)
    enhanced = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)
    enhanced.save(output_path)