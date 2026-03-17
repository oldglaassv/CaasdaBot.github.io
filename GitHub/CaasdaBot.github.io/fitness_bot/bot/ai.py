from openai import OpenAI
from config import OPENAI_KEY

client = OpenAI(api_key=OPENAI_KEY)

def generate_program(goal, weight, height):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"Ты профессиональный фитнес тренер"},
            {"role":"user","content":f"Цель {goal}, вес {weight}, рост {height}. Сделай программу тренировок"}
        ]
    )

    return response.choices[0].message.content
