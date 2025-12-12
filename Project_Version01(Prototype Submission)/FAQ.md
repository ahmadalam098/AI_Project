# ❓ Diagno AI - Frequently Asked Questions (FAQ)

## 🚀 Getting Started

### Q: Do I need a database to run this project?
**A:** No! This project uses in-memory storage. All data is stored temporarily during runtime.

### Q: What version of Python do I need?
**A:** Python 3.8 or higher is required. Check with: `python --version`

### Q: Do I need to download any datasets from Kaggle?
**A:** No! The training script automatically creates a comprehensive medical dataset with 1000+ samples covering 20 diseases and 50+ symptoms.

### Q: How long does setup take?
**A:** 5-10 minutes including installation and training.

---

## 🔧 Installation Issues

### Q: "pip is not recognized" error
**A:** Python is not in your PATH. Try:
```powershell
python -m pip install -r backend/requirements.txt
```

### Q: "No module named 'flask'" error
**A:** Dependencies not installed. Run:
```powershell
cd "d:\AI Projects\Diagno-AI\backend"
pip install -r requirements.txt
```

### Q: Installation takes too long
**A:** Some packages (numpy, scikit-learn) are large. Wait or try:
```powershell
pip install --no-cache-dir -r requirements.txt
```

### Q: "Permission denied" error during installation
**A:** Run PowerShell as Administrator or use:
```powershell
pip install --user -r requirements.txt
```

---

## 🤖 Model Training Issues

### Q: "FileNotFoundError" during training
**A:** Make sure you're in the correct directory:
```powershell
cd "d:\AI Projects\Diagno-AI\backend"
python train_model.py
```

### Q: Training is very slow
**A:** Training should take 10-30 seconds. If slower:
- Close other programs
- Check CPU usage
- Reduce dataset size in `train_model.py` (change 50 to 25 in line with `range(50)`)

### Q: "Model accuracy is low" (below 90%)
**A:** This is unusual. Try:
1. Delete existing model: `del ..\models\disease_model.pkl`
2. Retrain: `python train_model.py`
3. Check console for errors

### Q: Where is the trained model saved?
**A:** In `models/disease_model.pkl` (created automatically)

### Q: Do I need to retrain every time?
**A:** No! Train once, then just run `app.py`. Retrain only if you want to update the model.

---

## 🌐 Backend/Server Issues

### Q: "Address already in use" error
**A:** Port 5000 is busy. Solution:
```powershell
# Option 1: Find and kill process
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# Option 2: Use different port
# Edit app.py, change: app.run(port=5001)
```

### Q: Server starts but immediately stops
**A:** Check for errors in terminal. Common causes:
- Model not trained (run `train_model.py` first)
- Missing dependencies (reinstall requirements.txt)
- Port conflict (change port in app.py)

### Q: "Model file not found" error
**A:** Train the model first:
```powershell
cd backend
python train_model.py
```

### Q: How do I stop the server?
**A:** Press `Ctrl+C` in the terminal running the server

### Q: Can I run server in background?
**A:** Yes, but keep the terminal open or use:
```powershell
Start-Process python -ArgumentList "app.py" -WindowStyle Hidden
```

---

## 🖥️ Frontend Issues

### Q: Blank page when opening index.html
**A:** Check:
1. Is the file in correct location?
2. Open browser console (F12) for errors
3. Check if CSS/JS files exist in `assets/` folder

### Q: "API connection failed" error
**A:** Backend server not running. Start it:
```powershell
cd backend
python app.py
```

### Q: Charts not displaying
**A:** 
1. Check internet connection (Chart.js loads from CDN)
2. Open browser console (F12) for errors
3. Try different browser

### Q: Styling looks broken
**A:** Check if `assets/css/style.css` exists. Browser cache issue? Press `Ctrl+F5` to hard refresh.

### Q: JavaScript not working
**A:** Check if `assets/js/app.js` exists. Open browser console (F12) for errors.

---

## 🔐 Authentication Issues

### Q: "Invalid credentials" when logging in
**A:** Make sure:
1. You created an account first (signup)
2. Username/password are correct
3. Backend server is running

### Q: "User already exists" error
**A:** That username is taken (in current session). Try:
1. Different username
2. Restart server (clears memory)

### Q: Logged out automatically
**A:** JWT token expired (24 hours). Login again.

### Q: "Token is invalid" error
**A:** Token expired or corrupted. Clear browser storage:
```javascript
// In browser console (F12):
localStorage.clear();
```

### Q: Can't access diagnosis page
**A:** You need to login first. System redirects to login page automatically.

