# Food Spoilage Prediction System

### Live Demo
Try the application: https://food-spoilage-prediction.onrender.com

A deep learning-based image classification application that identifies the freshness condition of fruits and vegetables using computer vision.

The project uses **MobileNetV2 with Transfer Learning and Fine-Tuning** to classify images into Fresh, Semi-Fresh, and Rotten categories. A web application built using FastAPI allows users to upload images and view predictions.

## Project Overview

The system supports 8 types of fruits and vegetables, with 3 freshness conditions for each, resulting in 24 classification classes.

**Supported produce:**
- Banana
- Bittermelon
- Cucumber
- Eggplant
- Orange
- Papaya
- Pineapple
- Tomato

## Technologies Used

- **Language:** Python
- **Deep Learning:** TensorFlow, Keras
- **Architecture:** MobileNetV2
- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Data Processing:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Development:** Jupyter Notebook, VS Code

## Model Development

The model was developed using the following workflow:

1. Dataset loading and exploration.
2. Image preprocessing and resizing to 224 × 224.
3. Duplicate detection and removal of conflicting images.
4. Group-based training, validation, and test splitting.
5. Transfer learning using pretrained MobileNetV2.
6. Classification head development for 24 classes.
7. Fine-tuning selected pretrained layers.
8. Evaluation using accuracy, loss, F1-score, and confusion matrix.

### Model Configuration

- Architecture: MobileNetV2
- Input shape: 224 × 224 × 3
- Output classes: 24
- Optimizer: Adam
- Learning approach: Transfer Learning + Fine-Tuning
- Output activation: Softmax

## Dataset

The dataset contains 14,160 original images across 24 classes.

After duplicate and conflict removal, the final dataset contains **14,033 images**.

**Dataset distribution:**

- Training: 9,623 images (68.58%)
- Validation: 2,406 images (17.15%)
- Testing: 2,004 images (14.28%)

Original image resolution: 512 × 512 pixels.

A group-based splitting strategy was used to reduce data leakage from related or augmented image versions.

Dataset link: https://data.mendeley.com/datasets/42m5tb7yv9/1?

## Model Performance

The final fine-tuned model was evaluated on the held-out test set.

- **Validation Accuracy:** 92.93%
- **Test Accuracy:** 91.07%
- **Test Loss:** 0.2374
- **Macro F1-Score:** 0.9095
- **Weighted F1-Score:** 0.9099

## Application Workflow

1. User uploads a fruit or vegetable image.
2. FastAPI receives the image.
3. The image is resized and preprocessed.
4. The trained MobileNetV2 model generates predictions.
5. The predicted class is mapped to a fruit name and freshness category.
6. The result is displayed with a confidence score.

## Project Structure

Food-Spoilage-Prediction/
│
├── 01_data_exploration.ipynb
├── app.py
├── best_food_spoilage_finetuned.keras
├── class_names.json
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js

## Installation and Execution

**1. Clone the repository**

git clone https://github.com/shripad-gudsoorkar/Food-Spoilage-Prediction.git

**2. Navigate to the project directory**

cd Food-Spoilage-Prediction

**3. Create a virtual environment**

python -m venv venv

**4. Activate the environment (Windows)**

venv\Scripts\activate

**5. Install dependencies**

pip install -r requirements.txt

**6. Start the application**

uvicorn app:app --reload

**7. Open in your browser**

http://127.0.0.1:8000

Upload an image to obtain its predicted freshness category.

## Limitations

- Predictions depend on visible characteristics in the image.
- Fresh and Semi-Fresh categories may have similar visual features.
- Lighting, image quality, background, and produce variety can affect predictions.
- Softmax confidence scores are not calibrated probabilities.
- The system cannot detect invisible contamination or determine whether food is safe to consume.

## Future Improvements

- Improve classification of visually similar freshness categories.
- Deploy the application on a cloud platform.
- Add prediction history.
- Support real-time camera-based predictions.
- Expand the dataset with additional produce types.

## Author

**Shripad Gudsoorkar**

Artificial Intelligence and Data Science, DIT Pimpri

GitHub: [shripad-gudsoorkar](https://github.com/shripad-gudsoorkar)

