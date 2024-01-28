import openai

def generate_image(prompt):
    openai.api_key = 'your-api-key-here'

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    return response

# Example usage
prompt = "A futuristic cityscape"
image_response = generate_image(prompt)

print(image_response)
