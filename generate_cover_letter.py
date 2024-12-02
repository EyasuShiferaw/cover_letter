import logging
from utility import get_completion,resume_pipeline
from prompt import coverletter_template, summarize_prompt_template, system_prompt


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 

class CoverLetterGenerator:
    def __init__(self,company_name: str, job_description: str, resume_path: str):
        self.company_name = company_name
        self.job_description = job_description
        self.resume_path = resume_path
        self.resume = None
        self.cover_letter = None

    def __str__(self):
        return f"CoverLetterGenerator(company_name={self.company_name}, job_description={self.job_description}, resume_path={self.resume_path})"


    def __call__(self):
     
        self.generate_cover_letter()
        return self.cover_letter


    def construct_messages(self) -> list[dict]:
        """
        Construct the system and user prompts for the OpenAI API.
        
        Args:
            company_name (str): The name of the company.
            job_description (str): The job description.
            resume (str): The resume.
        
        Returns:
            list: A list of dictionaries representing the system and user prompts.
        """
        logger.info(f"calling the pipeline to extract text from resume and summarize it")
        try:
            self.resume = resume_pipeline(self.resume_path)
        except Exception as e:
            return f"Error extracting text from resume.\nException: {e}"
        if self.resume is None:
            return f"Can't extract text from resume: {self.resume_path}"
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": coverletter_template.format(company=self.company_name,job_description=self.job_description, resume=self.resume)}
        ]
        logger.info(f"Finished constructing messages")
        return messages

    def generate_cover_letter(self) -> str:
        """
        Generate a cover letter based on the provided job description and resume.
        Args:
            company_name (str): The name of the company.
            job_description (str): The job description.
            resume (str): The resume.
        
        Returns:
            list: A list of dictionaries representing the system and user prompts.
        """
        logger.info(f"starting the process to generate cover letter")

        messages = self.construct_messages()
        if not isinstance(messages, list):
            logger.error(f"Can't construct messages")
            return f"Can't construct messages"
        
        self.cover_letter = get_completion(messages)
        if self.cover_letter is None:
            logger.error(f"Can't generate cover letter")
            return f"Can't generate cover letter"
        else:
            logger.info("successfully generated cover letter")
        print(self.cover_letter)    
        return self.cover_letter

