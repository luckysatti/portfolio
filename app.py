                # import streamlit as st

# # ---------- PAGE CONFIG ----------
# st.set_page_config(
#     page_title="Sathi Lakshmi Narayana Reddy | Portfolio",
#     page_icon="💻",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # ---------- CSS STYLING ----------
# st.markdown("""
# <style>
# html, body, [data-testid="stAppViewContainer"], [data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"] {
#   background: linear-gradient(135deg, #0f172a, #1e293b) !important;
#   color: #e2e8f0 !important;
#   font-family: 'Poppins', sans-serif !important;
# }

# [data-testid="stHeader"] {background: rgba(15, 23, 42, 0.95) !important;}
# a {text-decoration: none !important; color: #38bdf8 !important;}
# a:hover {text-decoration: underline !important;}

# .nav-bar {
#   position: fixed; top: 0; left: 0; right: 0;
#   background: rgba(15, 23, 42, 0.95);
#   backdrop-filter: blur(10px);
#   padding: 0.8rem 2rem;
#   display: flex; justify-content: space-between; align-items: center;
#   box-shadow: 0 2px 10px rgba(0,0,0,0.4);
#   z-index: 999;
# }
# .nav-logo {font-size: 1.3rem; font-weight: 700; color: #38bdf8;}
# .nav-links {display: flex; gap: 1.2rem;}
# .nav-link {color: #f8fafc; font-weight: 500;}
# .nav-link:hover {color: #38bdf8;}



# .hero-section {
#   padding: 8rem 3rem 4rem;
#   display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center;
# }
# .hero-content {flex: 1; min-width: 300px;}
# .hero-title {font-size: 2.5rem; color: #38bdf8; font-weight: 700; margin-bottom: 0.5rem;}
# .hero-subtitle {font-size: 1.3rem; color: #cbd5e1; margin-bottom: 1rem;}
# .hero-description {max-width: 500px; color: #e2e8f0; margin-bottom: 1.5rem;}
# .hero-image-container {flex: 1; display: flex; justify-content: center;}
# .hero-image {
#   width: 240px; height: 240px; border-radius: 50%;
#   border: 4px solid #38bdf8; object-fit: cover;
#   box-shadow: 0 0 30px rgba(56,189,248,0.4);
# }

# .section {padding: 5rem 2rem; text-align: center;}
# .section-heading {
#   font-size: 2rem; color: #38bdf8; margin-bottom: 2rem;
#   position: relative;
# }
# .section-heading::after {
#   content: ""; width: 80px; height: 3px; background: #38bdf8;
#   display: block; margin: 0.5rem auto;
# }

# .content-card {
#   background: rgba(30,41,59,0.8);
#   padding: 1.5rem; border-radius: 12px;
#   margin: 1rem auto; max-width: 800px;
#   transition: transform 0.3s;
# }
# .content-card:hover {transform: translateY(-5px);}
# .card-title {color: #38bdf8; font-weight: 600; margin-bottom: 0.5rem;}
# .card-subtitle {color: #cbd5e1; font-weight: 500; margin-bottom: 0.5rem;}
# .card-description {color: #e2e8f0;}

# .projects-grid {
#   display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
#   gap: 2rem; margin-top: 2rem;
# }

# .skill-tags {
#   display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center;
# }
# .skill-tag {
#   background: #334155; padding: 0.4rem 0.9rem; border-radius: 20px;
#   font-size: 0.9rem; color: #e2e8f0; transition: 0.3s;
# }
# .skill-tag:hover {background: #38bdf8; color: #0f172a;}

# .cert-item {
#   background: rgba(30,41,59,0.8);
#   padding: 1rem 1.5rem; border-radius: 8px;
#   margin: 0.8rem auto; max-width: 700px;
#   display: flex; justify-content: space-between; align-items: center;
# }
# .cert-name {color: #e2e8f0;}
# .cert-link {color: #38bdf8; font-size: 0.9rem;}
# .cert-link:hover {text-decoration: underline;}

# .achievement-item {
#   background: rgba(30,41,59,0.8);
#   margin: 0.5rem auto; padding: 1rem;
#   border-radius: 10px; max-width: 700px;
#   color: #e2e8f0;
# }

# .contact-container {max-width: 600px; margin: auto;}
# .contact-links {
#   display: flex; justify-content: center; gap: 1.5rem; margin-top: 1rem;
# }
# .contact-link {color: #38bdf8; font-weight: 600;}
# .contact-link:hover {text-decoration: underline;}

