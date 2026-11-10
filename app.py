import os
import json
import numpy as np
import tensorflow as tf

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from PIL import Image
from io import BytesIO

app = FastAPI()

model = tf.keras.models.load_model(
    "best_food_spoilage_finetuned.keras"
)

with open("class_names.json", "r") as f:
    class_names = json.load(f)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image = Image.open(BytesIO(await file.read())).convert("RGB")
    image = image.resize((224, 224))

    image_array = np.array(image, dtype=np.float32) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array, verbose=0)

    index = int(np.argmax(predictions[0]))
    predicted_class = class_names[index]
    confidence = float(predictions[0][index] * 100)

    if predicted_class.lower().startswith("semi"):
        freshness = "Semi-Fresh"
        fruit = predicted_class.split("(")[0]
        fruit = fruit.replace("Semi_Fresh", "").replace("Semi Fresh", "").replace("Semi fresh", "").strip()

    elif predicted_class.lower().startswith("fresh"):
        freshness = "Fresh"
        fruit = predicted_class.replace("Fresh", "").split("(")[0].strip()

    else:
        freshness = "Rotten"
        fruit = predicted_class.replace("Rotten", "").split("(")[0].strip()

    return {
        "fruit": fruit,
        "freshness": freshness,
        "confidence": round(confidence, 2),
        "predicted_class": predicted_class
    }