# 🧪 Diagno AI - Testing Guide

## Quick Test Script

Follow these steps to verify everything is working:

## 1️⃣ Backend API Tests

### Start the Backend Server
```powershell
cd "d:\AI Projects\Diagno-AI\backend"
python app.py
```

### Test API Endpoints (Open new terminal)

```powershell
# Test 1: Server Health Check
curl http://localhost:5000/

# Test 2: Get All Symptoms
curl http://localhost:5000/get-symptoms

# Test 3: Get Model Accuracy
curl http://localhost:5000/get-accuracy

# Test 4: Get All Diseases
curl http://localhost:5000/get-diseases

# Test 5: Get Model Metrics
curl http://localhost:5000/get-metrics

# Test 6: Get Chart Data
curl http://localhost:5000/get-chart-data
```

### Test Prediction API (Advanced)

```powershell
curl -X POST http://localhost:5000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"symptoms\": [\"fever\", \"cough\", \"fatigue\"]}"
```

Expected Response:
```json
{
  "success": true,
  "primary_prediction": {
    "disease": "Flu",
    "confidence": 85.5
  },
  "top_predictions": [...],
  "disease_info": {...}
}
```

---

## 2️⃣ Frontend Tests

### Test User Authentication

1. **Open** `frontend/index.html` in browser
2. **Click** "Login" in navigation
3. **Sign Up** with new account:
   - Full Name: Test User
   - Email: test@diagnoai.com
   - Username: testuser
   - Password: test123
4. **Verify** account creation success message
5. **Login** with created credentials
6. **Check** if redirected to dashboard

**Expected Result:** ✅ Successful login, see dashboard with user name

---

### Test Disease Prediction

1. **Navigate** to Diagnosis page
2. **Select symptoms** (at least 3):
   - ✅ Fever
   - ✅ Cough  
   - ✅ Fatigue
   - ✅ Body Ache
3. **Click** "Analyze Symptoms & Predict Disease"
4. **Wait** for results (should be instant)

**Expected Result:** 
- ✅ Disease prediction displayed
- ✅ Confidence percentage shown
- ✅ Top 3 predictions visible
- ✅ Medical recommendations displayed
- ✅ Treatment suggestions visible
- ✅ Diet recommendations shown

---

### Test Insights Page

1. **Navigate** to Insights page
2. **Verify** all metrics load:
   - Model Accuracy
   - Total Diseases
   - Total Symptoms
   - Training Samples
3. **Check** all charts display:
   - Model Performance Chart
   - Severity Distribution Chart
   - Disease Distribution Chart
   - Symptom Frequency Chart

**Expected Result:** ✅ All statistics and charts load correctly

---

### Test Dashboard

1. **Navigate** to Dashboard
2. **Check** user welcome message
3. **Verify** system statistics
4. **Check** recent diagnoses section
5. **Verify** disease list loads

**Expected Result:** ✅ All sections display data correctly

---

## 3️⃣ Comprehensive Test Cases

### Test Case 1: Flu Detection
**Input Symptoms:**
- fever
- cough
- fatigue
- body_ache
- headache

**Expected Output:**
- Primary Disease: Flu
- Confidence: > 80%
- Severity: Moderate

---

### Test Case 2: COVID-19 Detection
**Input Symptoms:**
- fever
- dry_cough
- fatigue
- loss_of_taste
- difficulty_breathing

**Expected Output:**
- Primary Disease: COVID-19
- Confidence: > 75%
- Severity: Moderate to Severe
- ⚠️ Critical warning displayed

---

### Test Case 3: Diabetes Detection
**Input Symptoms:**
- frequent_urination
- excessive_thirst
- hunger
- fatigue
- blurred_vision

**Expected Output:**
- Primary Disease: Diabetes
- Confidence: > 80%
- Severity: Chronic - Manageable

---

### Test Case 4: Common Cold
**Input Symptoms:**
- cough
- runny_nose
- sneezing
- sore_throat

**Expected Output:**
- Primary Disease: Common Cold
- Confidence: > 75%
- Severity: Mild

---

### Test Case 5: Hypertension
**Input Symptoms:**
- headache
- dizziness
- chest_pain
- shortness_of_breath

**Expected Output:**
- Primary Disease: Hypertension
- Confidence: > 70%
- Severity: Chronic - Manageable

---

## 4️⃣ Feature-by-Feature Testing

### ✅ Authentication System
- [ ] User registration works
- [ ] Password encryption (bcrypt)
- [ ] JWT token generation
- [ ] Login functionality
- [ ] Logout functionality
- [ ] Protected routes redirect to login
- [ ] Token expiry (24 hours)

### ✅ Symptom Selection
- [ ] All 50+ symptoms load
- [ ] Checkbox selection works
- [ ] Search functionality works
- [ ] Selected count updates
- [ ] Clear all button works
- [ ] Multiple symptom selection

### ✅ AI Prediction Engine
- [ ] Prediction completes < 1 second
- [ ] Primary disease shown
- [ ] Confidence score displayed
- [ ] Top 3 predictions listed
- [ ] All predictions have confidence scores
- [ ] Symptoms analyzed list shown

### ✅ Medical Recommendations
- [ ] Disease description shown
- [ ] Prevention tips displayed
- [ ] Treatment suggestions listed
- [ ] Medicine recommendations shown
- [ ] Diet recommendations displayed
- [ ] Severity indicator visible

