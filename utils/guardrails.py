from langchain_core.prompts import PromptTemplate
from utils.config import llm  # uses Gemini
from prompts.prompt import input_guardrail_template, output_guardrail_template

# --- Guardrail Functions ---
def is_safe_input(query: str) -> bool:
    """Check if user input is safe using an LLM prompt-based moderation."""
    prompt = input_guardrail_template.format(query=query)
    result = llm.invoke(prompt)
    return "safe" in result.content.lower()

def is_safe_output(output: str) -> bool:
    """Check if generated output is safe using an LLM prompt-based moderation."""
    prompt = output_guardrail_template.format(output=output)
    result = llm.invoke(prompt)
    return "safe" in result.content.lower()
