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
   temp = ["Sincerely,", "Regards,", "Best,", "Respectfully,", "Thank you,", "Thank you for your consideration,"]
   return (random.choice(temp)) 


def save_to_pdf(
       test:str,
       filename:str =" cover1_letter.pdf",
       applicant_name:str = "Your Name",
       applicant_phone:str = "555-123-4567",
       applicant_email:str = "your.email@example.com",
      
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

    c = canvas.Canvas(filename, pagesize=letter)

    # Get the page dimensions
    page_width, page_height = letter  # letter is a tuple (width, height)

    # Define margins (adjust as needed)
    left_margin = 1 * inch
    right_margin = 1 * inch
    usable_width = page_width - left_margin - right_margin

    # Header (Applicant Info)
    # c.setFont("Times-Bold", 12)
    # c.drawString(1 * inch, 10 * inch, applicant_name)
    c.setFont("Times-Roman", 10)
    c.drawString(1 * inch, 10 * inch, applicant_name)
    # c.drawString(1 * inch, 9.8 * inch, applicant_address)
    c.drawString(1 * inch, 9.8 * inch, applicant_phone)
    c.drawString(1 * inch, 9.6 * inch, applicant_email)

    # Date
    c.setFont("Times-Roman", 10)
    c.drawString(1 * inch, 9.2 * inch, date)
    c.drawString(1 * inch, 8.8 * inch, salutation)

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

    flowable_y = 8.4 * inch
    for element in content:
        w, h = element.wrap(usable_width, page_height)
        element.drawOn(c, left_margin, flowable_y - h)
        flowable_y -= h + 6  # 6 points space between elements.

    c.save()
    logger.info(f"saved to pdf")


