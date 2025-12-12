# 🚀 Diagno AI - Complete Setup & Run Guide

## 📋 Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge)
- Internet connection (for first-time setup)

---

## 🔧 Installation Steps

### Step 1: Install Python Dependencies

Open PowerShell/Command Prompt and navigate to the project directory:

```powershell
cd "d:\AI Projects\Diagno-AI"
```

Install required packages:

```powershell
pip install -r backend/requirements.txt
```

**Note:** If you encounter any issues, try:
```powershell
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

---

## 🤖 Step 2: Train the Machine Learning Model

This is a **MANDATORY** step before running the application!

```powershell
cd backend
python train_model.py
```

**What happens during training:**
- Creates a comprehensive disease-symptom dataset
- Trains SVM model with 95%+ accuracy
- Generates confusion matrix visualization
- Saves model files and metadata

**Expected Output:**
```
==============================================================
DIAGNO AI - MODEL TRAINING SYSTEM
==============================================================

[1/7] Creating Sample Dataset...
Total Symptoms: 50+
Total Diseases: 20

[2/7] Preparing Features and Target...
[3/7] Splitting Data (80-20)...
[4/7] Training SVM Model...
[5/7] Making Predictions...

==============================================================
MODEL ACCURACY: 95.XX%
==============================================================

✓ Model saved successfully!
✓ Training completed!
```

**Generated Files:**
- `models/disease_model.pkl` - Trained SVM model
- `models/symptom_list.json` - All symptoms
- `models/disease_info.json` - Disease information
- `models/model_metrics.json` - Performance metrics
- `models/confusion_matrix.png` - Visualization
- `data/disease_symptom_dataset.csv` - Training data

---

## 🌐 Step 3: Start the Backend Server

Start the Flask API server:

```powershell
python app.py
```

**Expected Output:**
```
==============================================================
DIAGNO AI - Backend Server
==============================================================
Model Accuracy: 95.XX%
Total Diseases: 20
Total Symptoms: 50+
==============================================================

🚀 Server starting on http://localhost:5000

Available Endpoints:
  - POST /signup
  - POST /login
  - POST /predict
  - GET  /get-symptoms
  ...

 * Running on http://127.0.0.1:5000
```

**⚠️ Keep this terminal window open!** The server must run continuously.

---

## 🖥️ Step 4: Open the Frontend

### Option 1: Direct File Opening (Simple)
1. Open File Explorer
2. Navigate to: `d:\AI Projects\Diagno-AI\frontend`
3. Double-click `index.html`

### Option 2: Using VS Code Live Server (Recommended)
1. Open VS Code
2. Install "Live Server" extension (if not installed)
3. Right-click on `index.html`
4. Select "Open with Live Server"

### Option 3: Using Python HTTP Server
Open a NEW terminal window:
```powershell
cd "d:\AI Projects\Diagno-AI\frontend"
python -m http.server 8000
```
Then open: http://localhost:8000

---

## 🎯 Step 5: Test the Complete System

### Test Sequence:

#### 1️⃣ **Test Authentication**
- Go to Login/Signup page
- Create a new account:
  - Username: `testuser`
  - Password: `test123`
  - Email: `test@example.com`
  - Full Name: `Test User`
- Login with credentials

#### 2️⃣ **Test Dashboard**
- After login, you should see the Dashboard
- Check system statistics are loading
- Verify user name appears in header

#### 3️⃣ **Test Diagnosis (Most Important!)**
- Click "Start Diagnosis" or navigate to Diagnosis page
- Select multiple symptoms, for example:
  - ✓ Fever
  - ✓ Cough
  - ✓ Fatigue
  - ✓ Body Ache
- Click "Analyze Symptoms & Predict Disease"
- Wait for AI prediction (should be instant)
- Verify you see:
  - Primary disease prediction with confidence
  - Top 3 possible diseases
  - Medical recommendations
  - Treatment suggestions
  - Diet recommendations

#### 4️⃣ **Test Insights Page**
- Navigate to Insights page
- Verify all charts are loading:
  - Model Performance Chart
  - Severity Distribution
  - Disease Distribution
  - Symptom Frequency
- Check that statistics display correctly

#### 5️⃣ **Test Report Saving**
- Go back to Dashboard
- Check "View Reports" section
- Your previous diagnosis should be saved

---

## 🧪 Quick Test Commands

### Test API Endpoints (Optional)

Open a new PowerShell terminal:

```powershell
# Test server is running
curl http://localhost:5000/

# Test get symptoms
curl http://localhost:5000/get-symptoms

# Test get accuracy
curl http://localhost:5000/get-accuracy

