import os

# Specify the API keys for LLMs
os.environ["OPENAI_API_KEY"] = ""
os.environ["ANTHROPIC_API_KEY"] = ""

# Import necessary langchain classes for the LLMs
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


# Define the models to be used
# models = [ChatOpenAI(model="gpt-4o"), ChatAnthropic(model="claude-3-5-sonnet-20240620")]
models = [ChatOpenAI(model="gpt-4o"), ChatOpenAI(model="gpt-4-turbo"), ChatOpenAI(model="gpt-3.5-turbo")]

system_prompt = '''You are a tutor for students learning a topic. Each student is writing a reflection on his/her learning. Your task is to analyze the reflection to determine if the student expresses doubts on the topic and requires further explanation on the topic.'''

student_reflection = input("Enter the student's reflection: ")

human_prompt = f'''
Here is the student's reflection: {student_reflection}. 
If you detect the student explicitly expressing doubt, output 1. 
If you don't detect the student explicitly expressing doubt, output 0.

Q: I don't understand the Apriori algorithm. 
A: 1, because student explicitly expressed doubt on Apriori algorithm, requiring further explanation on the topic.

Q: Give more examples and spend more time on this topic.
A: 0, because the student is only giving suggestion on improving the learning experience and not explicitly requesting explanation on the topic.

Q: I am interested in learning about a topic. 
A: 0, because student is expressing interests in learning a topic, not explicitly requesting explanation on the topic.

Only reply 0 or 1, no explanation.
'''

result_map = {
    "0": "The student is not expressing doubt.",
    "1": "The student is expressing doubt."
}

model_count = 0
doubt_count = 0

from langchain_core.messages import HumanMessage, SystemMessage

for model in models:
    model_count += 1

    messages = [
        SystemMessage(system_prompt),
        HumanMessage(human_prompt),
    ]

    response = model.invoke(messages).content

    print(f"{model.model_name}: {result_map[response]}")

    if response == "1":
        doubt_count += 1

if doubt_count > model_count / 2:
    print("Majority of the models detected doubt in the student's reflection.")
else:
    print("Majority of the models did not detect doubt in the student's reflection.")