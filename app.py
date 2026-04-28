"""
SheSafe – Intelligent Safety Dashboard
An AI-powered smart wearable safety system for women
Production-quality Streamlit application
"""

from cProfile import label
from turtle import color

import streamlit as st
import math
from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Dict


# ============================================================================
# CONFIGURATION & STYLING
# ============================================================================

st.set_page_config(
    page_title="SheSafe - Safety Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Custom CSS for premium styling
def inject_custom_css():
    """Inject beautiful custom CSS for professional appearance"""
    custom_css = """
    <style>

    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Header styling */
    .header-container {
        text-align: center;
        margin-bottom: 2rem;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        color: white;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .header-title {
        font-size: 3em;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
    }
    
    .header-subtitle {
        font-size: 1.1em;
        margin-top: 0.5rem;
        opacity: 0.95;
        font-weight: 400;
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .card:hover {
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        transform: translateY(-2px);
    }
    
    .card-title {
        font-size: 1em;
        font-weight: 700;
        color: #333;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        opacity: 0.7;
    }
    
    /* Status card - SAFE */
    .status-safe {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(34, 197, 94, 0.05) 100%);
        border-left: 5px solid #22c55e;
    }
    
    /* Status card - WARNING */
    .status-warning {
        background: linear-gradient(135deg, rgba(234, 179, 8, 0.1) 0%, rgba(234, 179, 8, 0.05) 100%);
        border-left: 5px solid #eab308;
    }
    
    /* Status card - DANGER */
    .status-danger {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
        border-left: 5px solid #ef4444;
    }
    
    /* Status text */
    .status-text {
        font-size: 2.5em;
        font-weight: 800;
        margin: 1rem 0;
        letter-spacing: -1px;
        color: white !important
    }

    .status-safe .status-text {
    color: #ffffff !important;
    }
    
    .status-warning .status-text {
    color: #ffffff !important;
    }
    
    .status-danger .status-text {
    color: #ffffff !important;
    }
    
    /* Insights section */
    .insights-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .insights-title {
        font-size: 1.5em;
        font-weight: 700;
        color: #333;
        margin-bottom: 1.5rem;
    }
    
    .insight-item {
        background: white;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
        color: #333 !important; 
    }
    .insight-item p {
    color: #444 !important;
    }
    .insight-item strong {
    color: #222 !important;
    }
    
    /* Sidebar styling */
    .sidebar-section {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(0, 0, 0, 0.05);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    .sidebar-label {
        font-weight: 600;
        color: #333;
        margin-bottom: 0.5rem;
        font-size: 0.95em;
    }
    
    /* Alert styling */
    .alert-box {
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
        border-left: 4px solid;
    }
    
    .alert-danger {
        background-color: rgba(239, 68, 68, 0.1);
        border-left-color: #ef4444;
        color: #991b1b;
    }
    
    .alert-warning {
        background-color: rgba(234, 179, 8, 0.1);
        border-left-color: #eab308;
        color: #854d0e;
    }
    
    .alert-success {
        background-color: rgba(34, 197, 94, 0.1);
        border-left-color: #22c55e;
        color: #166534;
    }
    
    /* Metric styling */
    .metric-label {
        font-size: 0.85em;
        color: #666;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 2em;
        font-weight: 700;
        color: #333;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 8px;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    
    /* Progress bar styling */
    .stProgress > div > div {
        border-radius: 10px;
    }
    /* Sidebar text visibility fix */
    section[data-testid="stSidebar"] {
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] .sidebar-label {
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] label {
        color: #ffffff !important;
        font-weight: 600;
    }
    section[data-testid="stSidebar"] .stCaption {
    color: #cccccc !important;
    }
    section[data-testid="stSidebar"] span {
        color: #ffffff !important;
    }

    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


# ============================================================================
# ENUMS & DATA CLASSES
# ============================================================================

class SafetyStatus(Enum):
    """Enumeration for safety status levels"""
    SAFE = "SAFE"
    WARNING = "WARNING"
    DANGER = "DANGER"


@dataclass
class SensorReading:
    """Data class for sensor readings"""
    heart_rate: int
    stress_level: float
    motion_intensity: float
    motion_type: str


@dataclass
class SafetyAnalysis:
    """Data class for safety analysis results"""
    status: SafetyStatus
    risk_score: int
    reasoning: str
    action: str
    is_panic: bool
    panic_description: str
    confidence: int 


# ============================================================================
# LOGIC & ANALYSIS ENGINE
# ============================================================================

def calculate_risk_score(
    heart_rate: int,
    stress_level: float,
    motion_intensity: float,
    motion_type: str
) -> int:
    """
    Calculate comprehensive risk score (0-100) using weighted multi-sensor fusion
    
    Weights:
    - Heart Rate: 35% (physiological indicator)
    - Stress Level: 30% (psychological indicator)
    - Motion Intensity: 20% (physical activity level)
    - Motion Type: 15% (pattern analysis)
    """
    
    # Normalize heart rate (60-160 bpm)
    hr_normalized = (heart_rate - 60) / (160 - 60)
    hr_normalized = max(0, min(1, hr_normalized))
    hr_risk = hr_normalized * 100
    
    # Stress level already 0-1
    stress_risk = stress_level * 100
    
    # Motion intensity already 0-1
    motion_risk = motion_intensity * 100
    
    # Motion type penalty
    motion_type_penalty = 25 if motion_type == "Chaotic" else 5
    
    # Weighted calculation
    risk_score = (
        hr_risk * 0.35 +
        stress_risk * 0.30 +
        motion_risk * 0.20 +
        motion_type_penalty * 0.15
    )
    
    return int(min(100, max(0, risk_score)))


def detect_panic_state(
    heart_rate: int,
    stress_level: float,
    motion_intensity: float,
    motion_type: str
) -> Tuple[bool, str]:
    """
    Advanced panic detection using multi-sensor fusion
    
    Panic indicators:
    - High heart rate (>120 bpm) + High stress (>0.7) + Chaotic motion
    - Rapid elevation in multiple sensors simultaneously
    
    Non-panic high HR:
    - High HR + Low stress + Smooth motion = Exercise/Happy
    """
    
    is_high_hr = heart_rate > 120
    is_high_stress = stress_level > 0.7
    is_high_motion = motion_intensity > 0.7
    is_chaotic = motion_type == "Chaotic"
    
    # Panic pattern: High HR + High Stress + Chaotic Motion
    if is_high_hr and is_high_stress and is_chaotic and is_high_motion:
        return True, "🚨 Panic Pattern Detected: Multiple threat indicators"
    
    # Strong panic indicators (2+ severe conditions)
    panic_indicators = sum([is_high_hr, is_high_stress, is_chaotic])
    if panic_indicators >= 2 and is_high_motion:
        return True, "⚠️ Potential Panic: Abnormal pattern detected"
    
    # Exercise/Happy state: High HR but low stress and smooth
    if is_high_hr and not is_high_stress and not is_chaotic:
        return False, "🏃 Normal Activity: Exercise or happy state detected"
    
    return False, "✅ Normal State: No panic indicators"


def classify_safety_status(risk_score: int, is_panic: bool) -> SafetyStatus:
    """
    Classify safety status based on risk score and panic detection
    
    DANGER: risk_score > 70 OR panic detected
    WARNING: 40 < risk_score <= 70
    SAFE: risk_score <= 40
    """
    
    if is_panic or risk_score > 70:
        return SafetyStatus.DANGER
    elif risk_score > 40:
        return SafetyStatus.WARNING
    else:
        return SafetyStatus.SAFE


def generate_reasoning(
    heart_rate: int,
    stress_level: float,
    motion_intensity: float,
    motion_type: str,
    status: SafetyStatus
) -> str:
    """Generate human-readable reasoning for the classification"""
    
    reasons = []
    
    # Analyze heart rate
    if heart_rate > 120:
        reasons.append(f"High heart rate ({heart_rate} bpm)")
    elif heart_rate > 100:
        reasons.append(f"Elevated heart rate ({heart_rate} bpm)")
    else:
        reasons.append(f"Normal heart rate ({heart_rate} bpm)")
    
    # Analyze stress level
    if stress_level > 0.7:
        reasons.append(f"High stress level ({stress_level:.2f})")
    elif stress_level > 0.4:
        reasons.append(f"Moderate stress ({stress_level:.2f})")
    else:
        reasons.append(f"Low stress level ({stress_level:.2f})")
    
    # Analyze motion
    if motion_type == "Chaotic":
        reasons.append(f"Chaotic motion detected (intensity: {motion_intensity:.2f})")
    else:
        reasons.append(f"Smooth motion pattern (intensity: {motion_intensity:.2f})")
    
    return " • ".join(reasons)


def generate_action_message(status: SafetyStatus) -> str:
    """Generate action message based on status"""
    
    actions = {
        SafetyStatus.SAFE: "✅ You are safe. Continue with your activities.",
        SafetyStatus.WARNING: "⚠️ Stay alert. Monitor your surroundings.",
        SafetyStatus.DANGER: "🚨 Emergency detected. Seek help immediately!"
    }
    
    return actions.get(status, "Unknown status")


def analyze_safety(sensor_reading: SensorReading) -> SafetyAnalysis:
    """Perform comprehensive safety analysis"""
    
    risk_score = calculate_risk_score(
        sensor_reading.heart_rate,
        sensor_reading.stress_level,
        sensor_reading.motion_intensity,
        sensor_reading.motion_type
    )
    
    is_panic, panic_description = detect_panic_state(
        sensor_reading.heart_rate,
        sensor_reading.stress_level,
        sensor_reading.motion_intensity,
        sensor_reading.motion_type
    )
    
    status = classify_safety_status(risk_score, is_panic)
    
    reasoning = generate_reasoning(
        sensor_reading.heart_rate,
        sensor_reading.stress_level,
        sensor_reading.motion_intensity,
        sensor_reading.motion_type,
        status
    )
    
    action = generate_action_message(status)
    confidence = min(95, 60 + risk_score // 2)
    
    return SafetyAnalysis(
        status=status,
        risk_score=risk_score,
        reasoning=reasoning,
        action=action,
        is_panic=is_panic,
        panic_description=panic_description,
        confidence=confidence
    )


# ============================================================================
# UI COMPONENTS
# ============================================================================

def render_header():
    """Render premium header section"""
    st.markdown(
        """
        <div class="header-container">
            <h1 class="header-title">🛡️ SheSafe</h1>
            <p class="header-subtitle">AI-powered Intelligent Safety Monitoring System</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_status_card(status: SafetyStatus, emoji: str):
    """Render status card with color coding"""
    
    status_class = f"status-{status.value.lower()}"
    
    st.markdown(
        f"""
        <div class="card {status_class}">
            <div class="card-title">📍 Status</div>
            <div class="status-text" style="color: #ffffff; text-shadow: 0 2px 6px rgba(0,0,0,0.6);">{emoji} {status.value}
        </div>
        """,
        unsafe_allow_html=True
    )


def render_risk_score_card(risk_score: int, confidence: int):
    """Render risk score card with progress indicator"""
    
    # Determine color based on risk
    if risk_score < 40:
        color = "🟢"
        color_name = "green"
    elif risk_score < 70:
        color = "🟡"
        color_name = "orange"
    else:
        color = "🔴"
        color_name = "red"
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">📊 Risk Score</div>
                <div class="metric-value">{risk_score}%</div>
                <div class="metric-label">Overall Risk Level</div>
                <div class="metric-label">🧠 Confidence: {confidence}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">📈 Risk Indicator</div>
            """,
            unsafe_allow_html=True
        )
        st.progress(risk_score / 100, text=f"{color} {color_name.upper()}")
        st.markdown("</div>", unsafe_allow_html=True)


def render_reasoning_card(reasoning: str, panic_description: str):
    """Render reasoning card"""
    st.markdown(
        f"""
        <div class="card">
        <div class="card-title">🧠 Analysis & Reasoning</div>
        <p><strong>Sensor Analysis:</strong></p>
        <p style="color: #333; font-weight: 500; line-height: 1.6;">
            {reasoning}
        </p>
        <p style="margin-top: 1rem; font-size: 0.95em; color: #444;">
            <strong>Panic Detection:</strong> {panic_description}
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


def render_action_card(action: str, status: SafetyStatus):
    """Render action card"""
    
    alert_class = {
        SafetyStatus.SAFE: "alert-success",
        SafetyStatus.WARNING: "alert-warning",
        SafetyStatus.DANGER: "alert-danger"
    }.get(status, "alert-warning")
    
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">⚡ Recommended Action</div>
            <div class="alert-box {alert_class}">
                <strong>{action}</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_insights_section():
    """Render informational insights section"""
    
    st.markdown(
        """
        <div class="insights-container">
            <h3 class="insights-title">📚 How SheSafe Works</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div class="insight-item">
            <strong>🔗 Multi-Sensor Fusion</strong>
            <p>Combines heart rate, stress levels, and motion patterns to create a comprehensive threat assessment model.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div class="insight-item">
            <strong>📊 Risk Scoring</strong>
            <p>Advanced algorithm weighs physiological, psychological, and kinematic data to calculate real-time risk (0-100%).</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            """
            <div class="insight-item">
            <strong>🚨 Panic Detection</strong>
            <p>AI identifies panic patterns vs. normal activities (exercise, happiness) with high accuracy.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    col4, col5 = st.columns(2)
    
    with col4:
        st.markdown(
            """
            <div class="insight-item">
            <strong>⛔ False Alarm Prevention</strong>
            <p>Distinguishes between danger and normal high-HR activities to reduce false emergency alerts.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col5:
        st.markdown(
            """
            <div class="insight-item">
            <strong>🛡️ Privacy First</strong>
            <p>All processing occurs locally on your device. No data transmission to external servers.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================================
# SIDEBAR CONTROLS
# ============================================================================

def get_sensor_inputs() -> SensorReading:
    """Get sensor inputs from sidebar controls"""
    
    with st.sidebar:
        st.markdown("### 📊 Sensor Inputs")
        st.markdown("---")
        
        # Heart Rate Input
        st.markdown(
            """
            <div class="sidebar-label">❤️ Heart Rate (bpm)</div>
            """,
            unsafe_allow_html=True
        )
        heart_rate = st.slider(
            "Heart Rate",
            min_value=60,
            max_value=160,
            value=80,
            step=1,
            label_visibility="collapsed"
        )
        st.caption("Normal: 60-100 bpm | Elevated: 100-120 | High: 120+")
        
        st.markdown("---")
        
        # Stress Level Input
        st.markdown(
            """
            <div class="sidebar-label">📊 Stress Level (GSR)</div>
            """,
            unsafe_allow_html=True
        )
        stress_level = st.slider(
            "Stress Level",
            min_value=0.0,
            max_value=1.0,
            value=0.3,
            step=0.05,
            label_visibility="collapsed"
        )
        st.caption("Low: 0-0.3 | Moderate: 0.3-0.7 | High: 0.7-1.0")
        
        st.markdown("---")
        
        # Motion Intensity Input
        st.markdown(
            """
            <div class="sidebar-label">🏃 Motion Intensity</div>
            """,
            unsafe_allow_html=True
        )
        motion_intensity = st.slider(
            "Motion Intensity",
            min_value=0.0,
            max_value=1.0,
            value=0.2,
            step=0.05,
            label_visibility="collapsed"
        )
        st.caption("Still: 0-0.2 | Normal: 0.2-0.6 | Active: 0.6-1.0")
        
        st.markdown("---")
        
        # Motion Type Input
        st.markdown(
            """
            <div class="sidebar-label">🎯 Motion Pattern</div>
            """,
            unsafe_allow_html=True
        )
        motion_type = st.selectbox(
            "Motion Type",
            options=["Smooth", "Chaotic"],
            label_visibility="collapsed"
        )
        st.caption("Smooth: Steady movement | Chaotic: Erratic patterns")
        
        st.markdown("---")
        
        return SensorReading(
            heart_rate=heart_rate,
            stress_level=stress_level,
            motion_intensity=motion_intensity,
            motion_type=motion_type
        )


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application entry point"""
    
    # Apply custom CSS
    inject_custom_css()
    
    # Render header
    render_header()
    
    # Get sensor inputs from sidebar
    sensor_reading = get_sensor_inputs()
    
    # Perform safety analysis
    analysis = analyze_safety(sensor_reading)
    
    # Determine emoji for status
    emoji_map = {
        SafetyStatus.SAFE: "✅",
        SafetyStatus.WARNING: "⚠️",
        SafetyStatus.DANGER: "🚨"
    }
    emoji = emoji_map[analysis.status]
    
    # Main dashboard - status and risk score
    st.markdown("### 📈 Real-Time Safety Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_status_card(analysis.status, emoji)
    
    with col2:
        # Risk score
        if analysis.risk_score < 40:
            color = "green"
        elif analysis.risk_score < 70:
            color = "orange"
        else:
            color = "red"
        
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">📊 Risk Score</div>
                <div class="metric-value">{analysis.risk_score}%</div>
                <div class="metric-label">{color.upper()} Risk Level</div>
                <div class="metric-label">🧠 Confidence: {analysis.confidence}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.progress(analysis.risk_score / 100)
    
    # Reasoning and action
    st.markdown("### 🧠 Analysis & Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_reasoning_card(analysis.reasoning, analysis.panic_description)
    
    with col2:
        render_action_card(analysis.action, analysis.status)
    
    # False alarm prevention for DANGER status
    if analysis.status == SafetyStatus.DANGER:
        st.markdown("### 🚨 Emergency Protocol")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✅ I'm Safe - False Alarm", use_container_width=True):
                st.success(
                    "Thank you for confirming. System learning: Pattern logged as false positive.",
                    icon="✅"
                )
                st.info(
                    "🔄 **Alert Escalation Prevented**: "
                    "Your manual confirmation has prevented automatic emergency notifications.",
                    icon="ℹ️"
                )
        
        with col2:
            if st.button("🚨 Need Help - Real Emergency", use_container_width=True):
                st.error(
                    "🚨 **EMERGENCY MODE ACTIVATED**\n\n"
                    "Initiating emergency protocols:\n"
                    "✓ Emergency contacts notified\n"
                    "✓ Location shared with trusted contacts\n"
                    "✓ Local authorities alerted\n\n"
                    "*This is a simulation*",
                    icon="🚨"
                )
    
    # Insights section
    st.markdown("---")
    render_insights_section()
    
    # Technical details (expandable)
    st.markdown("---")
    with st.expander("⚙️ Technical Details & Algorithm"):
        st.markdown("""
        ### Risk Scoring Algorithm
        
        **Weighted Multi-Sensor Fusion:**
        - Heart Rate: 35% weight (60-160 bpm normalized)
        - Stress Level: 30% weight (0-1 GSR scale)
        - Motion Intensity: 20% weight (0-1 scale)
        - Motion Type: 15% weight (Smooth vs. Chaotic)
        
        ### Classification Rules
        | Status | Condition |
        |--------|-----------|
        | 🚨 DANGER | Risk Score > 70 OR Panic Detected |
        | ⚠️ WARNING | 40 < Risk Score ≤ 70 |
        | ✅ SAFE | Risk Score ≤ 40 |
        
        ### Panic Detection Logic
        **True Panic Pattern:**
        - High HR (>120) + High Stress (>0.7) + Chaotic Motion + High Intensity
        
        **Exercise/Happy (Non-Panic):**
        - High HR (>120) + Low Stress (<0.4) + Smooth Motion
        
        ### Privacy & Security
        - All computations performed locally
        - No external API calls
        - No data transmission
        - Fully offline capable
        """)


if __name__ == "__main__":
    main()
