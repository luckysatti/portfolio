import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Sathi Lakshmi Narayana Reddy | Portfolio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for stunning design with navigation
st.markdown("""
<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap');

/* Global Styles */
* {
    font-family: 'Inter', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Smooth Scrolling */
html {
    scroll-behavior: smooth;
}

/* Animated Background */
.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 25%, #16213e 50%, #0f1f3d 75%, #0a0e27 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    background-attachment: fixed;
    position: relative;
    overflow-x: hidden;
}

/* Background mesh pattern overlay */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
        radial-gradient(circle at 20% 30%, rgba(0, 212, 255, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 80% 70%, rgba(138, 43, 226, 0.06) 0%, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(0, 255, 157, 0.04) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Fixed Navigation Bar */
.nav-bar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: rgba(10, 14, 39, 0.85);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    padding: 16px 50px;
    z-index: 1000;
    border-bottom: 1px solid rgba(0, 212, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), 0 0 80px rgba(0, 212, 255, 0.1);
    transition: all 0.3s ease;
}

.nav-container {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    align-items: center;
}

.nav-logo {
    font-size: 1.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00d4ff 0%, #00ff9d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 0.5px;
    white-space: nowrap;
    flex-shrink: 0;
    font-family: 'Space Grotesk', sans-serif;
    text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
}

.nav-links {
    display: flex;
    gap: 8px;
    margin-left: auto;
    align-items: center;
}

.nav-link {
    color: #e0e0e0;
    text-decoration: none;
    font-size: 0.95rem;
    font-weight: 600;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.nav-link::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

.nav-link:hover::before {
    left: 100%;
}

.nav-link:hover {
    color: #00d4ff;
    background: rgba(0, 212, 255, 0.15);
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
    transform: translateY(-2px);
}

/* Main Content Spacing */
.main-content {
    margin-top: 0px;
    padding: 0 50px;
    position: relative;
    z-index: 1;
}

/* Section Spacing */
.section {
    padding: 80px 0;
    max-width: 1400px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

/* Hero Section */
.hero-section {
    min-height: auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
    padding: 40px 20px;
}

.hero-image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

.hero-image-container::before {
    content: '';
    position: absolute;
    width: 450px;
    height: 450px;
    background: radial-gradient(circle, rgba(0, 212, 255, 0.3) 0%, transparent 70%);
    border-radius: 50%;
    animation: pulse 3s ease-in-out infinite;
    z-index: -1;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.1); opacity: 0.8; }
}

.hero-image {
    width: 380px;
    height: 380px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid transparent;
    background: linear-gradient(#0a0e27, #0a0e27) padding-box,
                linear-gradient(135deg, #00d4ff, #00ff9d, #8a2be2) border-box;
    box-shadow: 
        0 20px 60px rgba(0, 212, 255, 0.4),
        0 0 80px rgba(0, 212, 255, 0.2),
        inset 0 0 20px rgba(0, 212, 255, 0.1);
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.hero-image:hover {
    transform: scale(1.05) rotate(2deg);
    box-shadow: 
        0 30px 90px rgba(0, 212, 255, 0.6),
        0 0 120px rgba(0, 212, 255, 0.4),
        inset 0 0 30px rgba(0, 212, 255, 0.2);
}

.hero-content {
    text-align: left;
}

@media (max-width: 968px) {
    .hero-section {
        grid-template-columns: 1fr;
        text-align: center;
    }
    .hero-content {
        text-align: center;
    }
}

.hero-title {
    font-size: 4.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #ffffff 0%, #e0e0e0 50%, #00d4ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 16px;
    letter-spacing: -2px;
    animation: fadeInDown 1s ease;
    font-family: 'Space Grotesk', sans-serif;
    line-height: 1.1;
}

.hero-subtitle {
    font-size: 1.8rem;
    background: linear-gradient(135deg, #00d4ff 0%, #00ff9d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 20px;
    font-weight: 700;
    animation: fadeInUp 1s ease;
    font-family: 'Space Grotesk', sans-serif;
}

.hero-description {
    font-size: 1.15rem;
    color: #c0c0c0;
    max-width: 800px;
    margin: 0 auto 40px;
    line-height: 1.8;
    font-weight: 400;
}

/* CTA Buttons */
.cta-container {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 30px;
}

.cta-button {
    display: inline-block;
    padding: 14px 32px;
    background: transparent;
    color: #00d4ff;
    text-decoration: none;
    border: 2px solid #00d4ff;
    border-radius: 10px;
    font-weight: 700;
    font-size: 0.95rem;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    font-family: 'Space Grotesk', sans-serif;
}

.cta-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.3), transparent);
    transition: left 0.6s ease;
}

.cta-button:hover::before {
    left: 100%;
}

.cta-button:hover {
    background: #00d4ff;
    color: #0a0e27;
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 12px 40px rgba(0, 212, 255, 0.5), 0 0 60px rgba(0, 212, 255, 0.3);
    border-color: #00d4ff;
}

.cta-button-primary {
    background: linear-gradient(135deg, #00d4ff 0%, #00ff9d 100%);
    color: #0a0e27;
    border: 2px solid transparent;
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
}

.cta-button-primary:hover {
    background: linear-gradient(135deg, #00ff9d 0%, #00d4ff 100%);
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 15px 50px rgba(0, 212, 255, 0.6);
}

/* Section Heading */
.section-heading {
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 0%, #00d4ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 60px;
    text-align: center;
    position: relative;
    padding-bottom: 25px;
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: -1px;
}

.section-heading::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 5px;
    background: linear-gradient(90deg, transparent, #00d4ff, #00ff9d, transparent);
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.6);
}

/* Stats Cards */
.stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 25px;
    margin: 60px 0;
}

.stat-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(0, 212, 255, 0.2);
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.stat-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(0, 212, 255, 0.1) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.stat-card:hover::before {
    opacity: 1;
}

.stat-card:hover {
    transform: translateY(-12px) scale(1.02);
    border-color: #00d4ff;
    box-shadow: 
        0 20px 60px rgba(0, 212, 255, 0.3),
        0 0 80px rgba(0, 212, 255, 0.2),
        inset 0 0 30px rgba(0, 212, 255, 0.05);
    background: rgba(255, 255, 255, 0.05);
}

.stat-number {
    font-size: 3.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #00d4ff 0%, #00ff9d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 12px;
    line-height: 1;
    font-family: 'Space Grotesk', sans-serif;
}

.stat-label {
    font-size: 1.05rem;
    color: #c0c0c0;
    font-weight: 600;
    letter-spacing: 0.5px;
}

/* Content Cards */
.content-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(0, 212, 255, 0.15);
    border-radius: 20px;
    padding: 40px;
    margin-bottom: 30px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.content-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.05), transparent);
    transition: left 0.6s ease;
}

.content-card:hover::before {
    left: 100%;
}

.content-card:hover {
    transform: translateY(-8px) scale(1.01);
    border-color: #00d4ff;
    box-shadow: 
        0 20px 60px rgba(0, 212, 255, 0.25),
        0 0 80px rgba(0, 212, 255, 0.15),
        inset 0 0 30px rgba(0, 212, 255, 0.05);
    background: rgba(255, 255, 255, 0.05);
}

.card-title {
    font-size: 1.9rem;
    background: linear-gradient(135deg, #00d4ff 0%, #00ff9d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 800;
    margin-bottom: 14px;
    font-family: 'Space Grotesk', sans-serif;
}

.card-subtitle {
    font-size: 1.35rem;
    color: #e0e0e0;
    margin-bottom: 10px;
    font-weight: 700;
}

.card-date {
    font-size: 1rem;
    color: #909090;
    margin-bottom: 22px;
    font-weight: 500;
}

.card-description {
    color: #c0c0c0;
    line-height: 1.9;
    font-size: 1.05rem;
    font-weight: 400;
}

/* Lists */
ul {
    color: #c0c0c0;
    line-height: 2;
    padding-left: 24px;
}

li {
    margin-bottom: 12px;
    position: relative;
    padding-left: 8px;
}

li::marker {
    color: #00d4ff;
}

/* Skills Section */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 25px;
    margin-top: 40px;
}

.skill-category {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(0, 212, 255, 0.15);
    border-radius: 18px;
    padding: 30px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.skill-category::before {
    content: '';
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: linear-gradient(135deg, #00d4ff, #00ff9d, #8a2be2);
    border-radius: 18px;
    opacity: 0;
    z-index: -1;
    transition: opacity 0.4s ease;
}

.skill-category:hover::before {
    opacity: 0.3;
}

.skill-category:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 
        0 15px 50px rgba(0, 212, 255, 0.3),
        0 0 60px rgba(0, 212, 255, 0.2);
    background: rgba(255, 255, 255, 0.05);
}

.skill-category-title {
    font-size: 1.4rem;
    background: linear-gradient(135deg, #00d4ff 0%, #00ff9d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 700;
    margin-bottom: 18px;
    font-family: 'Space Grotesk', sans-serif;
}

.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}

.skill-tag {
    background: rgba(0, 212, 255, 0.12);
    color: #00d4ff;
    padding: 10px 18px;
    border-radius: 10px;
    font-size: 0.95rem;
    font-weight: 600;
    border: 1px solid rgba(0, 212, 255, 0.3);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: default;
}

.skill-tag:hover {
    background: rgba(0, 212, 255, 0.25);
    border-color: #00d4ff;
    transform: translateY(-3px) scale(1.08);
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.4);
}

/* Projects Grid */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

/* Contact Section */
.contact-container {
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

.contact-info {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(0, 212, 255, 0.2);
    border-radius: 25px;
    padding: 60px;
    margin-top: 40px;
    box-shadow: 0 20px 60px rgba(0, 212, 255, 0.15);
    transition: all 0.4s ease;
}

.contact-info:hover {
    border-color: #00d4ff;
    box-shadow: 0 25px 80px rgba(0, 212, 255, 0.25);
    transform: translateY(-5px);
}

.contact-links {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    margin: 35px 0;
}

.contact-link {
    display: inline-block;
    padding: 14px 32px;
    background: transparent;
    color: #00d4ff;
    text-decoration: none;
    border: 2px solid #00d4ff;
    border-radius: 10px;
    font-weight: 700;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    font-family: 'Space Grotesk', sans-serif;
    position: relative;
    overflow: hidden;
}

.contact-link::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    background: #00d4ff;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    transition: width 0.5s ease, height 0.5s ease;
    z-index: -1;
}

.contact-link:hover::before {
    width: 300px;
    height: 300px;
}

.contact-link:hover {
    color: #0a0e27;
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 12px 40px rgba(0, 212, 255, 0.5);
}

/* Certifications */
.cert-item {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border-left: 5px solid #00d4ff;
    border-top: 1px solid rgba(0, 212, 255, 0.15);
    border-right: 1px solid rgba(0, 212, 255, 0.15);
    border-bottom: 1px solid rgba(0, 212, 255, 0.15);
    padding: 25px 30px;
    margin-bottom: 20px;
    border-radius: 12px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.cert-item::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 5px;
    background: linear-gradient(180deg, #00d4ff, #00ff9d);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.cert-item:hover::before {
    opacity: 1;
}

.cert-item:hover {
    background: rgba(255, 255, 255, 0.05);
    transform: translateX(12px) scale(1.01);
    box-shadow: 0 10px 40px rgba(0, 212, 255, 0.2);
    border-left-width: 5px;
}

.cert-name {
    font-size: 1.25rem;
    color: #e0e0e0;
    font-weight: 700;
    margin-bottom: 8px;
}

.cert-year {
    display: inline-block;
    background: linear-gradient(135deg, #00d4ff 0%, #00ff9d 100%);
    color: #0a0e27;
    padding: 6px 16px;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 800;
    margin-top: 8px;
    box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
    font-family: 'Space Grotesk', sans-serif;
}

.main .block-container { 
    padding-top: 0px; 
}

.main-content { 
    margin-top: 0px; 
}

.hero-section { 
    padding: 40px 20px; 
}

/* Achievements */
.achievement-item {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.12) 0%, rgba(0, 212, 255, 0.06) 100%);
    border: 1px solid rgba(0, 212, 255, 0.3);
    padding: 30px 35px;
    border-radius: 15px;
    margin-bottom: 20px;
    color: #e0e0e0;
    font-size: 1.15rem;
    font-weight: 600;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.achievement-item::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(0, 212, 255, 0.15) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.4s ease, transform 0.4s ease;
}

.achievement-item:hover::before {
    opacity: 1;
    transform: scale(1.1);
}

.achievement-item:hover {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.2) 0%, rgba(0, 212, 255, 0.1) 100%);
    transform: scale(1.03);
    box-shadow: 0 15px 50px rgba(0, 212, 255, 0.3);
    border-color: #00d4ff;
}

/* Animations */
@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Footer */
.footer {
    text-align: center;
    padding: 50px 20px;
    color: #909090;
    border-top: 1px solid rgba(0, 212, 255, 0.2);
    margin-top: 100px;
    font-weight: 500;
}

/* Responsive Design */
@media (max-width: 768px) {
    .nav-bar {
        padding: 12px 20px;
    }
    
    .nav-links {
        gap: 4px;
    }
    
    .nav-link {
        padding: 8px 12px;
        font-size: 0.85rem;
    }
    
    .hero-title {
        font-size: 2.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
    }
    
    .section-heading {
        font-size: 2.5rem;
    }
    
    .main-content {
        padding: 0 20px;
    }
    
    .content-card {
        padding: 25px;
    }
}
</style>

<script>
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        const yOffset = -100;
        const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({top: y, behavior: 'smooth'});
    }
}
</script>

""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<style>
/* Reduce page top padding */
.main .block-container { padding-top: 0rem; }

/* Slim header */
.header-wrap { padding: 6px 0; margin: 0 0 6px 0; }

/* Tight typography */
.header-title { font-size: 24px; line-height: 1.1; margin: 0; }
.header-subtitle { font-size: 14px; line-height: 1.2; margin: 2px 0 0 0; }

/* Headings default margin trim */
h1, h2, h3 { margin-top: 0.4rem; margin-bottom: 0.4rem; }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="nav-bar">
    <div class="nav-container">
        <div class="nav-logo">Sathi Lakshmi Narayana Reddy</div>
        <div class="nav-links">
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#about" onclick="scrollToSection('about'); return false;">About</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#education" onclick="scrollToSection('education'); return false;">Education</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#experience" onclick="scrollToSection('experience'); return false;">Experience</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#projects" onclick="scrollToSection('projects'); return false;">Projects</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#skills" onclick="scrollToSection('skills'); return false;">Skills</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#certifications" onclick="scrollToSection('certifications'); return false;">Certifications</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#contact" onclick="scrollToSection('contact'); return false;">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
  /* 1) Make nav a bit shorter */
  .nav-bar { padding: 12px 32px; }         /* was 20px 50px */

  /* 2) Remove extra offset under fixed nav */
  .main-content { margin-top: 0px; }      /* was 100px; adjust to your nav height */

  /* 3) Make hero section compact */
  .hero-section { 
    min-height: auto;                      /* was 90vh */
    padding: 10px 16px;                    /* was 100px 20px */
    gap: 36px;                             /* was 60px */
  }

  /* 4) Tighten headline block */
  .hero-title { font-size: 3.2rem; margin-bottom: 8px; }   /* was 5rem and 20px */
  .hero-subtitle { font-size: 1.2rem; margin-bottom: 8px; }
  .hero-description { margin: 6px 0 16px; }

  /* 5) Slightly smaller image so row height is smaller */
  .hero-image { width: 20px; height: 25px; }             /* was 400x400 */
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div id="about" class="main-content">
  <section class="hero-section">
    <div class="hero-image-container">
      <img src="https://github.com/luckysatti/photo/blob/main/IMG_20250909_193640.png" class="zoom-image"alt="Sathi Lakshmi Narayana Reddy" class="hero-image">
    </div>
    <div class="hero-content">
      <h1 class="hero-title">Sathi Lakshmi Narayana Reddy</h1>
      <p class="hero-subtitle"> Full Stack Developer | Software Engineer | Problem Solver </p>
      <p class="hero-description">
         Strongly skilled in Python, Java, DSA and SQL, along with experience in GUI/web development using HTML, CSS, and
 JavaScript. Hands-on exposure to building applications involving user interface design, database integration, and system
 simulations. Quick learner with problem-solving skills, adaptability, and teamwork abilities.
      </p>
    </div>
    
  </section>
</div>
""", unsafe_allow_html=True)


