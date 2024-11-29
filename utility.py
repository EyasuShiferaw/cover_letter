import os
import logging
import pymupdf
import aisuite as ai
from dotenv import load_dotenv
from functools import lru_cache
from tenacity import retry, stop_after_attempt, wait_exponential
from prompt import summary_resume_prompt_template


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 

# Load environment variables from .env file
load_dotenv()



@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=15))
def get_completion(messages: list[dict]) -> str:
    """ Generate a completion for the given messages and model.
    
    Args:
        messages (list): A list of messages, where each message is a dictionary with the following keys:
            - role: The role of the sender of the message, e.g. "user" or "system".
            - content: The text of the message.
        model (str): The model to use to generate the completion.
    
    Returns:
        str: The generated completion.
    """
    logger.info(f"Getting completion for messages:")
    client = ai.Client()
    client.configure({"openai" : {
  "api_key": os.environ.get("API_KEY"),
}})
    response = None
    model = "openai:gpt-4o"
    try:
        logger.info("Trying to get completion for messages")
        response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.75
            )
    except Exception as e:
        logger.error(f"Error getting completion for messages.\nException: {e}")
        raise  # Allow @retry to handle the exception
    else:
        logger.info(f"successfully got completion for messages")
        return response.choices[0].message.content

@lru_cache(maxsize=100)
def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    Args:
        file_path (str): Path to the PDF file.
    Returns:
        str: Extracted text.
    """
    logger.info(f"starting to extract text from PDF file: {file_path}")
    if not os.path.isfile(file_path):
        logger.error(f"File not found: {file_path}")
        return None
        
    try:
        doc = pymupdf.open(file_path) 

    except Exception as e:
        logger.error(f"Can not extract text from PDF file: {file_path}")
        return None 
    else:
        text = ""
        for page in doc:
            text += page.get_text()
        logger.info(f"successfully extracted text from PDF file: {file_path}")
        return text

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=15))
def summary_resume(resume: str) -> str:
    """
    Summary the resume.
    Args:
        resume (str): The resume.
    Returns:
        str: The summary of the resume.
    """
    messages = [
        {"role": "user", "content": summary_resume_prompt_template.format(resume=resume)}
    ]
    logger.info(f"starting to summarize resume")
    try:
        summary = get_completion(messages)
    except Exception as e:
        logger.error(f"Error summarizing resume.\nException: {e}")
        return None
    logger.info(f"successfully summarized resume")
    return summary

@lru_cache(maxsize=100)
def resume_pipeline(resume_path: str) -> str:
    """
    pipline to extract text from pdf and summarize it.
    Args:
        resume_path (str): The path to the resume.
    Returns:
        str: The summary of the resume.
    """
    resume = extract_text_from_pdf(resume_path)
    if resume is None:
        logger.error(f"Can not extract text from resume: {resume_path}")
        raise Exception(f"Can not extract text from resume: {resume_path}")
        return None
    summary = summary_resume(resume)
    if summary is None:  
        logger.error(f"Can not summarize resume: {resume_path}")
        raise Exception(f"Can not summarize resume: {resume_path}")
        return None
    return summary

