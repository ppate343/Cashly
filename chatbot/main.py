# Third-party imports
from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Depends
from decouple import config
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

# Internal imports
from models import Conversation, SessionLocal
from utils import send_message, logger

#loading environment variables
load_dotenv()
open_api_key = os.environ.get('OPEN_API_KEY')
whatsapp_number= os.environ.get('TO_NUMBER')


app = FastAPI()
# Set up the OpenAI API client
client = OpenAI(api_key=open_api_key)

#whatsapp_number = config("TO_NUMBER")

# Dependency
# creating new db session using session Local 
# once calling function is complete, close db 
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/message")
async def reply(Body: str = Form(), db: Session = Depends(get_db)):

    incoming_message = Body.strip().lower()
    
    # Check if the incoming message is a greeting
    if incoming_message in ["hi", "hello", "start"]:
        welcome_message = ("Thank you for filling out a form with Pinapple mortgages! One of our mortgage agents will give you a call soon. In the mean time, you can ask me any questions "
                           "related to loan types, eligibility, required documents, or book an appointment."
                           "You can also book an appointment for the call, please respond with 'appointment' to pick a date and time")
        send_message(whatsapp_number, welcome_message)
        return ""
    
    # Check if the message is about booking an appointment
    if "appointment" in incoming_message:
        appointment_message = "Sure, I can help you book an appointment. Please provide your preferred date and time."
        send_message(whatsapp_number, appointment_message)
        return ""


    # Call the OpenAI API to generate text with GPT-3.5
    response = client.chat.completions.create(
       model = "gpt-3.5-turbo",
       messages = [
            {"role": "user", "content": Body},
        ]
    )

    # The generated text
    #chat_response = response.choices[0].text.strip()  
    chat_response = response.choices[0].message.content.strip()

    # Store the conversation in the database using Conversation
    try:
        conversation = Conversation(
            sender=whatsapp_number,
            message=Body,
            response=chat_response
            )
        db.add(conversation)
        db.commit()
        logger.info(f"Conversation #{conversation.id} stored in database")
    except SQLAlchemyError as e:
        #rolling back in there is an error storing in the database 
        db.rollback()
        logger.error(f"Error storing conversation in database: {e}")
    send_message(whatsapp_number, chat_response)
    return ""