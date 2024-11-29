import os
import logging
from pathlib import Path
from para2pdf import save_to_pdf
from generate_cover_letter import CoverLetterGenerator


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 


def main():

    applicant_name:str = os.environ.get('applicant_name', 'default_value')
    applicant_email:str = os.environ.get('applicant_email', 'default_value')
    applicant_phone:str = os.environ.get('applicant_phone', 'default_value')
    company_name = os.environ.get('company_name', 'default_value')
    job_description = os.environ.get('job_description', 'default_value')
    resume_path = "cv.pdf"

    # resume_path = os.environ.get('resume_path', 'default_value')
    
   

    logger.info(f"resume_path: {resume_path}")
 

    if company_name == 'default_value' or company_name == '':
        logger.error(f"Can't generate cover letter, please provide company_name")
        return f"Can't generate cover letter, please provide company_name"
    if job_description == 'default_value' or job_description == '':
        logger.error(f"Can't generate cover letter, please provide job_description")
        return f"Can't generate cover letter, please provide job_description"
    if resume_path == 'default_value' or resume_path == '':
        logger.error(f"Can't generate cover letter, please provide resume_path")
        return f"Can't generate cover letter, please provide resume_path"


    cover_letter_generator = CoverLetterGenerator(company_name, job_description, resume_path)
    cover_letter = cover_letter_generator()
    
    if cover_letter is None:
        logger.error(f"Can't generate cover letter")
        cover_letter = f"Can't generate cover letter"
    
   # Get the directory of the current script (run.py)
    script_dir = Path(__file__).parent

    # Define the path for the 'output' folder inside the script's directory
    output_dir = script_dir / 'output'
    output_dir.mkdir(exist_ok=True)  # Create 'output' directory if it doesn't exist

    # Define the file path within the 'output' directory
    output_file = output_dir / 'result.pdf'

    save_to_pdf(cover_letter, output_file, applicant_name, applicant_phone, applicant_email)
    

if __name__ == "__main__":
    main()    

