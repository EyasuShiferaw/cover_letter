import random
from datetime import datetime
import logging

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 

def today_date() -> str:       
    """
    Get today's date in the format of "Month Day, Year"
    """
    today = datetime.now()
    formatted_date = today.strftime("%B %d, %Y")
    return formatted_date

def random_salutation() -> str:
   """
   Get a random salutation
   """      
   temp = ["Sincerely,", "Regards,", "Best,", "Respectfully,", "Thank you,", "Thank you for your consideration,", "Warm regards,"]
   return (random.choice(temp)) 


def save_to_pdf(
       test:str,
       filename:str,
       applicant_name:str,
       applicant_phone:str,
       applicant_email:str,
      
      ):
    """
    Generates a cover letter PDF using ReportLab with Times-Roman font.
    
    Args:
        filename (str): The name of the file to save the PDF to.
        applicant_name (str): The name of the applicant.
        applicant_phone (str): The phone number of the applicant.
        applicant_email (str): The email address of the applicant.
        body_paragraphs (list): A list of paragraphs to include in the body of the letter.
    """

    date=today_date()
    salutation="Dear Hiring Manager"
    body_paragraphs:list = test.split("\n\n")

    logger.info(f"starting to save to pdf")

    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    normal_style.fontName = "Times-Roman"  # Set font to Times-Roman
    heading_style = styles["Heading2"]
    heading_style.fontName = "Times-Bold"   # Use Times-Bold for headings

    c = canvas.Canvas(str(filename), pagesize=letter)

    # Get the page dimensions
    page_width, page_height = letter  # letter is a tuple (width, height)

    # Define margins (adjust as needed)
    left_margin = 1 * inch
    right_margin = 1 * inch
    usable_width = page_width - left_margin - right_margin

    # Header (Applicant Info)
    c.setFont("Times-Roman", 10)
    c.drawString(1 * inch, 10 * inch, applicant_name)
    # c.drawString(1 * inch, 9.8 * inch, applicant_phone)
    # c.drawString(1 * inch, 9.6 * inch, applicant_email)

    # Date
    c.setFont("Times-Roman", 10)
    c.drawString(1 * inch, 9.6 * inch, date)
    c.drawString(1 * inch, 9.2 * inch, salutation)

    # Content (using platypus for text wrapping)
    content = []
    # Body
    for paragraph_text in body_paragraphs:
        content.append(Paragraph(paragraph_text, normal_style))
        content.append(Spacer(1, 0.2 * inch))

    # Sincerely
    content.append(Paragraph(random_salutation(), normal_style))
    

    # Applicant Name (again)
    content.append(Paragraph(applicant_name, normal_style))

    flowable_y = 8.8 * inch
    for element in content:
        w, h = element.wrap(usable_width, page_height)
        element.drawOn(c, left_margin, flowable_y - h)
        flowable_y -= h + 6  # 6 points space between elements.
        

    c.save()
    logger.info(f"saved to pdf")




body_paragraphs = """
I am Eyasu Shiferaw, an AI and software engineer passionate about transforming innovative ideas into practical solutions. My career goal aligns perfectly with the role at Abyss, as I am driven by the desire to create user-friendly AI applications that can be accessed and utilized by a broader audience. The mission of Abyss to empower developers and connect them with those who can benefit from AI solutions resonates deeply with me, and I am eager to contribute to the development and success of your platform.

I have over three years of experience in Python programming, which is a core requirement for this role. At SingularityNet, I developed intelligent agents and optimized data pipelines, which honed my ability to write efficient, scalable code. This experience, coupled with my proficiency in machine learning frameworks like PyTorch and TensorFlow, allows me to seamlessly integrate AI-powered solutions into Python projects. My work with large language models (LLMs) and involvement in prompt engineering ensures that I am well-equipped to develop AI Widgets that require minimal user interaction while delivering powerful results. At iCog-Labs, I led projects that involved semantic search capabilities and web data extraction, which enhanced both system performance and user experience—skills I believe will prove invaluable at Abyss.

I'm excited about the opportunity to work with Abyss as you transition from beta to a fully functional platform. The prospect of helping developers scale and monetize their projects without technical barriers is thrilling. I am particularly passionate about the potential impact of AI Widgets and am eager to contribute my skills and experience to your innovative team. I am looking forward to the possibility of joining Abyss and helping push the boundaries of what AI can offer to both developers and end-users."""

save_to_pdf(body_paragraphs, "cover_letter.pdf", "Eyasu Shiferaw", "555-123-4567", "eyasu.shiferaw@gmail.com")