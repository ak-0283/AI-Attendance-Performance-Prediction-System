# 🎓 AI Attendance & Performance Prediction System

A comprehensive web-based machine learning application that predicts student academic risk levels based on attendance patterns and performance indicators. The system classifies students into **Safe**, **At Risk**, and **Critical** categories to enable early intervention and targeted support.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### 🎨 User Interface
- **Dark/Light Theme Toggle** - Seamless theme switching with localStorage persistence
- **Responsive Design** - Mobile-first approach with hamburger navigation
- **Smooth Scroll-to-Top** - Fixed button with elegant animations
- **Modern UI Components** - Cards, badges, tables, alerts with consistent styling

### 📊 Core Functionality
- **Performance Prediction** - ML-powered risk classification (Safe/At Risk/Critical)
- **Interactive Dashboard** - Visual metrics with confusion matrix and accuracy charts
- **Dataset Explorer** - Browse and understand training data with styled tables
- **Model Transparency** - View hyperparameters, evaluation metrics, and training details
- **Contact System** - Functional form with validation and flash messages

### 🔧 Technical Features
- **Flask Backend** - Lightweight Python web framework
- **Random Forest Classifier** - Robust ensemble learning model
- **Form Validation** - Server-side validation with user feedback
- **Session Management** - Flash messages for user notifications
- **Static Asset Management** - Organized CSS, images, and reports

## 📁 Project Structure

```
attendance_ai_agent/
│
├── app.py                          # Flask application with routes and logic
├── train_model.py                  # Model training and evaluation script
├── requirements.txt                # Python dependencies
│
├── templates/                      # HTML templates (Jinja2)
│   ├── base.html                   # Base template with navbar, footer, theme toggle
│   ├── index.html                  # Home page with system overview
│   ├── about.html                  # Project details and architecture
│   ├── dataset.html                # Dataset information and samples
│   ├── model.html                  # Model parameters and metrics
│   ├── results.html                # Evaluation results and visualizations
│   ├── predict.html                # Prediction form
│   └── contact.html                # Contact form with copy-to-clipboard
│
├── static/                         # Static assets
│   ├── style.css                   # Complete stylesheet with dark mode
│   ├── model_report.txt            # Training metrics and performance report
│   ├── accuracy.png                # Accuracy visualization
│   └── confusion_matrix.png        # Confusion matrix heatmap
│
├── data/                           # Training datasets
│   ├── student-mat.csv             # Primary student performance dataset
│   └── student_data.csv            # Supplementary records
│
└── model/                          # Trained models
    ├── attendance_model.pkl        # Serialized Random Forest model
    └── encoder.pkl                 # Label encoder for risk categories
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for cloning)

### Step 1: Clone the Repository
```bash
git clone https://github.com/ak-0283/AI-Attendance-Performance-Prediction-System.git
cd AI-Attendance-Performance-Prediction-System
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Train the Model (Optional)
```bash
python train_model.py
```
This will:
- Load and preprocess the dataset
- Train the Random Forest classifier
- Generate evaluation metrics
- Save the model to `model/` directory
- Create `static/model_report.txt`

### Step 4: Run the Application
```bash
python app.py
```
The application will be available at: `http://127.0.0.1:5000/`

## 📖 Usage Guide

### Navigation
- **Home** - System overview, features, quick start guide
- **About** - Project architecture, mission, credits
- **Dataset** - Data sources, preprocessing, feature highlights
- **Model** - Training pipeline, hyperparameters, evaluation
- **Results** - Confusion matrix, accuracy metrics, visualizations
- **Predict** - Enter student data for risk prediction
- **Contact** - Send inquiries with copy-to-clipboard for quick contacts

### Making Predictions
1. Navigate to the **Predict** page
2. Enter student details:
   - Attendance percentage (0-100)
   - Marks obtained (0-100)
   - Assignments completed (0-20)
   - Classes missed (0-50)
3. Click **Predict Risk**
4. View the risk band and suggested interventions

### Risk Categories
- 🟢 **Safe** - Maintain current study plan; periodic check-ins
- 🟡 **At Risk** - Increase attendance; add weekly tutoring
- 🔴 **Critical** - Immediate support plan; parental engagement

## 🧠 Model Details

### Algorithm
**Random Forest Classifier** - Ensemble learning method using multiple decision trees

### Key Hyperparameters
| Parameter | Value | Purpose |
|-----------|-------|---------|
| `n_estimators` | 200 | Number of trees in the forest |
| `max_depth` | None | Unlimited tree depth for full growth |
| `class_weight` | balanced | Handles class imbalance |
| `random_state` | 42 | Reproducible results |

### Input Features
- Attendance rate/frequency
- Study time (hours per week)
- Past academic performance
- Assignments completion rate
- Classes missed count
- Support indicators (family/school)

