**Chest X-ray Image Classification App**

This repository contains a Flask web application for classifying chest X-ray images into NORMAL, COVID19, and PNEUMONIA categories. The application uses a pre-trained EfficientNetB0 model for image classification.

**Files and Directory Structure**

1. Main folder Chest-Xray-Image-Classification-App

      app.py: The main Flask application file containing routes and functions for image upload and classification.
   
      app_helper.py: Helper functions for model loading and image preprocessing.
   
      chest_xray_classification_with_EfficientNetB0.ipynb: Jupyter notebook containing the code for training the image classification model.
   
      model.h5: Pre-trained model weights saved in HDF5 format.

   
2. Static/: Directory containing static files such as CSS.

            main.css: CSS file for styling the HTML templates.
   
3. uploads/: Where the input images will be stored


4. templates/: Directory containing HTML templates for the web application.


              layout.html: Base HTML template defining the layout structure.
   
              index.html: HTML template for the home page where users can upload images.
   
              upload.html: HTML template for displaying the uploaded image and its classification result.
   

**Folder Structure**

![image](https://github.com/vipinainvijayan/Chest-Xray-Image-Classification-App/assets/6160194/ffff7214-0443-4d53-bffd-9c9cc17755e1)


**Usage**


**Clone the repository:**


      git clone https://github.com/your_username/chest-Xray-Image-Classification-App.git


**Navigate to the project directory:**

      cd chest-Xray-Image-Classification-App


**Install dependencies:**

      pip install -r requirements.txt


**Run the Flask application:**

      python app.py


**Open a web browser and go to http://localhost:5000**

  Upload a chest X-ray image for classification.

**Model**

The classification model uses the EfficientNetB0 architecture pre-trained on ImageNet. Custom classification layers are added on top of the base model for the specific task of classifying chest X-ray images.

**Model Training**

The model is trained on a dataset containing chest X-ray images for three classes: NORMAL, COVID19, and PNEUMONIA. Data augmentation techniques are applied during training to improve generalization.

**Results**

The trained model achieves an accuracy of 93% on the testing data. Confusion matrix and other evaluation metrics are analyzed to assess the model's performance.



