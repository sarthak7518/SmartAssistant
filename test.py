import google.generativeai as genai

genai.configure(api_key="AIzaSyDywxXzm5un4tQU1lZPP13-uH5a6yzy0qA")
models = genai.list_models()

for model in models:
    print(model.name)
