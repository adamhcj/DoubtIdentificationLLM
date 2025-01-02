# ❓ Doubt Identification using LLMs
In reflective learning, students write reflections which could possibly contain doubts. While there exists automated doubt identification models, there lacks utilization of LLMs for such tasks. <br><br>
Majority voting of LLMs had been shown to be effective in identifying doubts within students' reflections. This repository provides a simple implementation of majority voting of multiple LLMs. <br><br>
LangChain is used to abstract model calling, enabling seamless integration of models from many providers such as OpenAI, Anthropic, and more.

# 🖼 Preview
![image](https://github.com/user-attachments/assets/3234bf2f-7d4d-4004-bcce-0ed9fde3731a)

# 💻 Setup
Python environment used: <br>
Python 3.12.1 <br>
A python virtual environment is recommended to ensure no conflicting python packages used. https://docs.python.org/3/library/venv.html
<br>
1. ```pip install -r requirements.txt```
2. ```python main.py```
3. Enter student's reflection
4. Observe output of LLMs, whether the reflection contains doubt or not.

# 🔧 Prompt Configuration
![prompt2](https://github.com/user-attachments/assets/4763f3f0-73ce-4d38-80d2-7379840e027a)

# ➡️ Future Developments
Input of students' reflections is currently through the Python input() function. This can be further expanded to extract reflections from a text source, or integrated into a learning system pipeline to automatically filter students' reflections which contain doubt.
