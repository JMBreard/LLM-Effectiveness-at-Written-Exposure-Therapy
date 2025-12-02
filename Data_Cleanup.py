import copy
import json 

def data_cleanup(file):
    
    filename = copy.deepcopy(file)
    
    convo = filename.get('full_conversation')
    client = ""
    
    for entry in convo:
        if entry[0] == 'T':
            continue
        text_body = entry.split(':', 1)
        client += text_body[1]
        
    return client

if __name__ == '__main__':
    
    directory = 'C:/Users/vijmb/OneDrive/Desktop/2025 Fall/CS312 AI Ethics/Assignments/Final Project/Dataset/ThousandVoicesOfTrauma/ThousandVoicesOfTrauma/conversations'
    
    for client_num in range(1, 500):
        
        filename = f'/{client_num}_P10_conversation.json'
        
        with open(directory + filename, 'r') as file:
            clean_file = json.load(file)
        sim_client_writing = data_cleanup(clean_file)
            
        output_directory = 'C:/Users/vijmb/OneDrive/Desktop/2025 Fall/CS312 AI Ethics/Assignments/Final Project/Simulated Client Writing'
        output_filename = f'{client_num}_simulated_writing_entry.json'
        
        output_data_for_scoring = {
            "filename" : output_filename,
            "client_dialogue" : sim_client_writing
        }
        
        with open(output_directory + f'/{output_filename}', 'w') as output_file:
            json.dump(output_data_for_scoring, output_file)
            
        print(f"Successfully processed and saved to: {output_directory + f'/{output_filename}'}")            
