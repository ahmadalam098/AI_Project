# 🚀 Diagno AI - Quick Reference Card

## 📦 Quick Start (3 Steps)

```powershell
# 1. Train Model
cd "d:\AI Projects\Diagno-AI\backend"
python train_model.py

# 2. Start Server
python app.py

# 3. Open Browser
# Navigate to: d:\AI Projects\Diagno-AI\frontend\index.html
```

---

## 🔧 Essential Commands

### Training
```powershell
python backend/train_model.py
```

### Start Server
```powershell
python backend/app.py
```

### Install Dependencies
```powershell
pip install -r backend/requirements.txt
```

### Quick Start (All-in-One)
```powershell
.\start.ps1
```

---

## 🌐 URLs & Ports

| Service | URL |
|---------|-----|
| Backend API | http://localhost:5000 |
| Frontend | Open `frontend/index.html` |
| API Docs | http://localhost:5000/ |

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| `backend/app.py` | Flask API server |
| `backend/train_model.py` | Model training |
| `frontend/index.html` | Home page |
| `models/disease_model.pkl` | Trained model |
| `SETUP_GUIDE.md` | Complete setup instructions |

---

## 🔑 API Endpoints

### Public Endpoints
```
GET  /                    - API info
GET  /get-symptoms        - All symptoms
GET  /get-diseases        - All diseases
GET  /get-accuracy        - Model accuracy
GET  /get-metrics         - Model metrics
GET  /get-chart-data      - Chart data
POST /signup              - Register user
POST /login               - Login user
POST /predict             - Disease prediction
```

### Protected Endpoints (Require JWT)
```
POST /save-report         - Save diagnosis
GET  /get-reports         - User reports
```

---

## 🧪 Quick Test

### Test Backend
```powershell
curl http://localhost:5000/get-accuracy
```

### Test Prediction
```powershell
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"symptoms\": [\"fever\", \"cough\"]}"
```

---

## 📊 System Stats

- **Diseases:** 20
- **Symptoms:** 50+
- **Accuracy:** 95%+
- **Model:** SVM (RBF Kernel)
- **Training Samples:** 1000
- **Response Time:** < 1 second

---

## 🎯 Features Checklist

✅ User Authentication (JWT + bcrypt)
✅ AI Disease Prediction (SVM)
✅ Medical Recommendations
✅ Interactive Charts (Chart.js)
✅ Report Management
✅ Voice Input (Browser API)
✅ Export Reports
✅ Mobile Responsive
✅ No Database Required

---

## 🐛 Troubleshooting Quick Fixes

### Problem: Module not found
```powershell
pip install flask flask-cors pandas numpy scikit-learn matplotlib seaborn joblib bcrypt PyJWT
```

### Problem: Model not found
```powershell
cd backend
python train_model.py
```

### Problem: Port 5000 busy
Edit `app.py`, change: `app.run(port=5001)`

### Problem: CORS error
Ensure `flask-cors` is installed and server is running

---

## 📱 Pages Overview

| Page | File | Purpose |
|------|------|---------|
| Home | `index.html` | Landing page |
| Login | `login.html` | Authentication |
| Dashboard | `dashboard.html` | User overview |
| Diagnosis | `diagnosis.html` | Symptom analysis |
| Insights | `insights.html` | Charts & stats |
| About | `about.html` | Project info |

---

## 🎓 Tech Stack

**Backend:**
- Python 3.x
- Flask (Web Framework)
- Scikit-learn (ML)
- Pandas & NumPy (Data)
- Matplotlib & Seaborn (Viz)

**Frontend:**
- HTML5, CSS3, JavaScript
- Chart.js (Visualizations)
- No frameworks (Pure vanilla JS)

**Security:**
- JWT (Authentication)
- bcrypt (Password Hashing)
- CORS (Cross-Origin)

---

## ⚡ Performance Tips

1. **Train model once** - Reuse the trained model
2. **Keep server running** - Restart only if needed
3. **Use caching** - Browser caches static files
4. **Optimize charts** - Limit data points if slow

---

## 🔒 Security Notes

- Passwords hashed with bcrypt
- JWT tokens expire in 24 hours
- No database = No SQL injection risk
- In-memory storage = Session-only data

---

## 📧 Support Checklist

Before asking for help:

- [ ] Python installed? (`python --version`)
- [ ] Dependencies installed? (`pip list`)
- [ ] Model trained? (Check `models/disease_model.pkl`)
- [ ] Server running? (Check terminal)
- [ ] Browser console checked? (F12)
- [ ] Correct port? (5000)

---

## ⚠️ Important Reminders

1. **Train First:** Always run `train_model.py` before starting server
2. **Keep Server On:** Don't close terminal while using app
3. **No Database:** Data is temporary (in-memory)
4. **Educational Use:** Not for actual medical diagnosis
5. **Medical Disclaimer:** Always consult healthcare professionals

---

## 🎉 Success Indicators

✅ Server shows "Running on http://127.0.0.1:5000"
✅ Model accuracy shows 95%+
✅ Frontend loads without errors
✅ Can create account and login
✅ Disease prediction returns results
✅ Charts display correctly

---

## 📚 Documentation Files

- `README.md` - Project overview
- `SETUP_GUIDE.md` - Complete setup instructions
- `TESTING_GUIDE.md` - Testing procedures
- `QUICK_REFERENCE.md` - This file

---

## 🚀 One-Line Setup

```powershell
cd "d:\AI Projects\Diagno-AI"; .\start.ps1
```

---

## 💡 Pro Tips

1. Use VS Code Live Server for frontend
2. Keep browser console open (F12) for debugging
3. Test with different symptom combinations
4. Check model metrics in Insights page
5. Export reports for documentation

---

## 📈 Expected Results

### Training Output
```
MODEL ACCURACY: 95.XX%
Total Diseases: 20
Total Symptoms: 50+
```

### Prediction Output
```json
{
  "success": true,
  "primary_prediction": {
    "disease": "Flu",
    "confidence": 85.5
  }
}
```

---

## 🎯 Quick Demo Script

1. **Start:** `python backend/app.py`
2. **Open:** `frontend/index.html`
3. **Register:** Create test account
4. **Diagnose:** Select: fever, cough, fatigue
5. **View:** Check prediction and recommendations
6. **Explore:** Dashboard, Insights, About pages

---

**⏱️ Total Setup Time:** 5-10 minutes
**🎓 Skill Level:** Beginner-friendly
**💻 Platform:** Windows (PowerShell)

---

**Need help? Check SETUP_GUIDE.md for detailed instructions!**
