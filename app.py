from flask import Flask, render_template, request
from PIL import Image
from collections import Counter
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'your_secret_key'

# Ensure the upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def find_most_common_colors(image_path, num_colors=5):
    """Find the most common colors in an image."""
    with Image.open(image_path) as img:
        img = img.convert('RGB')  # Ensure the image is in RGB mode
        pixels = list(img.getdata())
        color_counts = Counter(pixels)
        most_common = color_counts.most_common(num_colors)
        return most_common

def calculate_text_color(r, g, b):
    """Calculate whether text color should be black or white based on brightness."""
    brightness = (0.299 * r + 0.587 * g + 0.114 * b)
    return 'black' if brightness > 186 else 'white'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle image upload
        if 'image' not in request.files:
            return "No file part", 400
        file = request.files['image']
        if file.filename == '':
            return "No selected file", 400
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Find most common colors
            most_common_colors = find_most_common_colors(file_path)

            # Prepare data for rendering
            colors_data = [
                {
                    'color': f'rgb({r},{g},{b})',
                    'count': count,
                    'text_color': calculate_text_color(r, g, b)  # Adjust text color for visibility
                } for (r, g, b), count in most_common_colors
            ]

            return render_template('index.html', image=file.filename, colors=colors_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port= 9000)