### Evaluation Metrics
- **Precision** - Accuracy of positive predictions
- **Recall** - Coverage of actual positives
- **F1-Score** - Harmonic mean of precision and recall
- **Accuracy** - Overall correctness
- **Confusion Matrix** - Detailed classification breakdown

## 🎨 Design & Styling

### Theme System
- **CSS Variables** - Dynamic theming with `:root` and `[data-theme="dark"]`
- **Smooth Transitions** - All theme changes animated
- **LocalStorage Persistence** - Theme choice saved across sessions
- **System Preference Detection** - Respects OS-level dark mode

### Component Library
- **Sections** - Card-style blocks with borders and shadows
- **Badges** - Colored pills for risk categories
- **Tables** - Styled data/metrics tables with hover states
- **Forms** - Inputs, textareas, labels with focus rings
- **Alerts** - Success/error/info banners
- **Buttons** - Primary, secondary, CTA variants
- **Grid Layout** - Responsive 2-column cards

### Responsive Breakpoints
- Desktop: > 768px (full navbar, 2-column grid)
- Mobile: ≤ 768px (hamburger menu, single column)

## 📊 Dataset Information

### Primary Source
**UCI Student Performance Dataset** (`student-mat.csv`)
- Mathematics course performance data
- 395 students with 33 attributes
- Includes demographic, social, and academic features

### Feature Engineering
- Derived attendance rate from raw counts
- Normalized categorical variables
- Created composite study indicators
- Handled missing values with median/mode imputation

### Data Privacy
- Anonymized student identifiers
- No personally identifiable information (PII)
- Secure storage recommendations provided

## 🔒 Security & Privacy

### Best Practices Implemented
- ✅ Server-side form validation
- ✅ Flash messages for user feedback
- ✅ Secret key for session management (update in production!)
- ✅ Input sanitization in contact form
- ✅ HTTPS recommended for deployment

### Recommendations
- Change `app.secret_key` before production deployment
- Use environment variables for sensitive config
- Implement rate limiting for contact form
- Add CSRF protection for forms
- Consider database storage for submissions

## 🛠️ Technologies Used

### Backend
- **Flask** - Lightweight WSGI web framework
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation (training script)
- **scikit-learn** - Machine learning library
- **Pickle** - Model serialization

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with variables
- **Jinja2** - Template engine
- **Vanilla JavaScript** - Theme toggle, scroll button, clipboard

### Development Tools
- **Git** - Version control
- **GitHub** - Code hosting
- **VS Code** - IDE (recommended)
- **PowerShell** - Terminal environment

## 📈 Performance

### Model Metrics
Check `static/model_report.txt` for detailed metrics after training.

Typical performance:
- Training accuracy: ~85-90%
- Test accuracy: ~80-85%
- F1-Score: ~0.82 (macro average)

### Web Performance
- Lightweight CSS (~10KB compressed)
- No external dependencies (fonts, CDNs)
- Fast page loads (<100ms local)
- Efficient Flask routing

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contribution
- Add SHAP/LIME for model explainability
- Implement admin dashboard for cohort monitoring
- Add email notifications (SMTP integration)
- Create API endpoints (REST/GraphQL)
- Add unit tests with pytest
- Implement database backend (SQLite/PostgreSQL)
- Add user authentication system
- Create feature importance visualization
- Export prediction reports as PDF

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 Abhay Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👨‍💻 Developer

**Abhay Kumar**  
BCA Final Year Student  
Passionate about AI/ML and Web Development


## 🙏 Acknowledgments

- **UCI Machine Learning Repository** - Dataset source
- **Flask Community** - Framework and documentation
- **scikit-learn** - ML tools and algorithms
- **VS Code Copilot** - Development assistance


## 🔮 Roadmap

- [ ] Add student dashboard with historical predictions
- [ ] Implement batch prediction (CSV upload)
- [ ] Create REST API with authentication
- [ ] Add real-time notifications
- [ ] Integrate with LMS systems
- [ ] Multi-language support
- [ ] Mobile app (React Native/Flutter)
- [ ] Advanced analytics and trends

## 🎯 Project Goals

1. **Early Intervention** - Identify at-risk students before outcomes decline
2. **Data-Driven Decisions** - Replace intuition with evidence-based insights
3. **Accessibility** - Simple, intuitive interface for educators
4. **Transparency** - Explainable predictions with clear metrics
5. **Scalability** - Easily extend to multiple cohorts and institutions

---

⭐ **Star this repo** if you find it useful!  
🐛 **Report issues** to help improve the project  
🤝 **Contribute** to make education better with AI

**Made with ❤️ by Abhay Kumar | © 2025**
