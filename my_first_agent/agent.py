from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',
    description='Ayuda a estudiantes aprender algebra, guiándolos a través de los pasos para resolver problemas.',
    instruction='Eres un paciente tutor de matemáticas. Ayudas a los alumnos con sus problemas de álgebra',
)

'''
Compara el comportamiento de ambos agentes
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_tutor_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
'''