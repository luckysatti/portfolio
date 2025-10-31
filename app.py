import streamlit as st

st.set_page_config(page_title="Sathi Lakshmi Narayana Reddy | Portfolio", layout="wide")

# ------------------- CSS Styling -------------------
st.markdown("""
<style>
/* Reset + Base */
* { margin: 0; padding: 0; box-sizing: border-box; scroll-behavior: smooth; font-family: 'Poppins', sans-serif; }

body {
  background: linear-gradient(135deg, #0f172a, #1e293b);
  color: #f1f5f9;
  font-size: 16px;
  line-height: 1.6;
}

/* Navbar */
.nav-bar {
  background: rgba(15, 23, 42, 0.95);
  backdrop-filter: blur(8px);
  position: fixed;
  top: 0;
  width: 100%;
  padding: 0.8rem 2rem;
  z-index: 999;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
}
.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.nav-logo {
  font-size: 1.4rem;
  font-weight: 700;
  color: #38bdf8;
}
.nav-links {
  display: flex;
  gap: 1.5rem;
}
.nav-link {
  color: #f8fafc;
  text-decoration: none;
  font-weight: 500;
  transition: 0.3s;
}
.nav-link:hover {
  color: #38bdf8;
}

/* Hero Section */
.hero-section {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 8rem 4rem 4rem;
}
.hero-content {
  flex: 1;
  min-width: 300px;
}
.hero-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #38bdf8;
  margin-bottom: 0.5rem;
}
.hero-subtitle {
  font-size: 1.3rem;
  color: #cbd5e1;
  margin-bottom: 1rem;
}
.hero-description {
  max-width: 500px;
  color: #e2e8f0;
  margin-bottom: 1.5rem;
}
.cta-container {
  display: flex;
  gap: 1rem;
}
.cta-button {
  padding: 0.6rem 1.3rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  background: #334155;
  color: #f1f5f9;
  transition: all 0.3s;
}
.cta-button-primary {
  background: #38bdf8;
  color: #0f172a;
}
.cta-button:hover {
  transform: scale(1.05);
}
.hero-image-container {
  flex: 1;
  display: flex;
  justify-content: center;
  min-width: 300px;
}
.hero-image {
  width: 240px;
  height: 240px;
  border-radius: 50%;
  border: 4px solid #38bdf8;
  object-fit: cover;
  box-shadow: 0 0 30px rgba(56,189,248,0.5);
}

/* Section Styling */
.section {
  padding: 5rem 2rem;
  text-align: center;
}
.section-heading {
  font-size: 2rem;
  color: #38bdf8;
  margin-bottom: 2rem;
  position: relative;
}
.section-heading::after {
  content: "";
  width: 80px;
  height: 3px;
  background: #38bdf8;
  display: block;
  margin: 0.5rem auto;
}

/* Cards */
.content-card {
  background: rgba(30, 41, 59, 0.8);
  border-radius: 12px;
  padding: 1.5rem;
  margin: 1rem auto;
  max-width: 800px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  transition: transform 0.3s;
}
.content-card:hover { transform: translateY(-5px); }
.card-title {
  color: #38bdf8;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.card-description {
  color: #e2e8f0;
}

/* Skills */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  justify-items: center;
}
.skill-category-title {
  color: #f8fafc;
  margin-bottom: 1rem;
}
.skill-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
}
.skill-tag {
  background: #334155;
  padding: 0.4rem 0.9rem;
  border-radius: 20px;
  font-size: 0.9rem;
  color: #e2e8f0;
  transition: 0.3s;
}
.skill-tag:hover {
  background: #38bdf8;
  color: #0f172a;
}

/* Projects */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

/* Certifications */
.cert-item {
  background: rgba(30,41,59,0.8);
  margin: 0.8rem auto;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  max-width: 600px;
  display: flex;
  justify-content: space-between;
}
.cert-name { color: #e2e8f0; }
.cert-year { color: #38bdf8; }

/* Contact */
.contact-container {
  max-width: 600px;
  margin: auto;
}
.contact-links {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 1rem;
}
.contact-link {
  text-decoration: none;
  color: #38bdf8;
  font-weight: 600;
  transition: 0.3s;
}
.contact-link:hover {
  color: #f8fafc;
}

/* Footer */
.footer {
  background: #0f172a;
  padding: 1rem;
  text-align: center;
  color: #94a3b8;
  font-size: 0.9rem;
  margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------- Navbar -------------------
st.markdown("""
<div class="nav-bar">
  <div class="nav-container">
    <div class="nav-logo">Sathi Lakshmi Narayana Reddy</div>
    <div class="nav-links">
      <a class="nav-link" href="#about">About</a>
      <a class="nav-link" href="#skills">Skills</a>
      <a class="nav-link" href="#projects">Projects</a>
      <a class="nav-link" href="#certifications">Certifications</a>
      <a class="nav-link" href="#contact">Contact</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ------------------- Hero Section -------------------
st.markdown("""
<section class="hero-section" id="home">
  <div class="hero-content">
    <h1 class="hero-title">Sathi Lakshmi Narayana Reddy</h1>
    <h2 class="hero-subtitle">Python Developer | Web Enthusiast | ServiceNow Certified</h2>
    <p class="hero-description">
      Passionate about creating intelligent and efficient solutions using Python, SQL, and modern web technologies.
      Dedicated to continuous learning and innovation.
    </p>
    <div class="cta-container">
      <a href="#projects" class="cta-button cta-button-primary">View Projects</a>
      <a href="#contact" class="cta-button">Get In Touch</a>
    </div>
  </div>
  <div class="hero-image-container">
    <img src="https://avatars.githubusercontent.com/u/your-github-id" class="hero-image" alt="Profile Photo">
  </div>
</section>
""", unsafe_allow_html=True)

# ------------------- About Section -------------------
st.markdown("""
<section id="about" class="section">
  <h2 class="section-heading">About Me</h2>
  <div class="content-card">
    <p class="card-description">
      I’m a dedicated developer skilled in Python, SQL, ServiceNow, and full-stack web development.
      I love building creative and impactful projects like portfolio websites, management systems, and AI-driven applications.
    </p>
  </div>
</section>
""", unsafe_allow_html=True)

# ------------------- Skills Section -------------------
st.markdown("""
<section id="skills" class="section">
  <h2 class="section-heading">Skills</h2>
  <div class="skills-grid">
    <div class="skill-category">
      <h3 class="skill-category-title">Programming</h3>
      <div class="skill-tags">
        <span class="skill-tag">Python</span>
        <span class="skill-tag">Java</span>
        <span class="skill-tag">SQL</span>
      </div>
    </div>
    <div class="skill-category">
      <h3 class="skill-category-title">Web Development</h3>
      <div class="skill-tags">
        <span class="skill-tag">HTML</span>
        <span class="skill-tag">CSS</span>
        <span class="skill-tag">JavaScript</span>
        <span class="skill-tag">React</span>
      </div>
    </div>
    <div class="skill-category">
      <h3 class="skill-category-title">ServiceNow</h3>
      <div class="skill-tags">
        <span class="skill-tag">Administration</span>
        <span class="skill-tag">Development</span>
        <span class="skill-tag">Workflow Automation</span>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ------------------- Projects Section -------------------
st.markdown("""
<section id="projects" class="section">
  <h2 class="section-heading">Projects</h2>
  <div class="projects-grid">
    <div class="content-card">
      <h3 class="card-title">Banking System Simulator</h3>
      <p class="card-description">
        A web-based banking simulator built using JSP, Servlets, and SQLite with full account management and transaction features.
      </p>
    </div>
    <div class="content-card">
      <h3 class="card-title">Hotel Pineapple – Food Ordering System</h3>
      <p class="card-description">
        An interactive food ordering website developed with HTML, CSS, JS, and PHP integrated with SQL database.
      </p>
    </div>
    <div class="content-card">
      <h3 class="card-title">Crop Recommendation System</h3>
      <p class="card-description">
        A machine learning project predicting the most suitable crop for given soil and climate conditions using Python and ML libraries.
      </p>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ------------------- Certifications Section -------------------
st.markdown("""
<section id="certifications" class="section">
  <h2 class="section-heading">Certifications</h2>
  <div class="cert-item">
    <div class="cert-name">ServiceNow Certified System Administrator</div>
    <div class="cert-year">2025</div>
  </div>
  <div class="cert-item">
    <div class="cert-name">ServiceNow Certified Application Developer</div>
    <div class="cert-year">2025</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ------------------- Contact Section -------------------
st.markdown("""
<section id="contact" class="section">
  <h2 class="section-heading">Contact Me</h2>
  <div class="contact-container">
    <p>Let’s connect! I’m open to collaborations, internships, or freelance opportunities.</p>
    <div class="contact-links">
      <a href="mailto:sathilucky2003@gmail.com" class="contact-link">Email</a>
      <a href="https://www.linkedin.com/in/sathi-lakshmi-narayana-reddy" class="contact-link">LinkedIn</a>
      <a href="https://github.com/yourgithubusername" class="contact-link">GitHub</a>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ------------------- Footer -------------------
st.markdown("""
<div class="footer">
  © 2025 Sathi Lakshmi Narayana Reddy. All rights reserved.
</div>
""", unsafe_allow_html=True)
