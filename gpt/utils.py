import os
from openai import OpenAI

def interview_startter_templete(field,level):
    starter =f"""Hi, I am a student and I am looking for a job in {field} field. I have a good knowledge of {field} help me practice for my interview in area of {field} consdring my level to be {level} by posing questions one by one and increasing difficulty level, just keep sending questions """
    return starter

def get_ans_review(ans):
    prompt = f"""here is the {ans} score the ans out of 5 in format score=x if score is more than 3.5 ask followup question based on my previous answer else ask a single question on onther topic of the same field"""
    return prompt
def comparison(sample_ans,ans):
    """"rate the following answer and give suggestions for improvement based on the sample answer provided
question write  a mail to hr as a Multilingual interpreter seeking work in business translation

sample answer 
${sample_ans}

Answer
${ans}
"""

client = OpenAI(api_key = os.environ["KEY"] ,organization= os.environ["ORG"] )


def gpt_rep(history):

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=history
    )
    print(history)

    store = dict(dict(dict(response)['choices'][0])["message"])["content"]
    next_question = store.split("\n")[-1].split(":")[-1]
    score = False
    st = False
    for i in store.split("\n"):
        if "score" in i.lower():
    
            pos = i.find("/")
        
            score = i[pos-2:pos+2]
            score = "".join([i for i in score if i.isdigit() or i == "/" ])
        if 'Question' in i:
            st = True
            next_question = i.split(":")[-1]
        # elif st and i.strip() != "" :
        #     next_question += '\n'+i
    print(next_question)
    print(store)
    return next_question,score        
