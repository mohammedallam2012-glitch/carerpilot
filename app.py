import os
import sys
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24).hex())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/recruiter')
def recruiter():
    return render_template('recruiter.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400
    job_title = data.get('job_title', '')
    try:
        years_exp = int(data.get('years_exp', 0))
    except (ValueError, TypeError):
        years_exp = 0
    skills = data.get('skills', [])
    if not isinstance(skills, list):
        skills = []
    score = min(max(round((len(skills) * 7 + 20 + years_exp * 3) % 100), 10), 95)
    return jsonify({
        'survival_score': score,
        'risk_level': 'low' if score > 70 else 'medium' if score > 40 else 'high',
        'alternative_jobs': [
            {'title': 'مشرف جودة', 'match': 89},
            {'title': 'مدير وردية', 'match': 82},
            {'title': 'مدير مستودع', 'match': 76},
        ],
        'courses': [
            {'name': 'Excel للمبتدئين والمتقدمين', 'platform': 'Udemy', 'rating': 4.8},
            {'name': 'مراقبة الجودة ISO 9001', 'platform': 'Alison', 'rating': 4.7},
        ]
    })

@app.route('/api/login', methods=['POST'])
def login_api():
    data = request.form
    email = data.get('email', '')
    password = data.get('password', '')
    if not email or not password:
        return jsonify({'error': 'البريد الإلكتروني وكلمة المرور مطلوبان'}), 400
    return jsonify({'message': 'تم تسجيل الدخول بنجاح', 'redirect': '/dashboard'})

@app.route('/api/register', methods=['POST'])
def register_api():
    data = request.form
    email = data.get('email', '')
    password = data.get('password', '')
    name = data.get('full_name', '')
    if not email or not password or not name:
        return jsonify({'error': 'جميع الحقول المطلوبة غير مكتملة'}), 400
    return jsonify({'message': 'تم إنشاء الحساب بنجاح', 'redirect': '/upload'})

@app.route('/api/contact-investor', methods=['POST'])
def contact_investor():
    email = request.json.get('email')
    if not email or '@' not in email:
        return jsonify({'error': 'Invalid email'}), 400
    return jsonify({'message': 'تم إرسال اهتمامك! سنتواصل معك قريباً'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG', '').lower() == 'true')
