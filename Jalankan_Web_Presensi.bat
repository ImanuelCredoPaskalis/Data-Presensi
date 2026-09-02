@echo off
title Sistem Presensi Mahasiswa - Web App
cd /d "%~dp0"

echo ============================================================
echo   SISTEM PRESENSI MAHASISWA ^& KELAS - Web App Streamlit
echo   Lab Micro Teaching FisMat
echo ============================================================
echo.

REM Cek apakah Python tersedia
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python tidak ditemukan!
    echo Pastikan Python sudah terinstal dan ada di PATH.
    pause
    exit /b 1
)

REM Install dependensi jika belum
echo [*] Memeriksa dependensi...
pip install -r requirements.txt --quiet

echo.
echo [*] Menjalankan aplikasi web...
echo [*] Buka browser dan akses: http://localhost:8501
echo.
echo Tekan Ctrl+C di jendela ini untuk menghentikan server.
echo ============================================================
echo.

streamlit run app.py --server.port 8501 --server.headless false

pause
