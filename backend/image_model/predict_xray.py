import tensorflow as tf
import numpy as np
from PIL import Image

IMG_SIZE = 224

model = tf.keras.models.load_model("backend/image_model/xray_model.h5")

def predict_xray(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)[0][0]

    if prediction > 0.5:
        return {
            "prediction": "Pneumonia",
            "confidence": float(prediction)
        }
    else:
        return {
            "prediction": "Normal",
            "confidence": float(1 - prediction)
        }