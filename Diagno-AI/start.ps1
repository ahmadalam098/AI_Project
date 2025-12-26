# Diagno AI - Quick Start Script
# Run this script to set up and start the system

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "       DIAGNO AI - Quick Start Script" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check Python
Write-Host "[1/5] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "✗ Python not found! Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

# Step 2: Install Dependencies
Write-Host ""
Write-Host "[2/5] Installing Python dependencies..." -ForegroundColor Yellow
Write-Host "This may take a few minutes..." -ForegroundColor Gray
try {
    Set-Location -Path "backend"
    pip install -r requirements.txt --quiet
    Write-Host "✓ Dependencies installed successfully!" -ForegroundColor Green
}
catch {
    Write-Host "⚠ Some packages may have failed to install." -ForegroundColor Yellow
}

# Step 3: Check if model exists
Write-Host ""
Write-Host "[3/5] Checking for trained model..." -ForegroundColor Yellow
if (Test-Path "../models/disease_model.pkl") {
    Write-Host "✓ Model file found!" -ForegroundColor Green
    $retrain = Read-Host "Do you want to retrain the model? (y/n)"
    if ($retrain -eq "y") {
        Write-Host "Training model..." -ForegroundColor Yellow
        python train_model.py
    }
}
else {
    Write-Host "⚠ Model not found. Training now..." -ForegroundColor Yellow
    python train_model.py
}

# Step 4: Start Backend Server
Write-Host ""
Write-Host "[4/5] Starting Flask backend server..." -ForegroundColor Yellow
Write-Host "Server will run on http://localhost:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  Backend server is starting..." -ForegroundColor Green
Write-Host "  Keep this window open!" -ForegroundColor Green
Write-Host "" -ForegroundColor Green
Write-Host "  To access the frontend:" -ForegroundColor White
Write-Host "  1. Open a new browser window" -ForegroundColor White
Write-Host "  2. Navigate to: frontend/index.html" -ForegroundColor White
Write-Host "  3. Or use Live Server in VS Code" -ForegroundColor White
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Run the server
python app.py
