from prompts.prompt import prompt_template
from utils.config import llm


# 🔗 Chain
chain = prompt_template | llm

# 🚀 Generator Function
def generate_answer(question: str, context: str) -> str:
    try:
        prompt = prompt_template.format(question=question, context=context)
        return llm.invoke(prompt).content

    except Exception as e:
        print("⚠️ LLM failed. Returning fallback message.")
        return "I'm sorry, something went wrong while generating a response. Please try again."

