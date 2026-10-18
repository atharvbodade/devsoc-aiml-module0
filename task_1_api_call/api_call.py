import os
import requests
import json

API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_NAME = "gemini-3.8-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.json"

def read_questions(file_path):
    """Read a text file and return a list of the questions in it."""
    questions = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()
            questions.append(cleaned_line)
    return questions

def ask_llm(question):
    """Send one question to the Gemini API and return the answer text."""
    headers = {"Content-Type": "application/json", "x-goog-api-key": API_KEY}
    body = {"contents": [{"parts": [{"text": question}]}]}

    response = requests.post(API_URL, headers=headers, json=body)
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]

def main():
    questions = read_questions(INPUT_FILE)
    results = []

    for index, question in enumerate(questions, start=1):
        
        answer = ask_llm(question)
        
        entry = {"id": index , "question" : question, "answer" : answer}
        results.append(entry)
        
        print(f"Done {index}/{len(questions)}")

    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    main()
