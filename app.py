import streamlit as st

# ---------------------------------------------------------------
# ✅ Page Config
# ---------------------------------------------------------------
st.set_page_config(
    page_title="Sathi Lakshmi Narayana Reddy | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------------
# ✅ Custom CSS for styling + dark theme enforcement
# ---------------------------------------------------------------
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0e27, #1a1f3a, #16213e) !important;
    color: #e2e8f0 !important;
}
[data-testid="stHeader"] {display: none;}
#MainMenu, footer {visibility: hidden;}
a {text-decoration: none;}

.nav-bar {
  position: fixed;
  top: 0; left: 0; right: 0;
  background: rgba(10, 14, 39, 0.95);
  padding: 1rem 2rem;
  display: flex; justify-content: space-between; align-items: center;
  z-index: 9999;
  border-bottom: 1px solid rgba(0,212,255,0.25);
}
.nav-logo {
  font-size: 1.3rem; font-weight: 700;
  background: linear-gradient(135deg,#00d4ff,#00ff9d);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.nav-links {display: flex; gap: 1rem;}
.nav-link {
  color: #f8fafc; font-weight: 500; padding: 0.4rem 0.8rem;
  border-radius: 8px; transition: 0.3s;
}
.nav-link:hover {background: rgba(0,212,255,0.2); color: #00d4ff;}

.section {padding: 8rem 2rem 4rem; max-width: 1200px; margin: 0 auto;}
.section-heading {
  font-size: 2.5rem; font-weight: 800;
  background: linear-gradient(135deg,#00d4ff,#00ff9d);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 2rem; text-align: center;
}

.content-card {
  background: rgba(255,255,255,0.05);
  backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(0,212,255,0.15);
  border-radius: 18px;
  padding: 2rem; margin: 1rem 0;
  transition: 0.3s; position: relative;
}
.content-card:hover {
  transform: translateY(-5px); border-color: #00d4ff;
  box-shadow: 0 0 25px rgba(0,212,255,0.3);
}
.card-title {
  font-size: 1.5rem; font-weight: 700;
  background: linear-gradient(135deg,#00d4ff,#00ff9d);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.card-description {color: #cbd5e1; margin: 0.5rem 0 1rem;}
.cert-link {
  color: #00d4ff; font-weight: 600; margin-right: 10px;
}
.cert-link:hover {text-decoration: underline;}
.stat-card {
  background: rgba(255,255,255,0.05);
  padding: 2rem; text-align: center;
  border-radius: 12px; border: 1px solid rgba(0,212,255,0.2);
}
.stat-number {
  font-size: 2rem; font-weight: 800;
  background: linear-gradient(135deg,#00d4ff,#00ff9d);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.stat-label {color: #cbd5e1;}

.contact-link {
  display: inline-block; margin: 0.5rem;
  padding: 0.6rem 1.2rem; border: 1px solid #00d4ff;
  color: #00d4ff; border-radius: 8px;
}
.contact-link:hover {
  background: #00d4ff; color: #0a0e27;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# ✅ Navbar
# ---------------------------------------------------------------
st.markdown("""
<div class="nav-bar">
  <div class="nav-logo">Sathi Lakshmi Narayana Reddy</div>
  <div class="nav-links">
    <a class="nav-link" href="#about">About</a>
    <a class="nav-link" href="#education">Education</a>
    <a class="nav-link" href="#experience">Experience</a>
    <a class="nav-link" href="#projects">Projects</a>
    <a class="nav-link" href="#certifications">Certifications</a>
    <a class="nav-link" href="#contact">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# ✅ About Section
# ---------------------------------------------------------------
st.markdown("""
<section id="about" class="section">
  <h2 class="section-heading">About Me</h2>
  <div class="content-card">
    <p class="card-description">
      I'm <strong>Sathi Lakshmi Narayana Reddy</strong>, a passionate Full Stack Developer and AI/ML student from 
      Mohan Babu University, Tirupati. I enjoy crafting efficient solutions, building web applications, and exploring AI technologies.
      <br><br>
      Skilled in <strong>Python, Java, SQL, DSA, HTML, CSS, JavaScript</strong>, and <strong>ServiceNow development</strong>. 
      I love tackling new challenges and delivering impactful software solutions.
    </p>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# ✅ Education Section
# ---------------------------------------------------------------
st.markdown("""
<section id="education" class="section">
  <h2 class="section-heading">Education</h2>
  <div class="content-card">
    <h3 class="card-title">B.Tech in Artificial Intelligence & Machine Learning</h3>
    <p class="card-description">Mohan Babu University, Tirupati (2022 - 2026)</p>
    <p class="card-description">CGPA: 9.45 / 10</p>
  </div>
  <div class="content-card">
    <h3 class="card-title">Intermediate (MPC)</h3>
    <p class="card-description">Sri Chaitanya Junior College, Eluru (2020 - 2022)</p>
    <p class="card-description">Marks: 916 / 1000</p>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# ✅ Experience Section
# ---------------------------------------------------------------
st.markdown("""
<section id="experience" class="section">
  <h2 class="section-heading">Experience</h2>

  <div class="content-card">
    <h3 class="card-title">Java Full Stack Developer Intern</h3>
    <p class="card-description">NETWORX | June 2025 - August 2025</p>
    <ul>
      <li>Developed a Banking System Simulator using Java, Spring Boot, and SQLite.</li>
      <li>Designed front-end using HTML and CSS; integrated JDBC for database operations.</li>
    </ul>
    <a href="https://drive.google.com/file/d/1QM-kSE_ufTKhHvIS2QcFOltwEZ7BC_Cc/view" target="_blank" class="cert-link">View Certificate →</a>
  </div>

  <div class="content-card">
    <h3 class="card-title">AIML Intern</h3>
    <p class="card-description">AICTE (Eduskills) | Oct 2024 - Dec 2024</p>
    <ul>
      <li>Worked with ML algorithms and implemented model training pipelines.</li>
      <li>Improved understanding of AI workflows and deployment strategies.</li>
    </ul>
    <a href="https://drive.google.com/file/d/1RsvlfH8mgGtt3jA5hAx_EXX49YcaxABG/view" target="_blank" class="cert-link">View Certificate →</a>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# ✅ Projects Section
# ---------------------------------------------------------------
st.markdown("""
<section id="projects" class="section">
  <h2 class="section-heading">Projects</h2>

  <div class="content-card">
    <h3 class="card-title">Fantasy Cricket Application</h3>
    <p class="card-description">GUI-based app using Python and SQL for team creation, scoring, and player management.</p>
    <a href="https://github.com/luckysatti/Fantasy-Cricket-Application" target="_blank" class="cert-link">GitHub →</a>
    <a href="https://www.linkedin.com/posts/sathi-lakshmi-narayana-reddy-b05ab6284_excited-to-share-my-latest-project-activity-7211786994459271168-Ejiz" target="_blank" class="cert-link">LinkedIn →</a>
  </div>

  <div class="content-card">
    <h3 class="card-title">Banking System Simulator</h3>
    <p class="card-description">Java-based Banking System using Spring Boot, JDBC, and SQLite3 supporting all core banking operations.</p>
    <a href="https://github.com/luckysatti/Banking-System" target="_blank" class="cert-link">GitHub →</a>
  </div>

  <div class="content-card">
    <h3 class="card-title">Electricity Bill Management System</h3>
    <p class="card-description">ServiceNow-based platform to manage customer billing and payments, integrated with a Virtual Agent.</p>
    <a href="https://www.linkedin.com/posts/sathi-lakshmi-narayana-reddy-b05ab6284_servicenow-learningbydoing-servicenowdeveloper-activity-7370362503954022400--CMW" target="_blank" class="cert-link">LinkedIn →</a>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# ✅ Certifications Section
# ---------------------------------------------------------------
st.markdown("""
<section id="certifications" class="section">
  <h2 class="section-heading">Certifications</h2>

  <div class="content-card">
    <p>✅ <a href="https://drive.google.com/file/d/1w7lybh9zB-q1qsNoCHcNH3GuH6KG7dUa/view" class="cert-link" target="_blank">ServiceNow Certified System Administrator (2025)</a></p>
    <p>✅ <a href="https://drive.google.com/file/d/1Z3eSYGtxu6WGei6sSD-qF0xV459TL9DU/view" class="cert-link" target="_blank">ServiceNow Certified Application Developer (2025)</a></p>
    <p>✅ <a href="https://archive.nptel.ac.in/content/noc/NOC24/SEM1/Ecertificates/106/noc24-cs45/Course/NPTEL24CS45S54250031730104507.pdf" class="cert-link" target="_blank">NPTEL - Python DSA (2024)</a></p>
    <p>✅ <a href="https://www.coursera.org/account/accomplishments/verify/NB49HZZRHJ6N" class="cert-link" target="_blank">Google AI Essentials (Coursera)</a></p>
    <p>✅ <a href="https://www.hackerrank.com/certificates/bb2a5a287625" class="cert-link" target="_blank">Java (Basic) - HackerRank</a></p>
    <p>✅ <a href="https://www.hackerrank.com/certificates/41269ac79a7a" class="cert-link" target="_blank">Python (Basic) - HackerRank</a></p>
    <p>✅ <a href="https://www.hackerrank.com/certificates/bc7e1f10410a" class="cert-link" target="_blank">SQL (Basic) - HackerRank</a></p>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# ✅ Contact Section
# ---------------------------------------------------------------
st.markdown("""
<section id="contact" class="section">
  <h2 class="section-heading">Contact</h2>
  <div class="content-card" style="text-align:center;">
    <p>Email: <a href="mailto:luckysatti1045@gmail.com" class="cert-link">luckysatti1045@gmail.com</a></p>
    <p>Phone: <a href="tel:+919390984914" class="cert-link">+91 9390984914</a></p>
    <p>
      <a href="https://github.com/luckysatti" class="contact-link" target="_blank">GitHub</a>
      <a href="https://www.linkedin.com/in/sathi-lakshmi-narayana-reddy-b05ab6284/" class="contact-link" target="_blank">LinkedIn</a>
    </p>
    <p style="color:#94a3b8;">Tirupati, Andhra Pradesh, India</p>
  </div>
</section>
""", unsafe_allow_html=True)
