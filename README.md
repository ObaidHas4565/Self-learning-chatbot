# Self-learning-chatbot
A chatbot that learns from user interactions by dynamically updating its knowledge base based on user input.

## Files 

 • Jarvis.py — main chatbot script

 • KnowledgeBase.json — stored questions, variations and answers

## How it works

1. Loads KnowledgeBase.json into memory.

2. Uses difflib.get_close_matches to find close matches (also checks entries in variations).

3. If a match is found, returns the stored answer.

4. If not, Jarvis prompts you to teach it; a user-provided answer (not skip) is appended to the JSON and saved.

## Quick start (PyCharm)
1. Open the project folder in Pycharm

2. Right-click on Jarvis.py and click run.

3. Interact in the Run console. Type quit to exit the program

## Notes & limitations
 • Simple fuzzy matching — suitable for small datasets; not a full NLP solution.

 • No moderation for user-submitted content — add validation or an approval step before using in production.

 • Built as an educational bachelor project; intended to demonstrate persistence, matching, and a teachable loop.
