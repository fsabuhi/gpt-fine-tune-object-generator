import json
def system_data(text):
    return {"role": "system", "content": text}

def prompt_situation(question,answer):
    return {"role": "user", "content": question}, {"role": "assistant", "content": answer}

input('Hello, Welcome to GPT-3.5 fine-tuner. Press Enter to Continue')

print('If you do not enter asked data it will be set to default parameters by GPT')
bot_name = input('Enter name of the bot: ')
bot_creator = input('Creator of the bot: ')
bot_purpose = input('Purpose of the bot: ')
additional_data = input('Write additional data')
final_initial_data = ""
final_initial_data += 'Your name is {}. '.format(bot_name) if bot_name else ""
final_initial_data += 'You are created by {}. '.format(bot_creator) if bot_creator else ""
final_initial_data += 'Your purpose is {}. '.format(bot_purpose) if bot_purpose else ""
final_initial_data += 'Additional data: {}. '.format(additional_data) if additional_data else ""
system_data(final_initial_data)

while True:
    question = input('Enter question: ')
    answer = input('Enter answer: ')
    data_to_dump = {"messages":[system_data(final_initial_data),prompt_situation(question,answer)]}
    with open('data.jsonl','a') as f:
        f.write(json.dumps(data_to_dump) + '\n')
    if input('Do you want to continue? (y/n)') == 'n':
        break