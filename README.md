# 🎨 Image Color Analyzer

A simple web application built with **Flask** that allows users to upload an image and view the **top 5 most common colors** in that image. Each color is displayed with the number of pixels it appears in and the text color adjusts based on brightness for visibility.

---

## 📸 Features

- 📂 Upload any image (JPEG, PNG, etc.)
- 🎨 Detects the **top 5 most frequent colors**
- 🧠 Smart brightness detection for readable text
- 💻 Clean and simple web interface

---

## 🛠️ Technologies Used

- **Python**
- **Flask** – for web backend
- **Pillow (PIL)** – for image processing
- **HTML & CSS** – for frontend design

---

## 📁 Project Structure

Image-Color-Analyzer/
├── app.py # Main Flask app
├── static/
│ └── uploads/ # Folder for uploaded images
├── templates/
│ └── index.html # HTML template
└── README.md # Project description

yaml
Copy
Edit

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python installed.

Install required libraries:

```bash
pip install flask pillow
▶️ Running the App
Clone or download the repository

Navigate into the project directory

Run the Flask app:

bash
Copy
Edit
python app.py
Visit in your browser: http://127.0.0.1:9000/

🧠 How It Works
User uploads an image via a form

Image is saved to static/uploads/

The app uses Pillow to extract all pixel colors

Top 5 most common colors are calculated using collections.Counter

Each color is displayed with:

RGB value

Pixel count

Appropriate text color (black/white) based on brightness

💡 Future Enhancements
Add support for HEX color codes

Let users choose the number of colors to extract

Provide option to download the color palette

Improve mobile responsiveness

📄 License
This project is licensed under the MIT License.

📷 Sample Screenshot
(Insert a screenshot of your working app here if needed)

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

⭐ Show Your Support
If you like this project, give it a ⭐ on GitHub and share it with others!

yaml
Copy
Edit

---

Let me know if you'd like this written directly into a `README.md` file (I can generate it for downlo
