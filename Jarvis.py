import json
from typing import Union
from difflib import get_close_matches

def load_knowledge_base(filepath: str) -> dict:
    with open(filepath, 'r') as file:
        data: dict = json.load(file)
        return data

def save_knowledge_base(filepath: str, data:dict):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_matches(user_question: str, questions: list[str] ) -> Union[str, None]:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> Union[str, None]:
    for q in knowledge_base["questions"]:
        if q["user_question"] == question:
            return q["answer"]

def chatbot():
    knowledge_base: dict = load_knowledge_base("KnowledgeBase.json")

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == "quit":
            break

        best_match: Union[str, None] = find_best_matches(user_input, [q["user_question"] for q in knowledge_base["questions"]])
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Jarvis: {answer}")

        else:
            found_variation = False
            for q in knowledge_base["questions"]:
                if user_input == q["user_question"] or user_input in q.get("variations", []):
                    answer = q["answer"]
                    print(f"Jarvis: {answer}")
                    found_variation = True
            if not found_variation:
                print("I don't know the answer, can you teach me sir?")
                new_answer: str = input('Type the answer or "skip" to skip:')
                if new_answer.lower() != 'skip':
                    knowledge_base["questions"].append({"user_question": user_input, "answer": new_answer})
                    save_knowledge_base("KnowledgeBase.json", knowledge_base)
                    print("Thank you sir, adding the new data to my memory banks.")
                else:
                    print("Understood sir, tell me when you have free time, in the meantime ask me any other questions.")

if __name__ == "__main__":
    chatbot()