---

## 🔬 Diagnosis/Prediction Issues

### Q: "No symptoms provided" error
**A:** Select at least one symptom before clicking "Analyze"

### Q: Prediction always returns same disease
**A:** 
1. Check if you're selecting different symptoms
2. Retrain model: `python train_model.py`
3. Restart backend server

### Q: Confidence scores are always 100%
**A:** This means model is very certain. Try:
- Selecting fewer symptoms
- Selecting unrelated symptoms
- Different symptom combinations

### Q: Prediction takes too long
**A:** Should be instant (<1 second). If slow:
- Check server terminal for errors
- Restart backend server
- Check system resources

### Q: "Error: str object has no attribute predict"
**A:** Model file corrupted. Retrain:
```powershell
cd backend
python train_model.py
```

---

## 📊 Visualization Issues

### Q: Charts show "Loading..." forever
**A:** 
1. Check internet connection (Chart.js CDN)
2. Open console (F12) for errors
3. Verify API endpoint works: `http://localhost:5000/get-chart-data`

### Q: Charts display but no data
**A:** Backend not returning data. Check:
1. Server is running
2. Visit: `http://localhost:5000/get-chart-data`
3. Should return JSON data

### Q: Confusion matrix not showing
**A:** It's generated during training. Check if file exists:
`models/confusion_matrix.png`

### Q: Charts look distorted
**A:** Browser zoom issue. Reset zoom to 100% (`Ctrl+0`)

---

## 🎤 Voice Input Issues

### Q: Voice input button doesn't work
**A:** Voice recognition requires:
1. HTTPS or localhost
2. Microphone permission
3. Supported browser (Chrome recommended)
4. English language setting

### Q: "Microphone not available" error
**A:** 
1. Check browser permissions
2. Allow microphone access
3. Check system microphone settings

### Q: Voice not detecting symptoms
**A:** Speak clearly and say symptom names like:
- "fever"
- "cough"
- "headache"
- Not full sentences

---

## 💾 Data & Storage Issues

### Q: Where is my data stored?
**A:** In-memory only (RAM). Data is lost when:
- Server restarts
- Browser closes
- You logout

### Q: Can I save diagnosis permanently?
**A:** Not in this version. Data is session-only. To add permanent storage:
1. Add database (PostgreSQL, MongoDB)
2. Modify backend to save to DB
3. Update API endpoints

### Q: Reports disappeared after logout
**A:** Expected behavior. Reports are session-only (no database).

### Q: How to export diagnosis?
**A:** Click "Export Report" button on results page (downloads as text file).

---

## 🌐 Browser Compatibility

### Q: Which browsers are supported?
**A:** 
- ✅ Chrome (Recommended)
- ✅ Edge
- ✅ Firefox
- ✅ Safari
- ⚠️ IE11 (Not recommended)

### Q: Features not working in Firefox
**A:** Most features work. Voice input may not work in Firefox.

### Q: Mobile browser issues
**A:** Site is mobile-responsive. Use Chrome mobile for best experience.

---

## 🔧 Performance Issues

### Q: Website is slow
**A:** 
1. Close other browser tabs
2. Check internet connection
3. Clear browser cache
4. Restart browser

### Q: Prediction takes > 5 seconds
**A:** Should be instant. Problem likely:
- Server overloaded
- Network issue
- Restart backend server

### Q: High CPU usage
**A:** 
- Normal during model training
- Should be low during normal use
- Close other programs

---

## 📱 Mobile Issues

### Q: Layout looks broken on mobile
**A:** 
1. Site is responsive
2. Try landscape mode
3. Zoom to 100%
4. Use modern mobile browser

### Q: Can't click buttons on mobile
**A:** Buttons might be too small. Use zoom or try different device.

### Q: Charts too small on mobile
**A:** Rotate device to landscape mode for better view.

---

## 🐛 Common Error Messages

### Error: "CORS policy blocked"
**Solution:** Make sure:
1. Backend server is running
2. `flask-cors` is installed
3. Using correct API URL (localhost:5000)

### Error: "Failed to fetch"
**Solution:** 
1. Backend server not running
2. Wrong API URL
3. Network issue

### Error: "Unexpected token < in JSON"
**Solution:** API returned HTML instead of JSON. Usually means:
1. Server crashed
2. Wrong endpoint
3. Check server terminal for errors

### Error: "Cannot read property of undefined"
**Solution:** JavaScript error. Check:
1. Browser console (F12)
2. Refresh page
3. Clear browser cache

---

## 🎯 Feature-Specific Questions

