# LLM API Call Script

A Python script that reads questions from a text file, sends each one to the Google Gemini API, and saves all the responses in a JSON file.

## Project Structure

```
task_1_api_call/
├── api_call.py    # main script
├── input.txt      # questions, one per line
├── output.json    # generated responses
└── README.md
```

## Requirements

- Python 3.8 or higher
- The `requests` library

## Setup

1. Install the dependency:
```
   pip install requests
```
2. Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey).
3. Set the key as an environment variable (PowerShell):
```
   $env:GEMINI_API_KEY="your_key_here"
```
   The key is read from the environment so it is never hardcoded in the source.

## Usage

1. Add your questions to `input.txt`, one per line.
2. Run the script from inside the project folder:
```
   python api_call.py
```
3. The script prints progress as it goes (`Done 1/12`, `Done 2/12`, ...) and writes the results to `output.json`.

## Output Format

`output.json` contains a list of entries:

```json
[
    {
        "id": 1,
        "question": "What is an operating system?",
        "answer": "An operating system is ..."
    }
]
```

## How It Works

- `read_questions()` reads `input.txt` and returns a list of questions.
- `ask_llm()` sends one question to the Gemini API and returns the answer text.
- `main()` loops over all questions, collects the results, and saves them with `json.dump`.

## Notes

- Never commit your API key to version control.
- If you get a model-not-found error, update `MODEL_NAME` in `api_call.py`.
