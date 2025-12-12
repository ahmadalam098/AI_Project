import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("=" * 60)
print("DIAGNO AI - MODEL TRAINING SYSTEM")
print("=" * 60)

# Create necessary directories
os.makedirs('../models', exist_ok=True)
os.makedirs('../data', exist_ok=True)

# Sample Disease-Symptom Dataset
# In real scenario, download from Kaggle
print("\n[1/7] Creating Sample Dataset...")

# Creating a comprehensive symptom-disease dataset
diseases = {
    'Flu': ['fever', 'cough', 'fatigue', 'body_ache', 'headache'],
    'Common Cold': ['cough', 'runny_nose', 'sneezing', 'sore_throat', 'mild_fever'],
    'Pneumonia': ['high_fever', 'cough', 'chest_pain', 'difficulty_breathing', 'fatigue'],
    'Bronchitis': ['cough', 'mucus_production', 'fatigue', 'chest_discomfort', 'shortness_of_breath'],
    'Asthma': ['wheezing', 'shortness_of_breath', 'chest_tightness', 'coughing', 'difficulty_breathing'],
    'COVID-19': ['fever', 'dry_cough', 'fatigue', 'loss_of_taste', 'difficulty_breathing'],
    'Malaria': ['high_fever', 'chills', 'sweating', 'headache', 'nausea'],
    'Dengue': ['high_fever', 'severe_headache', 'joint_pain', 'muscle_pain', 'rash'],
    'Typhoid': ['prolonged_fever', 'weakness', 'abdominal_pain', 'headache', 'loss_of_appetite'],
    'Tuberculosis': ['persistent_cough', 'chest_pain', 'coughing_blood', 'weight_loss', 'night_sweats'],
    'Diabetes': ['frequent_urination', 'excessive_thirst', 'hunger', 'fatigue', 'blurred_vision'],
    'Hypertension': ['headache', 'dizziness', 'chest_pain', 'shortness_of_breath', 'nosebleeds'],
    'Migraine': ['severe_headache', 'nausea', 'vomiting', 'sensitivity_to_light', 'visual_disturbances'],
    'Gastroenteritis': ['diarrhea', 'vomiting', 'stomach_cramps', 'nausea', 'fever'],
    'Food Poisoning': ['nausea', 'vomiting', 'diarrhea', 'stomach_cramps', 'fever'],
    'Urinary Tract Infection': ['burning_urination', 'frequent_urination', 'cloudy_urine', 'pelvic_pain', 'fever'],
    'Kidney Stones': ['severe_pain', 'blood_in_urine', 'nausea', 'vomiting', 'frequent_urination'],
    'Arthritis': ['joint_pain', 'stiffness', 'swelling', 'decreased_range_of_motion', 'fatigue'],
    'Allergy': ['sneezing', 'runny_nose', 'itchy_eyes', 'rash', 'swelling'],
    'Anemia': ['fatigue', 'weakness', 'pale_skin', 'shortness_of_breath', 'dizziness'],
}

# Get all unique symptoms
all_symptoms = sorted(list(set([symptom for symptoms in diseases.values() for symptom in symptoms])))
print(f"Total Symptoms: {len(all_symptoms)}")
print(f"Total Diseases: {len(diseases)}")

# Create dataset
data = []
for disease, symptoms in diseases.items():
    # Create multiple samples with different symptom combinations
    for _ in range(50):  # 50 samples per disease
        row = {symptom: 0 for symptom in all_symptoms}
        # Randomly select 3-5 symptoms from the disease's symptom list
        num_symptoms = np.random.randint(3, min(6, len(symptoms) + 1))
        selected_symptoms = np.random.choice(symptoms, num_symptoms, replace=False)
        for symptom in selected_symptoms:
            row[symptom] = 1
        row['disease'] = disease
        data.append(row)

df = pd.DataFrame(data)

# Save dataset
dataset_path = '../data/disease_symptom_dataset.csv'
df.to_csv(dataset_path, index=False)
print(f"Dataset saved to: {dataset_path}")
print(f"Dataset shape: {df.shape}")

# Display sample
print("\nSample Data:")
print(df.head(3))

# Prepare features and target
print("\n[2/7] Preparing Features and Target...")
X = df.drop('disease', axis=1)
y = df['disease']

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Train-Test Split
print("\n[3/7] Splitting Data (80-20)...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Train SVM Model
print("\n[4/7] Training SVM Model...")
print("This may take a few moments...")
model = SVC(kernel='rbf', probability=True, random_state=42, gamma='scale')
model.fit(X_train, y_train)
print("✓ Model trained successfully!")

# Make predictions
print("\n[5/7] Making Predictions...")
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\n{'=' * 60}")
print(f"MODEL ACCURACY: {accuracy * 100:.2f}%")
print(f"{'=' * 60}")

# Detailed classification report
print("\n[6/7] Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Confusion Matrix
print("\n[7/7] Generating Confusion Matrix...")
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(14, 12))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=sorted(df['disease'].unique()),
            yticklabels=sorted(df['disease'].unique()))