# Stats

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""<div style="align:center" class="cta-container" style="justify-content: flex-start;">
        <a style="text-decoration:none" href="#contact" onclick="scrollToSection('contact'); return false;" class="cta-button">Get In Touch</a>
        <a style="text-decoration:none" href="https://drive.google.com/file/d/1fIFsWWEp7RFNmpUcVpPkSmyk8lvAfGad/view?usp=drive_link" target="_blank" class="cta-button">Check Out My Resume</a>
        <a style="text-decoration:none" href="https://github.com/ShariyaShaik" target="_blank" class="cta-button">View GitHub</a>
        <a style="text-decoration:none" href="https://www.linkedin.com/in/shariya-shaik-13677a268/" target="_blank" class="cta-button">LinkedIn Profile</a>
      </div>""",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <a style="text-decoration:none" href="https://drive.google.com/file/d/1jgRHNDqvfLdwMZeL8kt8XD6Un8Ov0zyP/view?usp=sharing">
    <div class="stat-card">
        <div class="stat-number">9.45</div>
        <div class="stat-label">CGPA</div>
    </div></a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a style="text-decoration:none" href="https://leetcode.com/u/luckysatti1045/"><div class="stat-card">
        <div class="stat-number">210+</div>
        <div class="stat-label">LeetCode Problems</div>
    </div></a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a style="text-decoration:none" href="#certifications" onclick="scrollToSection('certifications'); return false;">
        <div class="stat-card">
            <div class="stat-number">5+</div>
            <div class="stat-label">Certifications</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a style="text-decoration:none" href="https://www.hackerrank.com/profile/luckysatti1045">
    <div class="stat-card">
        <div class="stat-number"style="font-size: 2rem;">Hackerrank</div>
        <div class="stat-label">5★ in Python</div>
        <div class="stat-label">4★ in Java</div>
        <div class="stat-label">4★ in SQL</div>
    </div>
    </a>
    """, unsafe_allow_html=True)