# .footer {
#   background: #0f172a; padding: 1rem; text-align: center;
#   color: #94a3b8; font-size: 0.9rem; margin-top: 3rem;
# }
# </style>
# """, unsafe_allow_html=True)

# # # ---------- NAV BAR ----------
# # st.markdown("""
# # <div class="nav-bar">
# #   <div class="nav-logo">Sathi Lakshmi Narayana Reddy</div>
# #   <div class="nav-links">
# #     <a class="nav-link" href="#about">About</a>
# #     <a class="nav-link" href="#education">Education</a>
# #     <a class="nav-link" href="#experience">Experience</a>
# #     <a class="nav-link" href="#projects">Projects</a>
# #     <a class="nav-link" href="#skills">Skills</a>
# #     <a class="nav-link" href="#certifications">Certifications</a>
# #     <a class="nav-link" href="#achievements">Achievements</a>
# #     <a class="nav-link" href="#contact">Contact</a>
# #   </div>
# # </div>
# # """, unsafe_allow_html=True)

# # ---------------------------------------------------------------
# # ✅ Navbar
# # ---------------------------------------------------------------
# st.markdown("""
# <div class="nav-bar">
#   <div class="nav-logo">Sathi Lakshmi Narayana Reddy</div>
#   <div class="nav-links">
#     <a class="nav-link" href="#about">About</a>
#     <a class="nav-link" href="#education">Education</a>
#     <a class="nav-link" href="#experience">Experience</a>
#     <a class="nav-link" href="#projects">Projects</a>
#     <a class="nav-link" href="#certifications">Certifications</a>
#     <a class="nav-link" href="#contact">Contact</a>
#   </div>
# </div>
# """, unsafe_allow_html=True)

# # ---------- HERO SECTION ----------
# st.markdown("""
# <section class="hero-section" id="home">
#   <div class="hero-content">
#     <h1 class="hero-title">Sathi Lakshmi Narayana Reddy</h1>
#     <h2 class="hero-subtitle">Full Stack Developer | Python & Java Enthusiast | ServiceNow Certified </h2>
#     <p class="hero-description">
#       Strongly skilled in <strong>Java, Python, DSA, and SQL and ServiceNow development</strong>, with experience in GUI and web development using HTML, CSS, and JavaScript.
#       Passionate about building efficient systems with elegant interfaces, database integration, and strong backend logic. I love tackling new challenges and delivering impactful software solutions.
#     </p>
#   </div>
#   <div class="hero-image-container">
#     <img src="https://raw.githubusercontent.com/luckysatti/photo/main/IMG_20250909_193640.png" class="hero-image">
#   </div>
# </section>
# """, unsafe_allow_html=True)

# # ---------- ABOUT ----------
# st.markdown("""
# <section id="about" class="section">
#   <h2 class="section-heading">About Me</h2>
#   <div class="content-card">
#     <p class="card-description">
#       I’m a passionate software developer focused on creating impactful applications that combine functionality and design.
#       With hands-on experience in full stack development and ServiceNow, I’m eager to solve problems and continuously learn new technologies.
#     </p>
#   </div>
# </section>
# """, unsafe_allow_html=True)

# # ---------- EDUCATION ----------
# st.markdown("""
# <section id="education" class="section">
#   <h2 class="section-heading">Education</h2>
#   <div class="content-card">
#     <h3 class="card-title">B.Tech in Artificial Intelligence and Machine Learning</h3>
#     <p class="card-subtitle">Mohan Babu University, Tirupati (2022–2026)</p>
#     <p class="card-description">CGPA: 9.45 / 10</p>
#   </div>
#   <div class="content-card">
#     <h3 class="card-title">Intermediate (MPC)</h3>
#     <p class="card-description">Sri Chaitanya Junior College, Eluru (2020 - 2022)</p>
#     <p class="card-description">Marks: 916 / 1000</p>
#   </div>
# </section>
# """, unsafe_allow_html=True)

# # ---------- EXPERIENCE ----------
# st.markdown("""
# <section id="experience" class="section">
#   <h2 class="section-heading">Professional Experience</h2>