# Test get diseases
curl http://localhost:5000/get-diseases
```

---

## 🐛 Troubleshooting

### Problem: "Module not found" error
**Solution:**
```powershell
pip install flask flask-cors pandas numpy scikit-learn matplotlib seaborn joblib bcrypt PyJWT
```

### Problem: Backend server won't start
**Solution:**
- Check if Python is installed: `python --version`
- Check if port 5000 is available
- Try different port: Edit `app.py`, change `port=5000` to `port=5001`

### Problem: Model file not found
**Solution:**
- Make sure you ran `train_model.py` first
- Check if `models/disease_model.pkl` exists
- Re-run training script

### Problem: CORS errors in browser
**Solution:**
- Make sure Flask server is running
- Check browser console for specific error
- Verify `flask-cors` is installed

### Problem: Charts not displaying
**Solution:**
- Check internet connection (Chart.js loads from CDN)
- Open browser console (F12) for errors
- Verify API endpoint `/get-chart-data` is working

### Problem: Login not working
**Solution:**
- Check browser console for errors
- Verify backend server is running
- Check if `bcrypt` is installed: `pip install bcrypt`

---

## 📊 Features to Test

### ✅ Authentication System
- [x] User Registration
- [x] User Login
- [x] JWT Token Authentication
- [x] Password Encryption (bcrypt)
- [x] Logout

### ✅ AI Diagnosis
- [x] Symptom Selection (50+ symptoms)
- [x] Search Symptoms
- [x] Voice Input (browser support)
- [x] Disease Prediction with SVM
- [x] Confidence Scores
- [x] Top 3 Predictions

### ✅ Medical Recommendations
- [x] Disease Information
- [x] Treatment Suggestions
- [x] Prevention Tips
- [x] Medicine List
- [x] Diet Recommendations
- [x] Severity Indicators

### ✅ Visualizations
- [x] Model Performance Charts
- [x] Disease Distribution
- [x] Symptom Frequency
- [x] Severity Distribution
- [x] Confusion Matrix

### ✅ User Features
- [x] Save Reports
- [x] View History
- [x] Export Reports
- [x] Dashboard Statistics

---

## 📱 Supported Browsers

- ✅ Google Chrome (Recommended)
- ✅ Microsoft Edge
- ✅ Mozilla Firefox
- ✅ Safari
- ⚠️ Voice input may not work in all browsers

---

## 🎨 User Interface Pages

1. **Home Page** (`index.html`) - Landing page with project overview
2. **Login/Signup** (`login.html`) - User authentication
3. **Dashboard** (`dashboard.html`) - User overview and quick actions
4. **Diagnosis** (`diagnosis.html`) - Main symptom analysis page
5. **Insights** (`insights.html`) - Charts and statistics
6. **About** (`about.html`) - Project information and guide

---

## 💡 Sample Test Cases

### Test Case 1: Flu Detection
**Symptoms:** fever, cough, fatigue, body_ache, headache
**Expected:** Flu with high confidence

### Test Case 2: COVID-19 Detection
**Symptoms:** fever, dry_cough, fatigue, loss_of_taste, difficulty_breathing
**Expected:** COVID-19 with high confidence

### Test Case 3: Diabetes Detection
**Symptoms:** frequent_urination, excessive_thirst, hunger, fatigue, blurred_vision
**Expected:** Diabetes with high confidence

### Test Case 4: Common Cold
**Symptoms:** cough, runny_nose, sneezing, sore_throat
**Expected:** Common Cold with high confidence

---

## 📈 Performance Expectations

- **Model Accuracy:** 95%+ (as shown in training)
- **Prediction Time:** < 1 second
- **API Response Time:** < 100ms
- **Diseases Covered:** 20
- **Symptoms Tracked:** 50+

---

## 🔒 Security Features

- **Password Encryption:** bcrypt hashing
- **Token-based Auth:** JWT with 24-hour expiry
- **Secure Endpoints:** Protected routes require authentication
- **No Database:** All data in-memory (session-based)

---

## ⚠️ Important Notes

1. **No Database:** This system uses in-memory storage. All user data is temporary.
2. **Training Required:** Always run `train_model.py` before starting the server.
3. **Keep Server Running:** The Flask server must be active for the frontend to work.
4. **Medical Disclaimer:** This is for educational purposes only. Not for actual medical diagnosis.

---

## 🎯 Next Steps for Production

If you want to enhance this project:

1. **Add Database:** Integrate PostgreSQL/MongoDB for persistent storage
2. **More Diseases:** Expand dataset from Kaggle
3. **Better UI:** Add React/Vue.js framework
4. **Mobile App:** Create mobile version
5. **Model Improvement:** Use ensemble methods, neural networks
6. **Multi-language:** Add internationalization
7. **Admin Panel:** Create admin dashboard for model management

---

## 📧 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure model training completed successfully
4. Check browser console for errors (F12)
5. Review Flask server terminal for error messages

---

## ✅ Success Checklist

Before considering setup complete:

- [ ] All Python packages installed
- [ ] Model trained successfully (95%+ accuracy)
- [ ] Flask server running on port 5000
- [ ] Frontend loads in browser
- [ ] Can create user account
- [ ] Can login successfully
- [ ] Can select symptoms
- [ ] Receives disease prediction
- [ ] Charts display correctly
- [ ] Reports are saved

---

## 🎉 Congratulations!

If all tests pass, your Diagno AI system is fully functional! 

You now have a complete AI-powered health diagnosis system with:
- Machine Learning predictions
- User authentication
- Beautiful UI
- Data visualizations
- Medical recommendations

**Enjoy your AI Health Diagnosis System! 🏥🤖**
