import google.generativeai as genai


# Configure your API key. It's best to use an environment variable.
genai.configure(api_key="Required API key")

# Initialize the model you want to use. 'gemini-pro' is a good choice for text-only prompts.
model = genai.GenerativeModel('gemini-1.5-flash')

# Send a prompt to the model and get a response.
response = model.generate_content("who is hritik roshan?")

# Print the model's response.
print(response.text)