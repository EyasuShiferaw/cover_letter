
system_prompt = """
You are a Precision Prose Coach, an expert in crafting concise and impactful cover letters tailored to job descriptions and resumes. Your task is to generate highly customized, cover letters that align the candidate’s skills and experiences with the job requirements while reflecting the company’s values and mission.  
"""

# coverletter_template = """
# Compose a brief and impactful cover letter based on the provided job description and resume. The letter should be no longer than three paragraphs and should be written in a professional, yet conversational tone. Avoid using any placeholders, and ensure that the letter flows naturally and is tailored to the job.

# Analyze the job description to identify key qualifications and requirements. Introduce the candidate succinctly, aligning their career objectives with the role. Highlight relevant skills and experiences from the resume that directly match the job’s demands, using specific examples to illustrate these qualifications. Reference notable aspects of the company, such as its mission or values, that resonate with the candidate’s professional goals. Conclude with a strong statement of why the candidate is a good fit for the position, expressing a desire to discuss further.

# Please write the cover letter in a way that directly addresses the job role and the company’s characteristics, ensuring it remains concise and engaging without unnecessary embellishments. The letter should be formatted into paragraphs and should not include a greeting or signature.

# ## Rules:
# - Provide only the text of the cover letter.
# - Do not include any introductions, explanations, or additional information.
# - The letter should be formatted into paragraph.

# ## Company Name:
# {company}

# ## Job Description:
# ```
# {job_description}
# ```
# ## My resume:
# ```
# {resume}
# ```
# """



coverletter_template = """
Objective: Generate a Tailored, Impactful First-Person Cover Letter

First-Person Writing Requirements:
- ALWAYS write in first-person perspective ("I", "my")
- Candidate must speak directly about their own experiences
- Use personal pronouns consistently throughout the letter

Key Principles:
- Create a concise, powerful 3-paragraph cover letter
- Directly align MY skills with job requirements
- Demonstrate personal understanding of role and company

Letter Construction Guidelines:
- Length: 250-350 words
- Tone: Professional first-person narrative
- Use "I" to personalize every skill and achievement
- Avoid third-person references to the candidate

Narrative Structure:
1. First Paragraph: 
   - Introduce MYSELF
   - Use "I am" statements
   - Connect personal career goals to the role

2. Second Paragraph:
   - Describe MY specific skills
   - Use "I have" and "I've" to highlight achievements
   - Provide direct, personal examples

3. Third Paragraph:
   - Express MY enthusiasm
   - Use "I'm excited" or "I'm passionate"
   - Demonstrate forward-looking commitment

Critical First-Person Checklist:
- Every paragraph must contain multiple first-person pronouns
- Avoid passive voice
- Speak directly and personally about capabilities
- Ensure authentic, personal tone
- Avoid using any placeholders, and ensure that the letter flows naturally and is tailored to the job.
- The letter should be formatted into paragraphs and should not include a greeting or signature.

## Company Name:
{company}

## Job Description:
{job_description}

## Candidate Resume:
{resume}
"""


summarize_prompt_template = """
As a seasoned HR expert, your task is to identify and outline the key skills and requirements necessary for the position of this job. Use the provided job description as input to extract all relevant information. This will involve conducting a thorough analysis of the job's responsibilities and the industry standards. You should consider both the technical and soft skills needed to excel in this role. Additionally, specify any educational qualifications, certifications, or experiences that are essential. Your analysis should also reflect on the evolving nature of this role, considering future trends and how they might affect the required competencies.

Rules:
Remove boilerplate text
Include only relevant information to match the job description against the resume

# Analysis Requirements
Your analysis should include the following sections:
Technical Skills: List all the specific technical skills required for the role based on the responsibilities described in the job description.
Soft Skills: Identify the necessary soft skills, such as communication abilities, problem-solving, time management, etc.
Educational Qualifications and Certifications: Specify the essential educational qualifications and certifications for the role.
Professional Experience: Describe the relevant work experiences that are required or preferred.
Role Evolution: Analyze how the role might evolve in the future, considering industry trends and how these might influence the required skills.

# Final Result:
Your analysis should be structured in a clear and organized document with distinct sections for each of the points listed above. Each section should contain:
This comprehensive overview will serve as a guideline for the recruitment process, ensuring the identification of the most qualified candidates.

# Job Description:
```
{text}
```

---

# Job Description Summary
# """


summary_resume_prompt_template = """
As an experienced HR professional and resume expert, your task is to create a comprehensive and strategic summary of the candidate's resume. Use the provided resume as input to extract and highlight the most relevant and impactful information that aligns with potential job opportunities.

Rules:
- Analyze the resume comprehensively
- Focus on key achievements, skills, and professional highlights
- Provide a concise yet thorough summary that showcases the candidate's unique value proposition

# Analysis Sections:
1. Professional Profile:
   - Craft a compelling 2-3 sentence overview of the candidate's professional identity
   - Highlight key career trajectory and core professional strengths

2. Technical Skills:
   - List and categorize all technical skills and technologies
   - Prioritize skills most relevant to current industry demands
   - Note proficiency levels if clearly indicated

3. Professional Experience Highlights:
   - Summarize key roles and most significant achievements
   - Extract quantifiable accomplishments (metrics, impacts, results)
   - Identify transferable skills across different positions

4. Educational Background:
   - Outline academic qualifications
   - Note relevant certifications or specialized training
   - Highlight academic achievements or distinctions

5. Soft Skills and Professional Attributes:
   - Identify core soft skills demonstrated through experience
   - Extract leadership qualities, communication strengths, and interpersonal capabilities

6. Career Potential and Growth Trajectory:
   - Analyze the candidate's potential for future roles
   - Identify emerging skill sets and adaptability
   - Suggest potential career paths based on professional profile

# Formatting Guidelines:
- Use clear, concise language
- Avoid redundant information
- Ensure each section provides strategic insights
- Maintain a professional and objective tone

# Final Deliverable:
Produce a strategic resume summary that:
- Captures the essence of the candidate's professional capabilities
- Provides a quick, comprehensive overview for potential employers
- Highlights unique value propositions and key strengths

# Input Resume:
```
{resume}
```

# Resume Summary
"""
