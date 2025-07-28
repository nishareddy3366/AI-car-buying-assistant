# Paste your API key here
api_key = "AIzaSyC6_BxvOzwB24K2tj7c70CHr220kpnswjY"

from google import genai

client = genai.Client(api_key = api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
