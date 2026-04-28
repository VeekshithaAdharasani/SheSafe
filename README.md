# 🛡️ SheSafe – Intelligent Safety Dashboard

**A Production-Quality AI-Powered Smart Wearable Safety System for Women**

![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📋 Overview

SheSafe is a **startup-level, production-quality Streamlit application** that simulates an intelligent wearable safety system designed for personal security monitoring. The dashboard uses advanced multi-sensor fusion to analyze real-time physiological and kinematic data and classify user safety status with high accuracy.

### 🎯 Perfect For:
- **Portfolio Projects** – Demonstrates full-stack engineering thinking
- **Interview Demos** – Shows UI/UX design, algorithms, and code quality
- **Technical Interviews** – Discusses safety systems, sensor fusion, and AI/ML logic
- **Startup Showcases** – Professional, polished, production-ready UI

---

## ✨ Key Features

### 🔐 Core Safety System
- **Multi-Sensor Analysis**: Heart Rate, Stress Level (GSR), Motion Intensity, Motion Type
- **Intelligent Classification**: SAFE, WARNING, DANGER
- **Panic Detection**: Distinguishes panic from exercise/happiness
- **False Alarm Prevention**: Smart alert escalation with manual override

### 🎨 Premium UI/UX
- **Modern, Gradient-Based Design**: Professional color scheme
- **Responsive Layout**: Sidebar inputs, multi-column dashboard, insights panel
- **Real-Time Visualization**: Progress bars, status indicators, dynamic cards
- **Smooth Animations**: Hover effects, transitions, shadows

### 🧠 Advanced Algorithms
- **Weighted Risk Scoring** (0-100%):
  - Heart Rate: 35%
  - Stress Level: 30%
  - Motion Intensity: 20%
  - Motion Type: 15%
- **Context-Aware Panic Detection**: Avoids false positives during exercise
- **Comprehensive Analysis**: Sensor reasoning + actionable recommendations

### 🛡️ Professional Features
- **Clean Code Architecture**: Modular, well-documented, production-ready
- **Privacy-First Design**: All processing local, no external API calls
- **Expandable Technical Details**: Algorithm transparency for technical interviews
- **Emergency Protocol**: Simulated emergency response system

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# 1. Navigate to the project directory
cd /path/to/SheSafe_Demo

# 2. Create a virtual environment (optional but recommended)
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 📊 How It Works

### 1️⃣ **Sensor Input** (Sidebar)
Adjust real-time sensor values:
- ❤️ **Heart Rate** (60-160 bpm)
- 📊 **Stress Level** (0-1 GSR)
- 🏃 **Motion Intensity** (0-1)
- 🎯 **Motion Type** (Smooth / Chaotic)

### 2️⃣ **Real-Time Analysis** (Main Dashboard)
Instant multi-sensor fusion calculates:
- **Status**: SAFE ✅ | WARNING ⚠️ | DANGER 🚨
- **Risk Score**: 0-100% with color-coded indicators
- **Reasoning**: Detailed sensor analysis explanation
- **Action**: Context-specific recommendations

### 3️⃣ **Panic Detection**
Advanced algorithm identifies panic vs. normal activity:

| Pattern | Status |
|---------|--------|
| High HR + High Stress + Chaotic + Active | 🚨 PANIC |
| High HR + Low Stress + Smooth Motion | 🏃 Exercise (SAFE) |
| Normal Levels + Smooth Motion | ✅ NORMAL |

### 4️⃣ **Emergency Protocol** (for DANGER Status)
- **False Alarm Button**: "I'm Safe" → Prevents escalation
- **Emergency Button**: "Need Help" → Simulates emergency response

---

## 🧠 Algorithm Breakdown

### Risk Score Calculation

```
Risk Score = (HR_Risk × 0.35) + (Stress_Risk × 0.30) + 
             (Motion_Risk × 0.20) + (Motion_Type × 0.15)
```

**Classification Rules:**
- 🚨 **DANGER**: Risk > 70% OR Panic Detected
- ⚠️ **WARNING**: 40% < Risk ≤ 70%
- ✅ **SAFE**: Risk ≤ 40%

### Panic Detection Logic

**Triggers DANGER:**
```
(HR > 120 bpm) AND (Stress > 0.7) AND (Chaotic Motion) AND (Intensity > 0.7)
```

**Non-Panic High HR** (False Alarm Prevention):
```
(HR > 120 bpm) AND (Stress < 0.4) AND (Smooth Motion) = EXERCISE
```

---

## 🎨 Design Highlights

### Color Scheme
- **Green (#22c55e)**: SAFE ✅
- **Yellow (#eab308)**: WARNING ⚠️
- **Red (#ef4444)**: DANGER 🚨
- **Purple (#667eea)**: Accent/Header

### Component Features
- **Gradient Backgrounds**: Modern, professional look
- **Rounded Cards**: Soft, approachable UI
- **Smooth Shadows**: Depth and dimension
- **Responsive Layout**: Works on all screen sizes

### CSS Enhancements
```css
/* Key styling features */
- Border-radius: 12px (cards), 15px (header)
- Box-shadow: Multi-layer for depth
- Gradient backgrounds for visual appeal
- Hover effects for interactivity
- Smooth transitions (0.3s ease)
```

---

## 📁 Project Structure

```
SheSafe_Demo/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

### Code Organization (in app.py)

```python
1. Configuration & Styling
   - Streamlit page setup
   - Custom CSS injection

2. Enums & Data Classes
   - SafetyStatus enum
   - SensorReading dataclass
   - SafetyAnalysis dataclass

3. Logic & Analysis Engine
   - calculate_risk_score()
   - detect_panic_state()
   - classify_safety_status()
   - generate_reasoning()
   - analyze_safety()

4. UI Components
   - render_header()
   - render_status_card()
   - render_risk_score_card()
   - render_reasoning_card()
   - render_action_card()
   - render_insights_section()

5. Sidebar Controls
   - get_sensor_inputs()

6. Main Application
   - main()
```

---

## 💡 Interview-Ready Talking Points

### Engineering Excellence
- ✅ **Multi-Sensor Fusion**: Demonstrates system design thinking
- ✅ **Weighted Algorithms**: Shows mathematical reasoning
- ✅ **Modularity**: Clean separation of concerns
- ✅ **Error Prevention**: False alarm mitigation strategies

### UI/UX Design
- ✅ **Responsive Layout**: Professional dashboard design
- ✅ **Visual Hierarchy**: Clear information prioritization
- ✅ **Color Psychology**: Intuitive status indicators
- ✅ **Accessibility**: Clear labels and descriptions

### Real-World Applicability
- ✅ **Privacy First**: Local processing, no data transmission
- ✅ **Low Latency**: Instant analysis on user input
- ✅ **Scalability**: Algorithm works for different sensor types
- ✅ **User-Centric**: Emergency override for false alarms

---

## 🎯 Use Cases for Demos

### 1. **Showcase SAFE State**
```
HR: 72 bpm, Stress: 0.2, Motion: 0.1, Type: Smooth
→ Risk: 15% → SAFE
→ Shows baseline and system accuracy
```

### 2. **Show WARNING State**
```
HR: 110 bpm, Stress: 0.5, Motion: 0.6, Type: Chaotic
→ Risk: 48% → WARNING
→ Demonstrates mid-range classification
```

### 3. **Trigger DANGER + Panic Detection**
```
HR: 135 bpm, Stress: 0.8, Motion: 0.9, Type: Chaotic
→ Risk: 85% → DANGER
→ Panic Detected → Shows emergency protocol
```

### 4. **False Alarm Prevention (Exercise)**
```
HR: 140 bpm, Stress: 0.1, Motion: 0.8, Type: Smooth
→ Risk: 45% → WARNING (not DANGER!)
→ System recognizes exercise pattern
→ Shows AI understanding of context
```

---

## 🚀 Deployment Options

### Local Testing
```bash
streamlit run app.py
```

### Streamlit Cloud
```bash
# 1. Push to GitHub
git push origin main

# 2. Deploy on Streamlit Cloud
# Visit: https://share.streamlit.io
# Select your GitHub repo
```

### Docker
```bash
docker build -t shesafe .
docker run -p 8501:8501 shesafe
```

---

## 🔧 Customization

### Adjust Thresholds
Edit `classify_safety_status()` function:
```python
if is_panic or risk_score > 75:  # Change threshold
    return SafetyStatus.DANGER
```

### Modify Weights
Edit `calculate_risk_score()` function:
```python
# Change weight percentages
risk_score = (
    hr_risk * 0.40 +        # Increase HR importance
    stress_risk * 0.25 +    # Decrease stress importance
    ...
)
```

### Customize Colors
Edit the CSS section in `inject_custom_css()`:
```css
.header-container {
    background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
}
```

---

## 📚 Technical Stack

| Component | Technology |
|-----------|-----------|
| **Web Framework** | Streamlit 1.28.1 |
| **Language** | Python 3.8+ |
| **UI/UX** | HTML5 + CSS3 |
| **Architecture** | Modular, functional |
| **Data Processing** | NumPy-style computations |

---

## 🤝 Contributing

This is a demonstration project. For improvements or feedback:
1. Fork the repository
2. Create a feature branch
3. Submit pull requests

---

## 📄 License

MIT License – Use freely for educational and commercial purposes

---

## 🎓 Educational Value

This project demonstrates:
- ✅ Full-stack application development
- ✅ Algorithm design and implementation
- ✅ UI/UX best practices
- ✅ Professional code organization
- ✅ Real-world problem solving
- ✅ Safety-critical systems design

---

## 📞 Support

For questions or issues:
1. Check the expandable "Technical Details" section in the app
2. Review code comments in `app.py`
3. Consult the algorithm breakdown in this README

---

## 🌟 Highlights for Your Portfolio

```
✓ Production-grade UI with custom CSS
✓ Advanced multi-sensor fusion algorithm
✓ Panic detection with false alarm prevention
✓ Professional code architecture
✓ Full documentation and comments
✓ Interview-ready demo scenarios
✓ Startup-quality visual design
```

---

**Built with ❤️ for women's safety and AI engineering excellence**

**Version**: 1.0.0 | **Last Updated**: April 2026
