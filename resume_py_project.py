from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_resume(name, email, phone, skills, experience, education, job_title="Software Engineer"):
    """Generate a professional resume with a structured format"""
    resume_template = f"""
{name}
{email} | {phone}

------------------------------
PROFESSIONAL SUMMARY
------------------------------
Experienced {job_title} with expertise in {", ".join(skills.split(",")[:3])} and a strong background in {experience}. 
Passionate about delivering high-quality solutions and optimizing workflows.

------------------------------
WORK EXPERIENCE
------------------------------
{experience}

------------------------------
SKILLS
------------------------------
{skills}

------------------------------
EDUCATION
------------------------------
{education}

------------------------------
REFERENCES
------------------------------
Available upon request.
    """
    return resume_template.strip()

def save_as_pdf(content, filename="resume.pdf"):
    """Convert resume text to a properly formatted PDF using reportlab"""
    try:
        filename = filename if filename.endswith(".pdf") else filename + ".pdf"

        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        text = c.beginText(50, height - 50)
        text.setFont("Helvetica", 12)
        text.setLeading(16)  # Improve line spacing

        for line in content.split("\n"):
            text.textLine(line.strip())

        c.drawText(text)
        c.save()
        print(f"\n✅ Resume saved as {os.path.abspath(filename)}")
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")

# Take user input with validation
def get_input(prompt):
    """Helper function to get validated user input"""
    value = input(prompt).strip()
    return value if value else "N/A"

name = get_input("Enter your full name: ")
email = get_input("Enter your email: ")
phone = get_input("Enter your phone number: ")
job_title = get_input("Enter your desired job title: ")
skills = get_input("Enter your skills (comma-separated): ")
experience = get_input("Enter your work experience: ")
education = get_input("Enter your education details: ")

# Generate resume
resume_text = generate_resume(name, email, phone, skills, experience, education, job_title)

# Print & Save as PDF
print("\nGenerated Resume:\n")
print(resume_text)

# Save to PDF
save_as_pdf(resume_text, filename=f"{name.replace(' ', '_')}_Resume.pdf")