### ✅ Visualizations
- [ ] Model accuracy displayed
- [ ] Performance chart renders
- [ ] Severity distribution pie chart
- [ ] Disease distribution bar chart
- [ ] Symptom frequency chart
- [ ] Charts are interactive

### ✅ User Dashboard
- [ ] Welcome message shows user name
- [ ] Quick action cards work
- [ ] System statistics load
- [ ] Recent reports displayed
- [ ] Disease list loads
- [ ] Health tips shown

### ✅ Report Management
- [ ] Reports saved after diagnosis
- [ ] View reports functionality
- [ ] Report history displays
- [ ] Export report button works
- [ ] Report timestamp shown

---

## 5️⃣ Browser Compatibility Tests

Test in multiple browsers:

### Google Chrome
- [ ] All features work
- [ ] Charts display correctly
- [ ] Voice input works (optional)

### Microsoft Edge
- [ ] All features work
- [ ] Charts display correctly
- [ ] Voice input works (optional)

### Mozilla Firefox
- [ ] All features work
- [ ] Charts display correctly
- [ ] Voice input may not work

### Safari (Mac only)
- [ ] All features work
- [ ] Charts display correctly
- [ ] Voice input may not work

---

## 6️⃣ Performance Tests

### Response Time Tests
- [ ] Home page loads < 1 second
- [ ] API prediction < 500ms
- [ ] Charts load < 2 seconds
- [ ] Login/Signup < 1 second

### Model Performance
- [ ] Accuracy ≥ 95%
- [ ] Training samples: 1000
- [ ] Testing samples: 200
- [ ] All 20 diseases classified

---

## 7️⃣ Error Handling Tests

### Backend Errors
- [ ] Invalid symptoms handled
- [ ] Empty symptom list rejected
- [ ] Invalid credentials rejected
- [ ] Duplicate username rejected
- [ ] Invalid token handled

### Frontend Errors
- [ ] Network error displayed
- [ ] Server offline message
- [ ] Empty form validation
- [ ] Password mismatch check
- [ ] Loading states shown

---

## 8️⃣ Security Tests

### Authentication Security
- [ ] Passwords are hashed (bcrypt)
- [ ] JWT tokens expire after 24 hours
- [ ] Protected routes require auth
- [ ] Tokens stored in localStorage
- [ ] Logout clears tokens

### API Security
- [ ] CORS enabled correctly
- [ ] Protected endpoints check tokens
- [ ] Invalid tokens rejected
- [ ] SQL injection not possible (no DB)

---

## 9️⃣ Mobile Responsiveness Tests

Test on mobile devices or resize browser:

- [ ] Navigation menu responsive
- [ ] Cards stack vertically
- [ ] Forms are usable
- [ ] Charts resize properly
- [ ] Buttons are tappable
- [ ] Text is readable

---

## 🔟 Edge Cases & Stress Tests

### Edge Cases
- [ ] Test with 0 symptoms (should fail)
- [ ] Test with 1 symptom (should work)
- [ ] Test with all symptoms selected
- [ ] Test with special characters in username
- [ ] Test with very long password

### Stress Tests
- [ ] Multiple rapid predictions
- [ ] Many symptoms selected (20+)
- [ ] Quick login/logout cycles
- [ ] Browser refresh during prediction
- [ ] Multiple browser tabs

---

## 🎯 Success Criteria

### ✅ Minimum Requirements (Must Pass)
- [x] Model trains successfully
- [x] Backend server starts
- [x] Frontend loads in browser
- [x] User can register/login
- [x] Disease prediction works
- [x] Results display correctly
- [x] Charts load

### ⭐ Excellent Requirements (Should Pass)
- [x] 95%+ model accuracy
- [x] < 1 second prediction time
- [x] All 20 diseases work
- [x] All visualizations render
- [x] Mobile responsive
- [x] Error handling works
- [x] Reports save correctly

---

## 🐛 Common Issues & Solutions

### Issue: "Module not found"
**Solution:** `pip install -r backend/requirements.txt`

### Issue: "Model file not found"
**Solution:** Run `python backend/train_model.py`

### Issue: "CORS error"
**Solution:** Ensure Flask server is running with flask-cors installed

### Issue: Charts not loading
**Solution:** Check internet connection (Chart.js CDN)

### Issue: Voice input not working
**Solution:** Use Chrome browser, allow microphone permission

---

## 📊 Test Results Template

```
========================================
DIAGNO AI - TEST RESULTS
========================================
Date: _______________
Tester: _______________

Backend Tests:          [ ] PASS  [ ] FAIL
Authentication:         [ ] PASS  [ ] FAIL
Disease Prediction:     [ ] PASS  [ ] FAIL
Visualizations:         [ ] PASS  [ ] FAIL
Dashboard:              [ ] PASS  [ ] FAIL
Report Management:      [ ] PASS  [ ] FAIL
Mobile Responsive:      [ ] PASS  [ ] FAIL
Error Handling:         [ ] PASS  [ ] FAIL

Overall Status:         [ ] PASS  [ ] FAIL

Notes:
_________________________________________
_________________________________________
_________________________________________
========================================
```

---

## 🎉 Final Verification

If all tests pass:

✅ Your Diagno AI system is production-ready!
✅ All core features are functional
✅ System meets requirements
✅ Ready for demonstration

---

**Remember:** This is for educational purposes. Always consult healthcare professionals for actual medical diagnosis!
