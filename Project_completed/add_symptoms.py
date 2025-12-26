import pandas as pd
import numpy as np

# Load current dataset
df = pd.read_csv('data/disease_symptom_dataset.csv')

# Define new symptoms to add (42 new symptoms)
new_symptoms = [
    'confusion', 'irritability', 'dehydration', 'rapid_heartbeat', 'back_pain',
    'constipation', 'bloating', 'skin_rash', 'insomnia', 'rapid_breathing',
    'nasal_congestion', 'throat_irritation', 'chest_congestion', 'shallow_breathing',
    'loss_of_smell', 'metallic_taste', 'heartburn', 'bloody_stool', 'dark_urine',
    'red_eyes', 'watery_eyes', 'skin_bruising', 'yellowish_skin', 'cold_sweats',
    'dry_skin', 'tremors', 'seizures', 'numbness', 'tingling',
    'ear_pain', 'neck_pain', 'knee_pain', 'lower_back_pain',
    'swollen_lymph_nodes', 'loss_of_consciousness', 'muscle_cramps', 'cold_hands_feet',
    'loss_of_voice', 'body_chills', 'blurred_speech', 'slow_healing_wounds',
    'increased_urination_at_night'
]

print(f"Adding {len(new_symptoms)} new symptoms...")

# Disease-symptom mappings for new symptoms
# Format: {disease_name: {symptom: probability}}
disease_symptom_map = {
    'Flu': {'back_pain': 0.4, 'body_chills': 0.6, 'nasal_congestion': 0.5, 'ear_pain': 0.2, 'neck_pain': 0.3, 'swollen_lymph_nodes': 0.3},
    
    'Common Cold': {'nasal_congestion': 0.9, 'throat_irritation': 0.6, 'watery_eyes': 0.4, 'ear_pain': 0.2, 'loss_of_smell': 0.3, 'loss_of_voice': 0.2},
    
    'Pneumonia': {'chest_congestion': 0.8, 'shallow_breathing': 0.7, 'rapid_breathing': 0.6, 'back_pain': 0.3, 'confusion': 0.3, 'cold_sweats': 0.4},
    
    'Bronchitis': {'chest_congestion': 0.9, 'throat_irritation': 0.7, 'nasal_congestion': 0.4, 'loss_of_voice': 0.3, 'insomnia': 0.2},
    
    'Asthma': {'chest_congestion': 0.7, 'shallow_breathing': 0.8, 'rapid_breathing': 0.6, 'insomnia': 0.4, 'rapid_heartbeat': 0.4},
    
    'COVID-19': {'loss_of_smell': 0.7, 'loss_of_taste': 0.7, 'metallic_taste': 0.3, 'nasal_congestion': 0.5, 'chest_congestion': 0.5, 'confusion': 0.2, 'red_eyes': 0.2, 'shallow_breathing': 0.5, 'swollen_lymph_nodes': 0.3},
    
    'Malaria': {'confusion': 0.5, 'tremors': 0.4, 'seizures': 0.3, 'dark_urine': 0.4, 'yellowish_skin': 0.5, 'cold_sweats': 0.6, 'loss_of_consciousness': 0.3, 'muscle_cramps': 0.5},
    
    'Dengue': {'skin_bruising': 0.7, 'red_eyes': 0.5, 'confusion': 0.3, 'dark_urine': 0.4, 'dehydration': 0.6, 'rapid_heartbeat': 0.5, 'cold_sweats': 0.5, 'skin_rash': 0.8, 'loss_of_consciousness': 0.2},
    
    'Typhoid': {'confusion': 0.4, 'constipation': 0.6, 'bloating': 0.5, 'dark_urine': 0.3, 'yellowish_skin': 0.3, 'bloody_stool': 0.3, 'dehydration': 0.5, 'insomnia': 0.3},
    
    'Tuberculosis': {'cold_sweats': 0.8, 'swollen_lymph_nodes': 0.6, 'loss_of_voice': 0.3, 'back_pain': 0.4, 'chest_congestion': 0.5, 'insomnia': 0.5},
    
    'Diabetes': {'slow_healing_wounds': 0.7, 'increased_urination_at_night': 0.6, 'numbness': 0.5, 'tingling': 0.5, 'blurred_speech': 0.2, 'dry_skin': 0.4, 'dehydration': 0.4, 'insomnia': 0.3, 'irritability': 0.4, 'cold_hands_feet': 0.3},
    
    'Hypertension': {'insomnia': 0.5, 'irritability': 0.6, 'constipation': 0.3, 'rapid_heartbeat': 0.5, 'blurred_speech': 0.3, 'confusion': 0.2, 'cold_hands_feet': 0.3},
    
    'Migraine': {'sensitivity_to_light': 0.8, 'irritability': 0.6, 'insomnia': 0.5, 'neck_pain': 0.7, 'nausea': 0.6},
    
    'Gastroenteritis': {'dehydration': 0.8, 'bloating': 0.6, 'heartburn': 0.4, 'bloody_stool': 0.3, 'rapid_heartbeat': 0.3, 'constipation': 0.2},
    
    'Food Poisoning': {'dehydration': 0.9, 'bloating': 0.7, 'heartburn': 0.5, 'bloody_stool': 0.4, 'rapid_heartbeat': 0.4, 'muscle_cramps': 0.3},
    
    'Urinary Tract Infection': {'back_pain': 0.5, 'lower_back_pain': 0.6, 'dehydration': 0.3, 'dark_urine': 0.5},
    
    'Kidney Stones': {'lower_back_pain': 0.9, 'back_pain': 0.8, 'dark_urine': 0.6, 'dehydration': 0.4, 'rapid_heartbeat': 0.4, 'cold_sweats': 0.5},
    
    'Arthritis': {'knee_pain': 0.7, 'neck_pain': 0.4, 'back_pain': 0.5, 'insomnia': 0.5, 'irritability': 0.4},
    
    'Allergy': {'watery_eyes': 0.9, 'red_eyes': 0.7, 'nasal_congestion': 0.8, 'throat_irritation': 0.6, 'skin_rash': 0.5},
    
    'Anemia': {'numbness': 0.5, 'tingling': 0.5, 'cold_hands_feet': 0.7, 'rapid_heartbeat': 0.6, 'insomnia': 0.4, 'irritability': 0.5, 'confusion': 0.3, 'loss_of_consciousness': 0.2}
}

# Initialize new symptom columns with 0
for symptom in new_symptoms:
    df[symptom] = 0

# Apply disease-specific symptoms
print("Applying disease-specific symptom patterns...")
for idx, row in df.iterrows():
    disease = row['disease']
    if disease in disease_symptom_map:
        for symptom, prob in disease_symptom_map[disease].items():
            # Randomly assign based on probability
            if np.random.random() < prob:
                df.at[idx, symptom] = 1

# Reorder columns - put disease at the end
cols = [col for col in df.columns if col != 'disease'] + ['disease']
df = df[cols]

# Save updated dataset
df.to_csv('data/disease_symptom_dataset.csv', index=False)

print(f"\n✅ Dataset updated successfully!")
print(f"Total symptoms: {df.shape[1] - 1} (was 56, now {df.shape[1] - 1})")
print(f"New symptoms added: {len(new_symptoms)}")
print(f"Total rows: {df.shape[0]}")

# Display new symptoms list
print("\nNew symptoms added:")
for i, symptom in enumerate(new_symptoms, 1):
    print(f"{i}. {symptom.replace('_', ' ').title()}")
