🎨 Image Color Analyzer
A simple web application built using Flask and Python that allows users to upload an image and analyze the top 5 most common colors in the image. It also displays each color with a dynamically selected text color (black or white) for better visibility.

📸 Features
Upload any image (JPEG, PNG, etc.)

Detects the top 5 most common colors in the image.

Displays each color as a swatch with the RGB value and pixel count.

Automatically adjusts text color (black or white) based on background brightness.

User-friendly web interface.

🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML, CSS (inline)

Image Processing: PIL (Pillow)

Utilities: collections.Counter for color frequency

🚀 How to Run the Project
Prerequisites
Make sure you have Python installed. Then install the required packages:

bash
Copy
Edit
pip install flask pillow
Running the App
Clone or download this repository.

Navigate to the project directory.

Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:9000/

📁 Project Structure
php
Copy
Edit
project-directory/
│
├── app.py                  # Flask app
├── static/
│   └── uploads/            # Folder to store uploaded images
├── templates/
│   └── index.html          # HTML file for rendering the UI
└── README.md               # This file
🧠 How It Works
When a user uploads an image, it's saved in the static/uploads folder.

The image is then analyzed using Pillow (PIL.Image) to extract pixel data.

The Counter class is used to find the top 5 most frequent colors.

A simple brightness formula determines whether the text should be white or black for contrast.

📷 Screenshot
(You can add a screenshot of your web page here)

📄 License
This project is open-source and free to use under the MIT License.

💡 Future Improvements
Add color HEX values.

Allow users to select how many colors they want to detect.

Add support for color palette downloads.

Responsive design for mobile support.

Feel free to ⭐ the project if you found it helpful!