#   <div class="content-card">
#     <h3 class="card-title">Java Full Stack Developer Intern – NETWORX</h3>
#     <p class="card-subtitle">June 2025 – August 2025</p>
#     <ul class="card-description" style="text-align:left;">
#       <li>Developed Banking System Simulator using Java (OOP + DSA), JDBC, and Spring Boot.</li>
#       <li>Integrated SQLite3 and implemented complete account management features.</li>
#       <li><a href="https://drive.google.com/file/d/1QM-kSE_ufTKhHvIS2QcFOltwEZ7BC_Cc/view" class="cert-link" target="_blank">View Certificate →</a></li>
#     </ul>
#   </div>

#   <div class="content-card">
#     <h3 class="card-title">AIML Intern – AICTE (Eduskills)</h3>
#     <p class="card-subtitle">Oct 2024 – Dec 2024</p>
#     <ul class="card-description" style="text-align:left;">
#       <li>Gained hands-on experience with AI & ML model training and evaluation.</li>
#       <li>Worked on preprocessing, data analysis, and model deployment strategies.</li>
#       <li><a href="https://drive.google.com/file/d/1RsvlfH8mgGtt3jA5hAx_EXX49YcaxABG/view" class="cert-link" target="_blank">View Certificate →</a></li>
#     </ul>
#   </div>
# </section>
# """, unsafe_allow_html=True)

# # # ---------- PROJECTS ----------
# # st.markdown("""
# # <section id="projects" class="section">
# #   <h2 class="section-heading">Projects</h2>
# #   <div class="projects-grid">

# #     <div class="content-card">
# #       <h3 class="card-title">Fantasy Cricket Application</h3>
# #       <p class="card-description">GUI-based application using Python and SQL for team creation, scoring, and player management.</p>
# #       <a href="https://github.com/luckysatti/Fantasy-Cricket-Application" class="cert-link" target="_blank">GitHub →</a> |
# #       <a href="https://www.linkedin.com/posts/sathi-lakshmi-narayana-reddy-b05ab6284_excited-to-share-my-latest-project-activity-7211786994459271168-Ejiz" class="cert-link" target="_blank">LinkedIn →</a>
# #     </div>

# #     <div class="content-card">
# #       <h3 class="card-title">Banking System</h3>
# #       <p class="card-description">Java-based Banking System using Spring Boot, JDBC, and SQLite3 supporting all core banking operations.</p>
# #       <a href="https://github.com/luckysatti/Banking-System" class="cert-link" target="_blank">GitHub →</a>
# #     </div>

# #     <div class="content-card">
# #       <h3 class="card-title">Electricity Bill Management System</h3>
# #       <p class="card-description">ServiceNow-based platform to manage customer billing and payments, integrated with a Virtual Agent.</p>
# #       <a href="https://www.linkedin.com/posts/sathi-lakshmi-narayana-reddy-b05ab6284_servicenow-learningbydoing-servicenowdeveloper-activity-7370362503954022400--CMW" class="cert-link" target="_blank">LinkedIn →</a>
# #     </div>

# #   </div>
# # </section>
# # """, unsafe_allow_html=True)

# # ---------------------------------------------------------------
# # ✅ Projects Section
# # ---------------------------------------------------------------
# st.markdown("""
# <section id="projects" class="section">
#   <h2 class="section-heading">Projects</h2>

#   <div class="content-card">
#     <h3 class="card-title">Fantasy Cricket Application</h3>
#     <p class="card-description">GUI-based app using Python and SQL for team creation, scoring, and player management.</p>
#     <a href="https://github.com/luckysatti/Fantasy-Cricket-Application" target="_blank" class="cert-link">GitHub →</a>
#     <a href="https://www.linkedin.com/posts/sathi-lakshmi-narayana-reddy-b05ab6284_excited-to-share-my-latest-project-activity-7211786994459271168-Ejiz" target="_blank" class="cert-link">LinkedIn →</a>
#   </div>

#   <div class="content-card">
#     <h3 class="card-title">Banking System Simulator</h3>
#     <p class="card-description">Java-based Banking System using Spring Boot, JDBC, and SQLite3 supporting all core banking operations.</p>
#     <a href="https://github.com/luckysatti/Banking-System" target="_blank" class="cert-link">GitHub →</a>
#   </div>

#   <div class="content-card">
#     <h3 class="card-title">Electricity Bill Management System</h3>
#     <p class="card-description">ServiceNow-based platform to manage customer billing and payments, integrated with a Virtual Agent.</p>
#     <a href="https://www.linkedin.com/posts/sathi-lakshmi-narayana-reddy-b05ab6284_servicenow-learningbydoing-servicenowdeveloper-activity-7370362503954022400--CMW" target="_blank" class="cert-link">LinkedIn →</a>
#   </div>
# </section>
# """, unsafe_allow_html=True)


