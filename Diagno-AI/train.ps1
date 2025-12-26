# Run this script to ONLY train the model
# Use this if you want to retrain without starting the server

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "       DIAGNO AI - Model Training Script" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Starting model training..." -ForegroundColor Yellow
Write-Host "This will take a few moments..." -ForegroundColor Gray
Write-Host ""

Set-Location -Path "backend"
python train_model.py

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  Model training completed!" -ForegroundColor Green
Write-Host "  You can now run 'start.ps1' to start the server" -ForegroundColor White
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""

Read-Host "Press Enter to exit"
