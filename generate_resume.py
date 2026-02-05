from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 24)
        self.set_text_color(15, 23, 42) # Slate #0f172a
        self.cell(0, 15, 'Srimanyu Acharya H', ln=True, align='C')
        self.set_font('helvetica', 'I', 12)
        self.set_text_color(100, 116, 139) # Slate-500
        self.cell(0, 5, 'srimanyuacharya@gmail.com | +91 8088151160', ln=True, align='C')
        self.cell(0, 5, 'github.com/srimanyuacharyah | linkedin.com/in/srimanyu-a-494304310', ln=True, align='C')
        self.ln(10)

    def section_title(self, title):
        self.set_font('helvetica', 'B', 14)
        self.set_fill_color(241, 245, 249) # Slate-100
        self.set_text_color(15, 23, 42)
        self.cell(0, 8, f' {title}', ln=True, fill=True)
        self.ln(3)

    def body_text(self, text):
        self.set_font('helvetica', '', 11)
        self.set_text_color(51, 65, 85) # Slate-700
        self.multi_cell(0, 6, text)
        self.ln(4)

pdf = ResumePDF()
pdf.add_page()

# Summary
pdf.section_title('Professional Summary')
pdf.body_text('Motivated computer science student (Expected 08/2027) with foundational experience in core programming and front-end development. Eager to leverage technical knowledge, including exposure to React and AWS Cloud, and collaborate effectively in a dynamic team setting. Recognized for effective communication and problem-solving skills, and a friendly, positive attitude.')

# Education
pdf.section_title('Education')
pdf.set_font('helvetica', 'B', 11)
pdf.cell(0, 6, 'Bachelor in Computer Science and Engineering', ln=True)
pdf.set_font('helvetica', '', 11)
pdf.cell(0, 6, 'Maharaja Institute of Technology, Mysore, India | 7.94 CGPA', ln=True)
pdf.cell(0, 6, '2023 - 2027 (Expected August 2027)', ln=True)
pdf.ln(4)

# Skills
pdf.section_title('Skills')
pdf.body_text('Technical: Java, Python, SQL, C++, C, HTML, CSS, React (Foundational Knowledge)\nCloud & AI: AWS Cloud Practitioner Essentials, Artificial Intelligence Fundamentals\nNetworking: Packet Switching Networks and Algorithms, JDBC\nSoft Skills: Teamwork and collaboration, Time management, Friendly and positive attitude')

# Projects
pdf.section_title('Key Projects')
projects = [
    ('Offline Cyber Tutor', 'https://github.com/srimanyuacharyah/cyber-safety-tutor.git'),
    ('Eng to Kan Translator', 'https://github.com/srimanyuacharyah/eng-to-kan-translator.git'),
    ('CNN Flask Application', 'https://github.com/srimanyuacharyah/cnn-flask-application.git'),
    ('Chatbot', 'https://github.com/srimanyuacharyah/chatbot.git')
]
for name, link in projects:
    pdf.set_font('helvetica', 'B', 11)
    pdf.cell(0, 6, f'{name}: ', ln=False)
    pdf.set_font('helvetica', '', 11)
    pdf.set_text_color(56, 189, 248) # Accent #38bdf8
    pdf.cell(0, 6, link, ln=True, link=link)
    pdf.set_text_color(51, 65, 85)
pdf.ln(4)

# Certifications
pdf.section_title('Certifications')
pdf.body_text('- Advanced Java | Learn Quest (Dec 2025)\n- Introduction to Java Database Connectivity (JDBC) | Coursera (Dec 2025)\n- AWS Cloud Practitioner Essentials | Amazon Web Services (Nov 2025)\n- Artificial Intelligence Fundamentals | IBM (Oct 2025)\n- Developing Front-End Apps with React | IBM (Oct 2025)')

# Languages & Hobbies
pdf.section_title('Languages & Hobbies')
pdf.body_text('Languages: Kannada (Bilingual), Hindi (Intermediate), English (Elementary)\nHobbies: Reading newspapers daily, Watching cricket, Drawing/sketching')

pdf.output('resume.pdf')
print("PDF Resume generated successfully as resume.pdf")
