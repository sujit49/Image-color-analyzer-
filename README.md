# 🎨 Most Common Colors in an Image - Flask App

This is a simple and elegant **Flask-based web application** that allows users to upload an image and view the **top 5 most common colors** found in it. Each color is displayed as a colored box with a dynamic text color (black or white) for maximum readability.

---

## 🧩 Features

- Upload any image (`.jpg`, `.png`, etc.)
- Extract the top 5 most frequently occurring colors
- Visual representation with RGB codes
- Dynamic text color based on brightness for better contrast
- Lightweight and clean UI using `HTML` & `Flask`
- Supports multiple image types using the `Pillow` library

---

## 🚀 Technologies Used

- Python 3
- Flask
- PIL (Pillow)
- HTML/CSS
- Collections module (`Counter`)

---

## 🖼️ How It Works

1. User uploads an image via the web interface.
2. The backend:
   - Converts the image to RGB
   - Counts the frequency of each color using `Counter`
   - Extracts the 5 most common colors
3. The frontend displays each color as a colored block along with its count and RGB value.

---

## 📁 File Structure

```
project/
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # HTML frontend for upload and display
├── static/
│   └── uploads/          # Stores uploaded images
└── README.md             # Project documentation
```

---

## 🛠️ Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory in your terminal.
3. Install required packages:

```bash
pip install flask pillow
```

---

## ▶️ How to Run

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:9000/
```

---

## 📸 Example

> Upload an image and see output like:

- 🎨 `rgb(255, 255, 255)` – White
- 🎨 `rgb(0, 0, 0)` – Black
- 🎨 `rgb(34, 45, 200)` – Blue shade  
...each with frequency and contrast-aware text.

---

## 💡 Future Improvements

- Show a pie chart or bar chart of color distribution
- Allow user to select how many top colors to view
- Drag-and-drop interface
- HEX code display

---

## 📜 License

This project is open for learning, experimentation, and improvement. Replace media/UI as needed if redistributing.

---

Enjoy visualizing colors from your images! 🎨🖼️✨