# # ---------- SKILLS ----------
# st.markdown("""
# <section id="skills" class="section">
#   <h2 class="section-heading">Technical Skills</h2>
#   <div class="skill-tags">
#     <span class="skill-tag">Python</span>
#     <span class="skill-tag">Java</span>
#     <span class="skill-tag">SQL</span>
#     <span class="skill-tag">HTML/CSS/JS</span>
#     <span class="skill-tag">Spring Boot</span>
#     <span class="skill-tag">Qt Designer</span>
#     <span class="skill-tag">JDBC</span>
#     <span class="skill-tag">SQLite3</span>
#     <span class="skill-tag">ServiceNow (CSA, CAD)</span>
#   </div>
# </section>
# """, unsafe_allow_html=True)

# # ---------- CERTIFICATIONS ----------
# st.markdown("""
# <section id="certifications" class="section">
#   <h2 class="section-heading">Certifications</h2>

#   <div class="cert-item">
#     <div class="cert-name">ServiceNow Certified System Administrator</div>
#     <a href="https://drive.google.com/file/d/1w7lybh9zB-q1qsNoCHcNH3GuH6KG7dUa/view" target="_blank" class="cert-link">View →</a>
#   </div>

#   <div class="cert-item">
#     <div class="cert-name">ServiceNow Certified Application Developer</div>
#     <a href="https://drive.google.com/file/d/1Z3eSYGtxu6WGei6sSD-qF0xV459TL9DU/view" target="_blank" class="cert-link">View →</a>
#   </div>

#   <div class="cert-item">
#     <div class="cert-name">Programming, Data Structures & Algorithms using Python (NPTEL)</div>
#     <a href="https://archive.nptel.ac.in/content/noc/NOC24/SEM1/Ecertificates/106/noc24-cs45/Course/NPTEL24CS45S54250031730104507.pdf" target="_blank" class="cert-link">View →</a>
#   </div>

#   <div class="cert-item">
#     <div class="cert-name">Google AI Essentials - Coursera</div>
#     <a href="https://www.coursera.org/account/accomplishments/records/NB49HZZRHJ6N" target="_blank" class="cert-link">View →</a>
#   </div>

# </section>
# """, unsafe_allow_html=True)

# # ---------- ACHIEVEMENTS ----------
# st.markdown("""
# <section id="achievements" class="section">
#   <h2 class="section-heading">Achievements</h2>
#   <div class="achievement-item">🏆 1st Place in District-level Abacus Competition (6th Standard)</div>
#   <div class="achievement-item">🥇 1st Place in Running Competition (3rd Standard)</div>
# </section>
# """, unsafe_allow_html=True)

# # ---------- CONTACT ----------
# st.markdown("""
# <section id="contact" class="section">
#   <h2 class="section-heading">Contact Me</h2>
#   <div class="contact-container">
#     <p>Let’s connect! I’m open to new opportunities, collaborations, and challenges.</p>
#     <div class="contact-links">
#       <a href="mailto:luckysatti1045@gmail.com" class="contact-link">Email</a>
#       <a href="tel:+919390984914" class="contact-link">Phone</a>
#       <a href="https://www.linkedin.com/in/sathi-lakshmi-narayana-reddy-b05ab6284/" class="contact-link">LinkedIn</a>
#       <a href="https://github.com/luckysatti" class="contact-link">GitHub</a>
#     </div>
#   </div>
# </section>
# """, unsafe_allow_html=True)

# # ---------- FOOTER ----------
# st.markdown("""
# <div class="footer">
#   © 2025 Sathi Lakshmi Narayana Reddy | Built with ❤️ using Streamlit
# </div>
# """, unsafe_allow_html=True)


import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Sathi Lakshmi Narayana Reddy | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- CSS STYLING ----------
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"] {
  background: linear-gradient(135deg, #0f172a, #1e293b) !important;
  color: #e2e8f0 !important;
  font-family: 'Poppins', sans-serif !important;
  scroll-behavior: smooth !important;
}

