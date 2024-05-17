import configparser
configparser.__name__
import json
from difflib import get_close_matches


def load_content(file_path: str)-> dict:
    with open(file_path, 'r') as file:
            data: dict = json.load(file)
    return data

def save_content(file_path:str, data: dict):
    with open(file_path, 'w') as file:
         json.dump(data,file,indent=2)

def find_best_match(user_question: str, questions:list[str])-> str | None:
     matches: list = get_close_matches(user_question,questions, n=1,cutoff=0.7)
     return matches[0] if matches else None

def get_answer_for_question(question:str, content:dict)-> str | None:
     for q in content["Questions"]:
          if q["question"] == question:
               return q["answer"]
          



def chat_bot():
     content: dict= load_content('content.json')

     while True:
          user_input: str = input('You: ')

          if user_input.lower() == 'quit':
               break
          
          best_match: str | None = find_best_match(user_input, [q["question"] for q in content["Questions"]])

          if best_match:
               answer: str = get_answer_for_question(best_match, content)
               print(f"Bot: {answer}")
          else: print('Bot: I do not know the answer. Can you teach me? ')
          new_answer: str = input('Write your answer or "skip" to skip: ')


          if new_answer.lower()!= 'skip':
               content["Questions"].append({"question":user_input, "answer":new_answer})
               save_content("content.json", content)
               print("Bot:Thank you! I have Learned a new response")



if __name__ == '__main__':
      chat_bot()

              
# def integral(n):
#      my_dict= { }
#      for number in range(1,n+1):
#           my_dict[number] = number*number
#      return my_dict

# print(integral(8))
          

          
          

     

        