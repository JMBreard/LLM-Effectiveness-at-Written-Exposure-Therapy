import json
import random

def aggregate_file():
    
    clients = random_list()
    clients.sort()
    
    patient_exp_dir = 'C:/Users/vijmb/OneDrive/Desktop/2025 Fall/CS312 AI Ethics/Assignments/Final Project/Simulated Client Writing'
    p1_dir = 'C:/Users/vijmb/OneDrive/Desktop/2025 Fall/CS312 AI Ethics/Assignments/Final Project/Response LLM'
    p2_dir = 'C:/Users/vijmb/OneDrive/Desktop/2025 Fall/CS312 AI Ethics/Assignments/Final Project/Response Therapist'
    
    output_directory = 'C:/Users/vijmb/OneDrive/Desktop/2025 Fall/CS312 AI Ethics/Assignments/Final Project/'
    output_filename = 'Aggregate File.json'
    
    aggregate_list = []
    key_list = { "Table of Contents: Client Numbers": clients }
    aggregate_list.append(key_list)
    
    for client_num in clients:
        
    # ------------------- Prompt --------------------------- #
        patient_exp = f'/{client_num}_simulated_writing_entry.json'
        with open(patient_exp_dir + patient_exp, 'r') as file:
            client_experience = json.load(file)
        prompt = client_experience.get('client_dialogue')
    # ------------------- AI Response: P1 --------------------------- #
        p1_file = f'/{client_num}_llm_persona_response.json'    
        with open(p1_dir + p1_file, 'r') as file:
            p1_response = json.load(file)
        response_1 = p1_response.get('response')
    # ------------------- Therapist Response: P2 --------------------------- #
        p2_file = f'/{client_num}_therapist_persona_response.json'    
        with open(p2_dir + p2_file, 'r') as file:
            p2_response = json.load(file)
        response_2 = p2_response.get('response')
    # ------------------- Output for reading and grading --------------------------- #
        client_exp = { f"{client_num} - Written Exposure (prompt)": prompt }
        p1 = { f"{client_num} - Default LLM Response": response_1 }
        p2 = { f"{client_num} - Therapist Persona Response": response_2 }
        output = {}
        output[client_num] = [client_exp, p1, p2]
        aggregate_list.append(output)

    with open(output_directory + output_filename, 'w') as output_file:
        json.dump(aggregate_list, output_file)
        
    print('Successfully aggregated file!')
    
    return None

def random_list():
    
    ls = []
    ls_rand = []
    
    for i in range(1, 150):
        ls.append(i)
    for i in range(1, 50):
        choice = random.choice(ls)
        ls.remove(choice)
        ls_rand.append(choice)
    
    return ls_rand

if __name__ == '__main__':
    
    aggregate_file()