[data-testid="stHeader"] {display: none;}
#MainMenu, footer {visibility: hidden;}
a {text-decoration: none !important; color: #38bdf8 !important;}
a:hover {text-decoration: underline !important;}

/* ---------- NAVBAR ---------- */
.nav-bar {
  position: fixed;
  top: 0; left: 0; right: 0;
  background: rgba(15, 23, 42, 0.95);
  backdrop-filter: blur(10px);
  padding: 0.8rem 2rem;
  display: flex; justify-content: space-between; align-items: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.4);
  z-index: 9999;
}
.nav-logo {font-size: 1.3rem; font-weight: 700; color: #38bdf8;}
.nav-links {display: flex; gap: 1.2rem;}
.nav-link {color: #f8fafc; font-weight: 500; cursor: pointer;}
.nav-link:hover {color: #38bdf8;}

/* ---------- HERO ---------- */
.hero-section {
  padding: 9rem 3rem 4rem;
  display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center;
}
.hero-content {flex: 1; min-width: 300px;}
.hero-title {font-size: 2.5rem; color: #38bdf8; font-weight: 700; margin-bottom: 0.5rem;}
.hero-subtitle {font-size: 1.3rem; color: #cbd5e1; margin-bottom: 1rem;}
.hero-description {max-width: 500px; color: #e2e8f0; margin-bottom: 1.5rem;}
.hero-image-container {flex: 1; display: flex; justify-content: center;}
.hero-image {
  width: 240px; height: 240px; border-radius: 50%;
  border: 4px solid #38bdf8; object-fit: cover;
  box-shadow: 0 0 30px rgba(56,189,248,0.4);
}

/* ---------- SECTIONS ---------- */
.section {padding: 6rem 2rem; text-align: center;}
.section-heading {
  font-size: 2rem; color: #38bdf8; margin-bottom: 2rem;
  position: relative;
}
.section-heading::after {
  content: ""; width: 80px; height: 3px; background: #38bdf8;
  display: block; margin: 0.5rem auto;
}

.content-card {
  background: rgba(30,41,59,0.8);
  padding: 1.5rem; border-radius: 12px;
  margin: 1rem auto; max-width: 800px;
  transition: transform 0.3s;
}
.content-card:hover {transform: translateY(-5px);}
.card-title {color: #38bdf8; font-weight: 600; margin-bottom: 0.5rem;}
.card-subtitle {color: #cbd5e1; font-weight: 500; margin-bottom: 0.5rem;}
.card-description {color: #e2e8f0; text-align: left;}

/* ---------- SKILLS ---------- */
.skill-tags {
  display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center;
}
.skill-tag {
  background: #334155; padding: 0.4rem 0.9rem; border-radius: 20px;
  font-size: 0.9rem; color: #e2e8f0; transition: 0.3s;
}
.skill-tag:hover {background: #38bdf8; color: #0f172a;}

/* ---------- CERT ---------- */
.cert-item {
  background: rgba(30,41,59,0.8);
  padding: 1rem 1.5rem; border-radius: 8px;
  margin: 0.8rem auto; max-width: 700px;
  display: flex; justify-content: space-between; align-items: center;
}
.cert-name {color: #e2e8f0;}
.cert-link {color: #38bdf8; font-size: 0.9rem;}
.cert-link:hover {text-decoration: underline;}

/* ---------- CONTACT ---------- */
.contact-container {max-width: 600px; margin: auto;}
.contact-links {
  display: flex; justify-content: center; gap: 1.5rem; margin-top: 1rem;
}
.contact-link {color: #38bdf8; font-weight: 600;}
.contact-link:hover {text-decoration: underline;}

/* ---------- FOOTER ---------- */
.footer {
  background: #0f172a; padding: 1rem; text-align: center;
  color: #94a3b8; font-size: 0.9rem; margin-top: 3rem;
}

/* Fix anchor jump in Streamlit */
section::before {
  display: block;
  content: " ";
  margin-top: -90px;
  height: 90px;
  visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------- NAVBAR ----------
st.markdown("""
<div class="nav-bar">
  <div class="nav-logo">Sathi Lakshmi Narayana Reddy</div>
  <div class="nav-links">
    <a class="nav-link" href="#about">About</a>
    <a class="nav-link" href="#education">Education</a>
    <a class="nav-link" href="#experience">Experience</a>
    <a class="nav-link" href="#projects">Projects</a>
    <a class="nav-link" href="#skills">Skills</a>
    <a class="nav-link" href="#certifications">Certifications</a>
    <a class="nav-link" href="#achievements">Achievements</a>
    <a class="nav-link" href="#contact">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown("""
<section id="home" class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">Sathi Lakshmi Narayana Reddy</h1>
    <h2 class="hero-subtitle">Full Stack Developer | Python & Java Enthusiast | ServiceNow Certified</h2>
    <p class="hero-description">
      Strongly skilled in <strong>Java, Python, DSA, SQL, and ServiceNow development</strong>, with experience in GUI and web development using HTML, CSS, and JavaScript.
      Passionate about building efficient systems with elegant interfaces, database integration, and strong backend logic.
    </p>
  </div>
  <div class="hero-image-container">
    <img src="https://raw.githubusercontent.com/luckysatti/photo/main/IMG_20250909_193640.png" class="hero-image">
  </div>
</section>
""", unsafe_allow_html=True)

# ---------- ABOUT ----------
st.markdown("""
<section id="about" class="section">
  <h2 class="section-heading">About Me</h2>
  <div class="content-card">
    <p class="card-description">
      I’m a passionate software developer focused on creating impactful applications that combine functionality and design.
      With hands-on experience in full stack development and ServiceNow, I’m eager to solve problems and continuously learn new technologies.
    </p>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------- EDUCATION ----------
st.markdown("""
<section id="education" class="section">
  <h2 class="section-heading">Education</h2>
  <div class="content-card">
    <h3 class="card-title">B.Tech in Artificial Intelligence & Machine Learning</h3>
    <p class="card-subtitle">Mohan Babu University, Tirupati (2022–2026)</p>
    <p class="card-subtitle">CGPA: 9.45 / 10</p>
  </div>
  <div class="content-card">
    <h3 class="card-title">Intermediate (MPC)</h3>
    <p class="card-subtitle">Sri Chaitanya Junior College, Eluru (2020–2022)</p>
    <p class="card-subtitle">Marks: 916 / 1000</p>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------- EXPERIENCE ----------
st.markdown("""
<section id="experience" class="section">
  <h2 class="section-heading">Professional Experience</h2>
  <div class="content-card">
    <h3 class="card-title">Java Full Stack Developer Intern – NETWORX</h3>
    <p class="card-subtitle">June 2025 – August 2025</p>
    <ul class="card-description">
      <li>Developed Banking System Simulator using Java (OOP + DSA), JDBC, and Spring Boot.</li>
      <li>Integrated SQLite3 and implemented complete account management features.</li>
      <a  href="https://drive.google.com/file/d/1QM-kSE_ufTKhHvIS2QcFOltwEZ7BC_Cc/view" class="cert-link" target="_blank">View Certificate →</a>
    </ul>
  </div>

  <div class="content-card">
    <h3 class="card-title">AIML Intern – AICTE (Eduskills)</h3>
    <p class="card-subtitle">Oct 2024 – Dec 2024</p>
    <ul class="card-description">
      <li>Gained hands-on experience with AI & ML model training and evaluation.</li>
      <li>Worked on preprocessing, data analysis, and model deployment strategies.</li>
      <a href="https://drive.google.com/file/d/1RsvlfH8mgGtt3jA5hAx_EXX49YcaxABG/view" class="cert-link" target="_blank">View Certificate →</a>
    </ul>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------- PROJECTS ----------
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

# ---------- SKILLS ----------
st.markdown("""
<section id="skills" class="section">
  <h2 class="section-heading">Skills</h2>
  <div class="content-card skills-container" style="text-align:left;">
    <h3 style="color:#38bdf8;">Technical Skills</h3>
    <ul style="list-style-type:none; padding-left:0;">
    <h5 align="center"><strong>Programming Languages</strong> </h5>
        <div class="skill-tags">
            <span class="skill-tag"> Java</span>
            <span class="skill-tag"> Python</span>
            <span class="skill-tag"> SQL</span>
            <span class="skill-tag"> DBMS</span>
            <span class="skill-tag"> DSA</span>
        </div>
        <h5 align="center"><strong>Frame works </strong> </h5>
        <div class="skill-tags">
            <span class="skill-tag"> Spring</span>
            <span class="skill-tag"> Spring Boot</span>
            <span class="skill-tag"> Qt Designer</span>
            <span class="skill-tag"> JDBC</span>
        </div>
        <h5 align="center"> <strong>Web Technologies</strong></strong> </h5>
        <div class="skill-tags">
            <span class="skill-tag"> HTML5</span>
            <span class="skill-tag"> CSS</span>
            <span class="skill-tag"> CSS3</span>
            <span class="skill-tag"> JavaScript</span>
        </div>
        <h5 align="center"><strong>Databases</strong> </h5>
        <div class="skill-tags">
            <span class="skill-tag"> MySQL</span>
            <span class="skill-tag"> SQLite3</span>
            <span class="skill-tag"> SQL</span>
            <span class="skill-tag"> DBMS</span>
            <span class="skill-tag"> DSA</span>
        </div>
        <h5 align="center"><strong>Tools and Technologies</strong> </h5>
        <div class="skill-tags">
            <span class="skill-tag"> VS Code</span>
            <span class="skill-tag"> Google Colab</span>
            <span class="skill-tag"> Jupyter Notebook</span>
            <span class="skill-tag"> Replit</span>
        </div>
        <h5 align="center"><strong>Service Now </strong> </h5>
        <div class="skill-tags">
            <span class="skill-tag"> CSA</span>
            <span class="skill-tag"> CAD</span>
            <span class="skill-tag"> Incident | Problem | Change Management</span>
            <span class="skill-tag"> Service Catalog</span>
            <span class="skill-tag"> User and Role Management | Access Control</span>
            <span class="skill-tag"> Business Rules, UI Policies, Client Scripts</span>
        </div>
    </ul>
    <h3 style="color:#38bdf8; margin-top:1.5rem;">Soft Skills</h3>
    <ul style="list-style-type:none; padding-left:0;">
      <div class="skill-tags">
            <span class="skill-tag">Adaptability and Flexibility</span>
            <span class="skill-tag">Communication and Logical Thinking</span>
            <span class="skill-tag">Problem-solving mindset and Quick Learner</span>
      </div>
    </ul>
  </div>
</section>
""", unsafe_allow_html=True)




# ---------- CERTIFICATIONS ----------
st.markdown("""
<section id="certifications" class="section">
  <h2 class="section-heading">Certifications</h2>
  <div class="cert-item"><div class="cert-name">ServiceNow Certified System Administrator</div>
  <a href="https://drive.google.com/file/d/1w7lybh9zB-q1qsNoCHcNH3GuH6KG7dUa/view" target="_blank" class="cert-link">View →</a></div>

  <div class="cert-item"><div class="cert-name">ServiceNow Certified Application Developer</div>
  <a href="https://drive.google.com/file/d/1Z3eSYGtxu6WGei6sSD-qF0xV459TL9DU/view" target="_blank" class="cert-link">View →</a></div>

  <div class="cert-item"><div class="cert-name">NPTEL: Python DSA</div>
  <a href="https://archive.nptel.ac.in/content/noc/NOC24/SEM1/Ecertificates/106/noc24-cs45/Course/NPTEL24CS45S54250031730104507.pdf" target="_blank" class="cert-link">View →</a></div>

  <div class="cert-item"><div class="cert-name">Google AI Essentials - Coursera</div>
  <a href="https://www.coursera.org/account/accomplishments/verify/NB49HZZRHJ6N" target="_blank" class="cert-link">View →</a></div>
</section>
""", unsafe_allow_html=True)

# ---------- ACHIEVEMENTS ----------
st.markdown("""
<section id="achievements" class="section">
  <h2 class="section-heading">Achievements</h2>
  <div class="content-card">🏆 1st Place in District-level Abacus Competition (6th Standard)</div>
  <div class="content-card">🥇 1st Place in Running Competition (3rd Standard)</div>
</section>
""", unsafe_allow_html=True)

# ---------- CONTACT ----------
st.markdown("""
<section id="contact" class="section">
  <h2 class="section-heading">Contact Me</h2>
  <div class="contact-container">
    <p>Let’s connect! I’m open to new opportunities, collaborations, and challenges.</p>
    <div class="contact-links">
      <a href="mailto:luckysatti1045@gmail.com" class="contact-link">Email</a>
      <a href="tel:+919390984914" class="contact-link">Phone</a>
      <a href="https://www.linkedin.com/in/sathi-lakshmi-narayana-reddy-b05ab6284/" class="contact-link">LinkedIn</a>
      <a href="https://github.com/luckysatti" class="contact-link">GitHub</a>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
  © 2025 Sathi Lakshmi Narayana Reddy | Built with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)