plt.title('Disease Prediction - Confusion Matrix', fontsize=16, fontweight='bold')
plt.ylabel('Actual Disease', fontsize=12)
plt.xlabel('Predicted Disease', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('../models/confusion_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Confusion matrix saved to: ../models/confusion_matrix.png")

# Save Model
model_path = '../models/disease_model.pkl'
joblib.dump(model, model_path)
print(f"\n✓ Model saved to: {model_path}")

# Save symptom list
symptom_list_path = '../models/symptom_list.json'
with open(symptom_list_path, 'w') as f:
    json.dump(all_symptoms, f, indent=2)
print(f"✓ Symptom list saved to: {symptom_list_path}")

# Save disease information
disease_info = {
    'Flu': {
        'description': 'Influenza is a viral infection that attacks respiratory system.',
        'prevention': ['Get annual flu vaccine', 'Wash hands frequently', 'Avoid close contact with sick people'],
        'treatment': ['Rest and sleep', 'Drink plenty of fluids', 'Take antiviral medications if prescribed'],
        'medicines': ['Paracetamol', 'Ibuprofen', 'Oseltamivir (Tamiflu)'],
        'diet': ['Warm liquids', 'Chicken soup', 'Fruits rich in Vitamin C'],
        'severity': 'Moderate'
    },
    'Common Cold': {
        'description': 'A viral infection of upper respiratory tract, usually harmless.',
        'prevention': ['Wash hands regularly', 'Avoid touching face', 'Stay away from sick people'],
        'treatment': ['Rest', 'Stay hydrated', 'Use saline nasal drops'],
        'medicines': ['Antihistamines', 'Decongestants', 'Pain relievers'],
        'diet': ['Hot tea with honey', 'Citrus fruits', 'Ginger tea'],
        'severity': 'Mild'
    },
    'Pneumonia': {
        'description': 'Infection that inflames air sacs in lungs, can be serious.',
        'prevention': ['Get vaccinated', 'Practice good hygiene', 'Quit smoking'],
        'treatment': ['Antibiotics', 'Fever reducers', 'Oxygen therapy if severe'],
        'medicines': ['Amoxicillin', 'Azithromycin', 'Cephalosporins'],
        'diet': ['Protein-rich foods', 'Fluids', 'Fruits and vegetables'],
        'severity': 'Severe'
    },
    'Bronchitis': {
        'description': 'Inflammation of bronchial tubes causing cough and mucus.',
        'prevention': ['Avoid smoking', 'Avoid lung irritants', 'Get flu vaccine'],
        'treatment': ['Rest', 'Drink fluids', 'Use humidifier'],
        'medicines': ['Cough suppressants', 'Expectorants', 'Bronchodilators'],
        'diet': ['Warm liquids', 'Anti-inflammatory foods', 'Honey'],
        'severity': 'Moderate'
    },
    'Asthma': {
        'description': 'Chronic condition causing airway inflammation and breathing difficulty.',
        'prevention': ['Identify and avoid triggers', 'Take prescribed medications', 'Monitor breathing'],
        'treatment': ['Quick-relief inhalers', 'Long-term control medications', 'Avoid triggers'],
        'medicines': ['Albuterol', 'Inhaled corticosteroids', 'Montelukast'],
        'diet': ['Omega-3 rich foods', 'Vitamin D foods', 'Avoid food allergens'],
        'severity': 'Moderate to Severe'
    },
    'COVID-19': {
        'description': 'Respiratory illness caused by SARS-CoV-2 virus.',
        'prevention': ['Vaccination', 'Wear masks', 'Social distancing', 'Hand hygiene'],
        'treatment': ['Isolate', 'Rest', 'Monitor oxygen levels', 'Seek medical care if severe'],
        'medicines': ['Paracetamol', 'Antivirals (Paxlovid)', 'Monoclonal antibodies'],
        'diet': ['Protein-rich foods', 'Vitamin C', 'Zinc supplements', 'Hydration'],
        'severity': 'Moderate to Severe'
    },
    'Malaria': {
        'description': 'Mosquito-borne disease caused by Plasmodium parasites.',
        'prevention': ['Use mosquito nets', 'Insect repellent', 'Antimalarial medications'],
        'treatment': ['Antimalarial drugs', 'Supportive care', 'Hospitalization if severe'],
        'medicines': ['Chloroquine', 'Artemisinin-based combination therapy', 'Quinine'],
        'diet': ['High-calorie foods', 'Fluids', 'Easily digestible foods'],
        'severity': 'Severe'
    },
    'Dengue': {
        'description': 'Mosquito-borne viral infection causing severe flu-like illness.',
        'prevention': ['Eliminate mosquito breeding sites', 'Use repellents', 'Wear protective clothing'],
        'treatment': ['Rest', 'Hydration', 'Pain relievers (avoid aspirin)', 'Monitor platelet count'],
        'medicines': ['Paracetamol', 'Oral rehydration solutions', 'No aspirin or NSAIDs'],
        'diet': ['Papaya leaf juice', 'Coconut water', 'Orange juice', 'Pomegranate'],
        'severity': 'Severe'
    },
    'Typhoid': {
        'description': 'Bacterial infection causing prolonged fever, transmitted through contaminated food/water.',
        'prevention': ['Vaccination', 'Drink safe water', 'Practice good hygiene'],
        'treatment': ['Antibiotics', 'Fluids and electrolytes', 'Rest'],
        'medicines': ['Ciprofloxacin', 'Azithromycin', 'Ceftriaxone'],
        'diet': ['High-calorie foods', 'Cooked vegetables', 'Banana', 'Yogurt'],
        'severity': 'Severe'
    },
    'Tuberculosis': {
        'description': 'Bacterial infection primarily affecting lungs.',
        'prevention': ['BCG vaccine', 'Avoid close contact', 'Good ventilation'],
        'treatment': ['Long-term antibiotics (6-9 months)', 'DOT therapy', 'Regular monitoring'],
        'medicines': ['Rifampicin', 'Isoniazid', 'Pyrazinamide', 'Ethambutol'],
        'diet': ['Protein-rich foods', 'Vitamin A, C, E foods', 'Whole grains'],
        'severity': 'Severe'
    },
    'Diabetes': {
        'description': 'Metabolic disorder characterized by high blood sugar levels.',
        'prevention': ['Maintain healthy weight', 'Exercise regularly', 'Healthy diet'],
        'treatment': ['Blood sugar monitoring', 'Insulin therapy', 'Oral medications', 'Lifestyle changes'],
        'medicines': ['Metformin', 'Insulin', 'Sulfonylureas', 'DPP-4 inhibitors'],
        'diet': ['Low glycemic index foods', 'Whole grains', 'Leafy vegetables', 'Avoid sugary foods'],
        'severity': 'Chronic - Manageable'
    },
    'Hypertension': {
        'description': 'High blood pressure condition affecting cardiovascular system.',
        'prevention': ['Reduce salt intake', 'Exercise regularly', 'Maintain healthy weight', 'Limit alcohol'],
        'treatment': ['Lifestyle modifications', 'Blood pressure medications', 'Regular monitoring'],
        'medicines': ['ACE inhibitors', 'Beta blockers', 'Calcium channel blockers', 'Diuretics'],
        'diet': ['DASH diet', 'Low sodium foods', 'Potassium-rich foods', 'Reduce caffeine'],
        'severity': 'Chronic - Manageable'
    },
    'Migraine': {
        'description': 'Neurological condition causing severe recurring headaches.',
        'prevention': ['Identify triggers', 'Regular sleep schedule', 'Stress management', 'Stay hydrated'],
        'treatment': ['Pain relievers', 'Preventive medications', 'Rest in dark room'],
        'medicines': ['Triptans', 'NSAIDs', 'Anti-nausea medications', 'Preventive medications'],
        'diet': ['Regular meals', 'Avoid trigger foods', 'Magnesium-rich foods', 'Stay hydrated'],
        'severity': 'Moderate'
    },
    'Gastroenteritis': {
        'description': 'Inflammation of digestive tract causing diarrhea and vomiting.',
        'prevention': ['Hand hygiene', 'Food safety', 'Avoid contaminated water'],
        'treatment': ['Rehydration', 'Rest', 'Bland diet', 'Avoid dairy temporarily'],
        'medicines': ['Oral rehydration salts', 'Anti-diarrheal medications', 'Probiotics'],
        'diet': ['BRAT diet (Banana, Rice, Applesauce, Toast)', 'Clear liquids', 'Electrolyte drinks'],
        'severity': 'Mild to Moderate'
    },
    'Food Poisoning': {
        'description': 'Illness from eating contaminated food.',
        'prevention': ['Proper food handling', 'Cook food thoroughly', 'Refrigerate promptly'],
        'treatment': ['Rest', 'Rehydration', 'Avoid solid foods initially'],
        'medicines': ['Anti-diarrheal medications', 'Oral rehydration solutions', 'Antibiotics if bacterial'],
        'diet': ['Clear liquids initially', 'BRAT diet', 'Gradually return to normal diet'],
        'severity': 'Mild to Moderate'
    },
    'Urinary Tract Infection': {
        'description': 'Bacterial infection affecting urinary system.',
        'prevention': ['Stay hydrated', 'Urinate frequently', 'Proper hygiene', 'Avoid irritants'],
        'treatment': ['Antibiotics', 'Pain relievers', 'Increased fluid intake'],
        'medicines': ['Trimethoprim-sulfamethoxazole', 'Nitrofurantoin', 'Ciprofloxacin'],
        'diet': ['Cranberry juice', 'Water', 'Vitamin C foods', 'Avoid caffeine'],
        'severity': 'Mild to Moderate'
    },
    'Kidney Stones': {
        'description': 'Hard deposits of minerals in kidneys causing severe pain.',
        'prevention': ['Stay hydrated', 'Limit sodium', 'Limit animal protein', 'Avoid high oxalate foods'],
        'treatment': ['Pain management', 'Drink lots of water', 'Medical procedures if large'],
        'medicines': ['Pain relievers', 'Alpha blockers', 'Medications to prevent stones'],
        'diet': ['Increase water intake', 'Lemon water', 'Reduce salt', 'Limit oxalate-rich foods'],
        'severity': 'Moderate to Severe'
    },
    'Arthritis': {
        'description': 'Joint inflammation causing pain and stiffness.',
        'prevention': ['Maintain healthy weight', 'Exercise regularly', 'Protect joints', 'Healthy diet'],
        'treatment': ['Pain management', 'Physical therapy', 'Exercise', 'Heat/cold therapy'],
        'medicines': ['NSAIDs', 'Corticosteroids', 'Disease-modifying antirheumatic drugs'],
        'diet': ['Anti-inflammatory foods', 'Omega-3 fatty acids', 'Fruits and vegetables', 'Avoid processed foods'],
        'severity': 'Chronic - Manageable'
    },
    'Allergy': {
        'description': 'Immune system reaction to foreign substance.',
        'prevention': ['Identify and avoid allergens', 'Keep environment clean', 'Use air purifiers'],
        'treatment': ['Avoid triggers', 'Antihistamines', 'Immunotherapy'],
        'medicines': ['Antihistamines', 'Decongestants', 'Corticosteroid nasal sprays', 'Epinephrine (severe cases)'],
        'diet': ['Anti-inflammatory foods', 'Quercetin-rich foods', 'Avoid trigger foods'],
        'severity': 'Mild to Severe'
    },
    'Anemia': {
        'description': 'Condition with lack of healthy red blood cells.',
        'prevention': ['Iron-rich diet', 'Vitamin supplements', 'Regular checkups'],
        'treatment': ['Iron supplements', 'Vitamin B12 supplements', 'Treat underlying cause'],
        'medicines': ['Iron supplements', 'Vitamin B12', 'Folic acid', 'Erythropoietin'],
        'diet': ['Iron-rich foods (spinach, red meat)', 'Vitamin C foods', 'Folate-rich foods'],
        'severity': 'Mild to Moderate'
    }
}

disease_info_path = '../models/disease_info.json'
with open(disease_info_path, 'w') as f:
    json.dump(disease_info, f, indent=2)
print(f"✓ Disease information saved to: {disease_info_path}")

# Save model metrics
metrics = {
    'accuracy': float(accuracy),
    'total_diseases': len(diseases),
    'total_symptoms': len(all_symptoms),
    'training_samples': len(X_train),
    'testing_samples': len(X_test),
    'model_type': 'Support Vector Machine (SVM)',
    'kernel': 'RBF (Radial Basis Function)'
}

metrics_path = '../models/model_metrics.json'
with open(metrics_path, 'w') as f:
    json.dump(metrics, f, indent=2)
print(f"✓ Model metrics saved to: {metrics_path}")

print("\n" + "=" * 60)
print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
print("=" * 60)
print(f"\nGenerated Files:")
print(f"  1. Model: {model_path}")
print(f"  2. Symptoms: {symptom_list_path}")
print(f"  3. Disease Info: {disease_info_path}")
print(f"  4. Metrics: {metrics_path}")
print(f"  5. Confusion Matrix: ../models/confusion_matrix.png")
print(f"  6. Dataset: {dataset_path}")
print("\n✓ Ready to run Flask API server!")
