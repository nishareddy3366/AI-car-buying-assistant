from langchain_core.prompts import PromptTemplate
from config import llm  # uses Gemini
from prompt.prompt import input_guardrail_template, output_guardrail_template

# --- Guardrail Functions ---

def is_safe_input(query: str) -> bool:
    prompt = input_guardrail_template.format(query=query)
    result = llm.invoke(prompt)
    return "safe" in result.content.lower()

def is_safe_output(output: str) -> bool:
    prompt = output_guardrail_template.format(output=output)
    result = llm.invoke(prompt)
    return "safe" in result.content.lower()
