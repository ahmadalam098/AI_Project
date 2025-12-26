// API Configuration
const API_URL = 'http://localhost:5000';

// Authentication Helper Functions
function getToken() {
    return localStorage.getItem('diagno_token');
}

function setToken(token) {
    localStorage.setItem('diagno_token', token);
}

function removeToken() {
    localStorage.removeItem('diagno_token');
    localStorage.removeItem('diagno_user');
}

function getUser() {
    const user = localStorage.getItem('diagno_user');
    return user ? JSON.parse(user) : null;
}

function setUser(user) {
    localStorage.setItem('diagno_user', JSON.stringify(user));
}

function isAuthenticated() {
    return !!getToken();
}

// Update Navigation based on auth status
function updateNavigation() {
    const authLinks = document.querySelectorAll('.auth-required');
    const guestLinks = document.querySelectorAll('.guest-only');
    const userInfo = document.getElementById('userInfo');

    if (isAuthenticated()) {
        authLinks.forEach(link => link.style.display = 'block');
        guestLinks.forEach(link => link.style.display = 'none');

        if (userInfo) {
            const user = getUser();
            userInfo.innerHTML = `
                <div class="user-info">
                    <div class="user-avatar">${user.fullname ? user.fullname.charAt(0).toUpperCase() : 'U'}</div>
                    <span>${user.username}</span>
                    <button onclick="logout()" class="btn btn-danger" style="padding: 0.5rem 1rem; margin-left: 1rem;">Logout</button>
                </div>
            `;
        }
    } else {
        authLinks.forEach(link => link.style.display = 'none');
        guestLinks.forEach(link => link.style.display = 'block');

        if (userInfo) {
            userInfo.innerHTML = '';
        }
    }
}

// Logout Function
function logout() {
    if (confirm('Are you sure you want to logout?')) {
        removeToken();
        showAlert('Logged out successfully!', 'success');
        setTimeout(() => {
            window.location.href = 'login.html';
        }, 1000);
    }
}

// API Request Helper
async function apiRequest(endpoint, method = 'GET', data = null, requiresAuth = false) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        }
    };

    if (requiresAuth) {
        const token = getToken();
        if (token) {
            options.headers['Authorization'] = `Bearer ${token}`;
        }
    }

    if (data && method !== 'GET') {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(`${API_URL}${endpoint}`, options);
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('API Error:', error);
        return { success: false, message: 'Network error. Please check if the server is running.' };
    }
}

// Show Alert Message
function showAlert(message, type = 'info', duration = 5000) {
    const alertContainer = document.getElementById('alertContainer');

    if (!alertContainer) {
        const container = document.createElement('div');
        container.id = 'alertContainer';
        container.style.position = 'fixed';
        container.style.top = '80px';
        container.style.right = '20px';
        container.style.zIndex = '9999';
        container.style.maxWidth = '400px';
        document.body.appendChild(container);
    }

    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.style.animation = 'fadeIn 0.5s';
    alert.innerHTML = `
        <strong>${type === 'error' ? '❌' : type === 'success' ? '✓' : 'ℹ'}</strong>
        <span>${message}</span>
    `;

    document.getElementById('alertContainer').appendChild(alert);

    setTimeout(() => {
        alert.style.animation = 'fadeOut 0.5s';
        setTimeout(() => alert.remove(), 500);
    }, duration);
}

// Show Loading Spinner
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = '<div class="spinner"></div>';
    }
}

// Hide Loading Spinner
function hideLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = '';
    }
}

// Format Date
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Format Symptom Name
function formatSymptomName(symptom) {
    return symptom.replace(/_/g, ' ').split(' ').map(word =>
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
}

// Check Protected Pages
function checkAuth() {
    const protectedPages = ['dashboard.html', 'diagnosis.html', 'result.html'];
    const currentPage = window.location.pathname.split('/').pop();

    if (protectedPages.includes(currentPage) && !isAuthenticated()) {
        showAlert('Please login to access this page', 'error');
        setTimeout(() => {
            window.location.href = 'login.html';
        }, 1500);
        return false;
    }
    return true;
}

// Voice Recognition (if supported)
function startVoiceRecognition(callback) {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();

        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onresult = function (event) {
            const transcript = event.results[0][0].transcript;
            callback(transcript);
        };

        recognition.onerror = function (event) {
            showAlert('Voice recognition error: ' + event.error, 'error');
        };

        recognition.start();
        showAlert('🎤 Listening... Speak your symptoms', 'info', 3000);

        return recognition;
    } else {
        showAlert('Voice recognition not supported in this browser', 'error');
        return null;
    }
}

// Export to PDF (simple text version)
function exportToPDF(elementId, filename = 'ai-health-diagnostic-report.pdf') {
    showAlert('Preparing PDF export...', 'info');

    // This is a simple implementation. For production, use jsPDF library
    const element = document.getElementById(elementId);
    if (element) {
        const content = element.innerText;
        const blob = new Blob([content], { type: 'text/plain' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = filename.replace('.pdf', '.txt');
        link.click();

        showAlert('Report exported as text file', 'success');
    }
}

// Search Symptoms
function searchSymptoms(query, symptoms) {
    query = query.toLowerCase();
    return symptoms.filter(symptom =>
        symptom.toLowerCase().includes(query)
    );
}

// Calculate Severity Color
function getSeverityColor(severity) {
    const severityLower = severity.toLowerCase();
    if (severityLower.includes('mild')) return '#10B981';
    if (severityLower.includes('moderate')) return '#F59E0B';
    if (severityLower.includes('severe')) return '#EF4444';
    if (severityLower.includes('chronic')) return '#8B5CF6';
    return '#6B7280';
}

// Confidence Color based on percentage
function getConfidenceColor(confidence) {
    if (confidence >= 80) return '#10B981';
    if (confidence >= 60) return '#F59E0B';
    if (confidence >= 40) return '#FF6B6B';
    return '#EF4444';
}

// Initialize page
document.addEventListener('DOMContentLoaded', function () {
    updateNavigation();
    checkAuth();

    // Set active nav link
    const currentPage = window.location.pathname.split('/').pop();
    document.querySelectorAll('.nav-links a').forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });
});

// Add fadeOut animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeOut {
        from { opacity: 1; }
        to { opacity: 0; }
    }
`;
document.head.appendChild(style);
