from src.gemini_client import GeminiClient

gemini = GeminiClient()

response = gemini.generate(
    "Who wrote Harry Potter?"
)

print(response)