# Education Section
st.markdown('<div id="education" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Education</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="content-card">
    <h3 class="card-title">B.Tech in Artificial Intelligence and Machine Learning</h3>
    <p class="card-subtitle">Mohan Babu University, Tirupati</p>
    <p class="card-date">2022 - 2026</p>
    <p class="card-description" style="color: #00d4ff; font-size: 1.3rem; font-weight: 700; margin-top: 15px;">
        CGPA: 9.45/10
    </p>
</div>
<div class="content-card">
    <h3 class="card-title">Intermediate in MPC</h3>
    <p class="card-subtitle">Sri Chaitanya Junior College, Eluru</p>
    <p class="card-date">2020 - 2022</p>
    <p class="card-description" style="color: #00d4ff; font-size: 1.3rem; font-weight: 700; margin-top: 15px;">
        Marks: 916/1000
    </p>
</div>
""", unsafe_allow_html=True)


# Professional Experience Section
st.markdown('<div id="experience" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Experience</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="content-card">
    <h3 class="card-title">Java Full Stack Developer Intern</h3>
    <p class="card-subtitle">NETWORX</p>
    <p class="card-date">June 2025 - August 2025</p>
    <div class="card-description">
        <ul>
            <li>Developed Banking System Simulator using Java (OOP + DSA) and Spring Boot</li>
            <li>Integrated JDBC and SQLite3 for efficient data storage and manipulation</li>
            <li>Designed front-end interface using HTML and CSS</li>
            <li>Enhanced skills in JDBC and database handling</li>
        </ul>
        <a href="https://drive.google.com/file/d/1QM-kSE_ufTKhHvIS2QcFOltwEZ7BC_Cc/view" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 10px; display: inline-block;">View Certificate →</a>
    </div>
</div>
<div class="content-card">
    <h3 class="card-title">AIML Intern</h3>
    <p class="card-subtitle">AICTE (Eduskills)</p>
    <p class="card-date">October 2024 - December 2024</p>
    <div class="card-description">
        <ul>
            <li>Experimented with ML models and learned model training based on specific requirements</li>
            <li>Gained practical experience in developing machine learning models</li>
            <li>Enhanced skills in model evaluation, data pre-processing, and deployment strategies</li>
        </ul>
        <a href="https://drive.google.com/file/d/1RsvlfH8mgGtt3jA5hAx_EXX49YcaxABG/view" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 10px; display: inline-block;">View Certificate →</a>
    </div>
</div>


""", unsafe_allow_html=True)