### Q: How accurate is the AI model?
**A:** 95%+ accuracy on test data. Remember, this is for educational purposes only.

### Q: Can I add more diseases?
**A:** Yes! Edit `train_model.py`:
1. Add disease to `diseases` dictionary
2. List its symptoms
3. Retrain model

### Q: Can I add more symptoms?
**A:** Yes! Edit `train_model.py`:
1. Add symptoms to disease lists
2. Retrain model
3. Restart server

### Q: How to change the accuracy threshold?
**A:** Model doesn't use threshold. It always returns prediction with confidence score.

### Q: Can I use different ML algorithm?
**A:** Yes! In `train_model.py`:
```python
# Replace SVM with:
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
```

---

## 🔒 Security Questions

### Q: Is my password secure?
**A:** Yes! Passwords are hashed with bcrypt (industry standard).

### Q: Is my data private?
**A:** Data is in-memory only (no database), lost when server restarts.

### Q: Can others see my diagnoses?
**A:** No, if you're the only one using the server. In production, add proper user isolation.

### Q: Should I use this for real diagnosis?
**A:** ⚠️ **NO!** This is for educational purposes only. Always consult healthcare professionals.

---

## 📊 About the Model

### Q: What algorithm is used?
**A:** Support Vector Machine (SVM) with RBF kernel

### Q: How many diseases can it detect?
**A:** 20 diseases including Flu, COVID-19, Diabetes, etc.

### Q: How many symptoms does it analyze?
**A:** 50+ symptoms

### Q: Training data source?
**A:** Synthetically generated based on medical knowledge (not real patient data)

### Q: Can it diagnose rare diseases?
**A:** No, only the 20 common diseases it was trained on

---

## 🚀 Advanced Questions

### Q: How to deploy to production?
**A:** 
1. Add proper database (PostgreSQL)
2. Use production WSGI server (Gunicorn)
3. Add HTTPS (SSL certificate)
4. Deploy to cloud (Heroku, AWS, Azure)
5. Add user authentication improvements

### Q: How to improve model accuracy?
**A:** 
1. Collect real medical data
2. Increase training samples
3. Feature engineering
4. Try ensemble methods
5. Cross-validation
6. Hyperparameter tuning

### Q: Can I connect to a real medical database?
**A:** Yes, but requires:
1. Medical data access rights
2. HIPAA compliance (if US)
3. Data privacy regulations
4. Ethical approval

### Q: How to add more features?
**A:** Code is well-structured:
- Backend: Add endpoints in `app.py`
- Frontend: Add pages in `frontend/`
- Model: Modify `train_model.py`

---

## 📚 Learning Resources

### Q: I want to understand the ML code better
**A:** Learn:
- Scikit-learn documentation
- SVM algorithm concepts
- Python pandas basics
- Machine learning fundamentals

### Q: I want to improve the frontend
**A:** Learn:
- HTML/CSS basics
- JavaScript (vanilla)
- Chart.js documentation
- Responsive design

### Q: I want to enhance the backend
**A:** Learn:
- Flask framework
- REST API design
- JWT authentication
- Python best practices

---

## ⚠️ Important Reminders

### Medical Disclaimer
**This system is for EDUCATIONAL purposes only!**
- NOT for actual medical diagnosis
- NOT a replacement for doctors
- NOT validated on real patients
- ALWAYS consult healthcare professionals

### Data Privacy
- No database = No persistent storage
- Data lost when server restarts
- Not suitable for production medical use
- Add proper database for production

### Legal
- Follow local healthcare regulations
- Don't use for commercial purposes without proper licensing
- Get medical professional validation
- Ensure HIPAA/GDPR compliance if needed

---

## 🆘 Still Need Help?

If you're still having issues:

1. **Check Documentation:**
   - READ `SETUP_GUIDE.md`
   - Check `TESTING_GUIDE.md`
   - Review `QUICK_REFERENCE.md`

2. **Debug Steps:**
   - Check browser console (F12)
   - Check server terminal
   - Verify all files exist
   - Check Python version
   - Reinstall dependencies

3. **Common Solutions:**
   - Restart server
   - Retrain model
   - Clear browser cache
   - Refresh page (Ctrl+F5)

4. **Last Resort:**
   - Delete project
   - Re-extract/re-create
   - Start fresh with setup guide

---

## 🎉 Success Tips

✅ **Always train model first!**
✅ **Keep server running while using app**
✅ **Use Chrome for best experience**
✅ **Check documentation before asking**
✅ **Test with different symptoms**

---

**Remember: This project is for learning and demonstration. Enjoy building and learning! 🚀**
