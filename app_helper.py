import tensorflow as tf
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input
import numpy as np

def get_prediction(image_path):
    model = load_model('/home/vipinainvijayan4286/ChestXray-Classification-App/model.h5')
    img = load_img(image_path, target_size=(229, 229))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions[0])
    class_names=['COVID19', 'NORMAL', 'PNEUMONIA']
    class_name = class_names[class_index]
    probability = predictions[0][class_index]
    return class_name