# Projects Section
st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Projects</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="content-card">
        <h3 class="card-title">Banking System Simulator</h3>
        <p class="card-description">
            Comprehensive banking application built with Java, Spring Boot, and database integration for managing financial operations.
        </p>
        <p style="color: #e0e0e0; font-weight: 600; margin: 20px 0 10px 0;">Key Features:</p>
        <ul>
            <li>Object-oriented programming with Java (OOP + DSA)</li>
            <li>Clean and responsive front-end using HTML and CSS</li>
            <li>JDBC and SQLite3 integration for data persistence</li>
            <li>Complete banking operations management</li>
        </ul>
        <div style="margin-top: 20px;">
            <span class="skill-tag">Java</span>
            <span class="skill-tag">Spring Boot</span>
            <span class="skill-tag">JDBC</span>
            <span class="skill-tag">SQLite3</span>
        </div>
        <a href="https://github.com/luckysatti/Banking-System" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 15px; display: inline-block;">View on GitHub →</a>
    </div>
     <div class="content-card">
        <h3 class="card-title">Electricity Bill Management System</h3>
        <p class="card-description">
            ServiceNow-based system for managing electricity bill operations with AI-powered virtual agent.
        </p>
        <p style="color: #e0e0e0; font-weight: 600; margin: 20px 0 10px 0;">Key Features:</p>
        <ul>
            <li>Consumer and bill details management</li>
            <li>Receipt generation and tracking</li>
            <li>Virtual agent integration for seamless interaction</li>
        </ul>
        <div style="margin-top: 20px;">
            <span class="skill-tag">ServiceNow</span>
            <span class="skill-tag">Virtual Agent</span>
            <span class="skill-tag">Integration</span>
        </div>
        <a href="https://www.linkedin.com/posts/sathi-lakshmi-narayana-reddy-b05ab6284_servicenow-learningbydoing-servicenowdeveloper-activity-7370362503954022400--CMW?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEU34bUBnfFrkkibKaBaNCjQKmkWr3IGqRk" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 15px; display: inline-block;">View on LinkedIn →</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""    
    <div class="content-card">
        <h3 class="card-title">Fantasy Cricket Application</h3>
        <p class="card-description">
            GUI-based desktop application for cricket enthusiasts to create and manage fantasy teams.
        </p>
        <p style="color: #e0e0e0; font-weight: 600; margin: 20px 0 10px 0;">Key Features:</p>
        <ul>
            <li>Interactive team creation interface</li>
            <li>Player addition/removal functionality</li>
            <li>Automated score calculation based on player performance</li>
            <li>SQL database for persistent data storage</li>
        </ul>
        <div style="margin-top: 20px;">
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Qt Designer</span>
            <span class="skill-tag">SQL</span>
        </div>
        <a href="https://www.linkedin.com/posts/sathi-lakshmi-narayana-reddy-b05ab6284_excited-to-share-my-latest-project-activity-7211786994459271168-Ejiz?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEU34bUBnfFrkkibKaBaNCjQKmkWr3IGqRk" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 15px; display: inline-block;">View on LinkedIn →</a>
    </div>
    """, unsafe_allow_html=True)


# Skills Section
st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Technical Skills</h2>', unsafe_allow_html=True)

skills_data = {
    "Programming Languages": ["Python", "Java", "SQL", "DSA"],
    "Frameworks": ["Qt Designer", "JDBC"],
    "Web Technologies": ["HTML", "CSS", "JavaScript"],
    "Databases": ["MySQL", "SQLite3"],
    "ServiceNow": ["System Administration", "Application Development", "Incident Management", 
                   "Problem Management", "Change Management", "Service Catalog", 
                   "User and Role Management", "Access Control", "Business Rules", 
                   "UI Policies", "Client Scripts"],
    "Tools & Technologies": ["VS Code", "Google Colab", "Jupyter Notebook", "Replit", "Servicenow"]  
}

cols = st.columns(2)
items = list(skills_data.items())
for idx, (category, skills) in enumerate(items):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class="skill-category">
            <h3 class="skill-category-title">{category}</h3>
            <div class="skill-tags">
                {''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills])}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<h3 style="color: #00d4ff; font-size: 2rem; margin-top: 60px; margin-bottom: 30px; text-align: center;">Soft Skills</h3>', unsafe_allow_html=True)

soft_skills = [
    "Strong Collaboration & Teamwork",
    "Adaptable in Dynamic Environments",
    "Client Relationship Management",
    "Problem-Solving Mindset",
    "Quick Learner"
]

cols = st.columns(3)
for idx, skill in enumerate(soft_skills):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="skill-category" style="text-align: center;">
            <p style="color: #e0e0e0; font-size: 1.05rem; margin: 0;">{skill}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Certifications Section
st.markdown('<div id="certifications" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Certifications</h2>', unsafe_allow_html=True)

certifications = [
    ("Certified System Administrator - ServiceNow", "2025", "https://drive.google.com/file/d/1w7lybh9zB-q1qsNoCHcNH3GuH6KG7dUa/view"),
    ("Certified Application Developer - ServiceNow", "2025", "https://drive.google.com/file/d/1Z3eSYGtxu6WGei6sSD-qF0xV459TL9DU/view"),
    ("Programming, Data Structures and Algorithms using Python - NPTEL", "2024", "https://archive.nptel.ac.in/content/noc/NOC24/SEM1/Ecertificates/106/noc24-cs45/Course/NPTEL24CS45S54250031730104507.pdf"),
    ("Google AI Essentials - Google, Coursera", "2024", "https://www.coursera.org/account/accomplishments/verify/NB49HZZRHJ6N"),
    ("Java (Basic) Certificate - HackerRank", "2025", "https://www.hackerrank.com/certificates/bb2a5a287625"),
    ("Python (Basic) Certificate - HackerRank", "2025", "https://www.hackerrank.com/certificates/41269ac79a7a"),
    ("SQL (Basic) Certificate - HackerRank", "2025", "https://www.hackerrank.com/certificates/bc7e1f10410a")
]

for cert, year, link in certifications:
    st.markdown(f"""
    <div class="cert-item">
        <div class="cert-name">{cert}</div>
        <span class="cert-year">{year}</span>
        <a href="{link}" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-left: 15px; display: inline-block;">View Certificate →</a>
    </div>
    """, unsafe_allow_html=True)


# Contact Section
st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Get In Touch</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-container">
    <div class="contact-info">
        <p style="color: #e0e0e0; font-size: 1.2rem; margin-bottom: 30px; line-height: 1.8;">
            I'm always open to discussing new opportunities, collaborations, or just having a chat about technology!
        </p>
        <div class="contact-links">
            <a style="text-decoration:none" href="mailto:luckysatti1045@gmail.com" class="contact-link">Email</a>
            <a style="text-decoration:none" href="tel:+919390984914" class="contact-link">Phone</a>
            <a style="text-decoration:none" href="https://www.linkedin.com/in/sathi-lakshmi-narayana-reddy-b05ab6284/" target="_blank" class="contact-link">LinkedIn</a>
            <a style="text-decoration:none" href="https://github.com/luckysatti" target="_blank" class="contact-link">GitHub</a>
        </div>
        <p style="color: #808080; font-size: 1.05rem; margin-top: 30px;">
            Resident in Tirupati, Andhra Pradesh, India
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)










