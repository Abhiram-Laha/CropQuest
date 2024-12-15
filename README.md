# **CropQuest: Intelligent Crop and Fertilizer Recommendation System**

## **Project Overview**
CropQuest is a data-driven web application designed to enhance agricultural productivity by providing tailored recommendations for crops and fertilizers. It leverages machine learning models to analyze various environmental and soil parameters, enabling farmers to make informed decisions for better yield and soil health management.

---

## **Features**
1. **Crop Recommendation**  
   Provides recommendations for the most suitable crop based on soil properties, weather conditions, and other parameters.
   
2. **Fertilizer Recommendation**  
   Offers precise fertilizer suggestions tailored to the selected crop and soil conditions to maximize productivity.
   
3. **Interactive User Interface**  
   Built with Flask and HTML templates to create a seamless and user-friendly experience.

4. **Data Validation and Error Handling**  
   Ensures robust handling of invalid or missing inputs, providing helpful feedback to users.

---

## **Project Structure**

```plaintext
CropQuest/
|-- static/
|   |-- css/             # CSS files for styling
|   |-- images/          # Images used in the app
|-- templates/
|   |-- index.html       # Home page
|   |-- crop_rec.html    # Crop recommendation page
|   |-- fertilizer_Rec.html  # Fertilizer recommendation page
|-- Models/
|   |-- RandomForest.pkl # Machine learning model for crop prediction
|   |-- classifier.pkl   # Fertilizer recommendation model
|   |-- fertilizer.pkl   # Classifier object for fertilizers
|-- app.py               # Main application file
|-- README.md            # Documentation file
```

---

## **Dependencies**

### **Python Libraries**
Ensure you have the following Python libraries installed:

- `Flask`
- `numpy`
- `pandas`
- `scikit-learn`
- `pickle`

### **Frontend Technologies**

- HTML5
- Bootstrap
- CSS

---

## **Installation**

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cropquest.git
cd cropquest
```

### 2. Set Up the Python Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Add Pre-trained Models
Place the pre-trained `.pkl` files (`RandomForest.pkl`, `classifier.pkl`, `fertilizer.pkl`) in the `Models/` directory.

### 4. Run the Application
```bash
python app.py
```
Access the application at `http://127.0.0.1:8000/`.

---

## **Usage**

### **1. Home Page**
The homepage provides an overview of the application and links to its core functionalities.

### **2. Crop Recommendation**
- Navigate to the **Crop Recommendation** page.
- Input the required parameters: 
  - Nitrogen, Phosphorus, Potassium
  - Temperature, Humidity, pH
  - Rainfall
- Click **Predict** to receive the most suitable crop suggestion.

### **3. Fertilizer Recommendation**
- Navigate to the **Fertilizer Recommendation** page.
- Input the required parameters:
  - Temperature, Humidity, Moisture
  - Soil Type, Crop Type
  - Nitrogen, Phosphorus, Potassium
- Click **Predict** to receive the recommended fertilizer for the selected crop and soil conditions.

---

## **Machine Learning Models**

### 1. **Crop Recommendation Model**
- **Algorithm**: Random Forest Classifier
- **Input Features**:
  - Soil Nutrients (N, P, K)
  - Environmental Conditions (Temperature, Humidity, Rainfall)
  - Soil pH

### 2. **Fertilizer Recommendation Model**
- **Algorithm**: Classifier
- **Input Features**:
  - Soil and Environmental Parameters (Temperature, Humidity, Moisture)
  - Soil and Crop Types
  - Nutrient Levels (N, P, K)

---

## **Error Handling**
- Ensures all input fields are validated.
- Provides user-friendly messages for invalid or missing inputs.
- Handles model prediction errors gracefully.

---

## **Screenshots**

### **Home Page**
![image](https://github.com/user-attachments/assets/d2e58c40-714e-4373-b7d6-5cdf97112a90)
![image](https://github.com/user-attachments/assets/67bdcad6-4e1d-4657-8819-86a7ddc77c4a)
![image](https://github.com/user-attachments/assets/6fa819b2-7627-41ea-b145-59a702868752)

_Description: Screenshot of the homepage with an overview of features._

### **Crop Recommendation Page**
![image](https://github.com/user-attachments/assets/c4cb3725-bc49-4cfc-a797-e0ad223c9ded)

_Description: Screenshot of the input form and prediction results for crop recommendation._

### **Fertilizer Recommendation Page**
![image](https://github.com/user-attachments/assets/09f23478-67ec-4bb5-92c9-84b4cfa058fc)

_Description: Screenshot of the input form and prediction results for fertilizer recommendation._

---

## **Future Enhancements**
1. Add weather forecast integration to enhance prediction accuracy.
2. Enable real-time data collection from IoT devices.
3. Expand crop and fertilizer datasets to cover more regions and types.

---

## **Contributors**
- **Abhiram Laha** - [GitHub](https://github.com/Abhiram-Laha)

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- Thanks to the open-source community for resources and libraries.
- Inspired by the goal to optimize farming and support sustainable agriculture.
