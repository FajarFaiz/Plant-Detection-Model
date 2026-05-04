<div align="center"> <video src="https://github.com/user-attachments/assets/cb869a69-b53e-4726-ac38-cc7528a80b3d" width="100%" autoplay loop muted></video> <p><i>Real-time Plant Disease Detection Demo</i></p> </div> 

# Plant Health AI:
Leaf Disease Detection System: A full-stack Deep Learning application that uses a Convolutional Neural Network (CNN) to identify plant diseases from leaf images. The system provides real-time classification through a Flask web interface. 

## Live Features 
Automated Classification: Instant detection of 4 distinct plant health states.

High Precision: Uses image normalization (1/255) and standardized (225x225) input for consistent accuracy.

Web Interface: User-friendly Flask dashboard for image uploads and result display. 

Confidence Scoring: Provides a probability percentage for every prediction.

## Tech Stack
Backend: Python, Flask
Deep Learning: TensorFlow, Keras Computer Vision: NumPy, Pillow (PIL) Frontend: HTML5, CSS3 

## Supported Conditions
The model is trained to recognize the following classes: 
Healthy Leaf – Optimal plant health. Powdery Mildew – Fungal infection appearing as white flour-like spots. Early Blight – Identifying target-like spots before they spread. 
Rust – Detection of reddish-brown fungal spores.

## Project Structure
plant-detection-ai 
┣ 📂 models ┃
┗ 📜 model.h5 <-- Trained CNN weights ┣ 📂 static ┃ ┗ 📂 uploads <-- User-uploaded leaf images
┣ 📂 templates ┃ ┗ 📜 index.html <-- Flask Web Interface
┣ 📜 app.py <-- Main Server & Logic 
┣ 📜 history.pkl <-- Training metrics & history
┣ 📜 requirements.txt <-- Library dependencies ┗ 📜 README.md <-- Project Documentation 

## Installation & Setup
1: Clone the repository:
git clone https://github.com cd your-repo-name
2: Set up Virtual Environment (Windows): 
python -m venv venv .\venv\Scripts\Activate.ps1
3:Install Dependencies:
pip install flask tensorflow numpy pillow 
4:Run the Application:
python app.py 

## Technical Highlights

Data Pipeline: Images are standardized to 225x225 pixels and normalized by a factor of 1/255. This ensures the model receives a consistent distribution of data, improving inference speed.

Error Handling: The load_model function is wrapped in a try-except block to ensure the Flask server gracefully handles file-path or compatibility errors without crashing.

Preprocessing Logic: Used np.expand_dims to transform single images into the 4D batches required by the Keras backend.
