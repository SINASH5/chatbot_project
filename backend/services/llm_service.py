from transformers import pipeline

# Load the text generation pipeline with an open-source LLM (GPT-2)
generator = pipeline("text-generation", model="gpt2")

def generate_llm_response(user_input):
    try:
        response = generator(user_input, max_length=50, num_return_sequences=1)
        return response[0]["generated_text"]
    except Exception as e:
        return f"Error generating response: {str(e)}"
