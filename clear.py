import json

def clear_names_in_file(input_filepath, output_filepath):
    try:
        # Read the JSON data from the input file
        with open(input_filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        # Iterate through the dictionary and replace the values
        for username, user_data in data.items():
            if isinstance(user_data, dict):
                if 'f_name' in user_data:
                    user_data['f_name'] = ""
                if 'l_name' in user_data:
                    user_data['l_name'] = ""
                    
        # Write the updated data to the output file
        with open(output_filepath, 'w', encoding='utf-8') as file:
            # indent=4 makes the output file easy to read
            # ensure_ascii=False keeps Thai/Unicode characters intact
            json.dump(data, file, indent=4, ensure_ascii=False)
            
        print(f"Success! The updated data has been saved to {output_filepath}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filepath}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{input_filepath}' does not contain valid JSON.")

# --- How to use it ---
# 1. Save your string format inside a file named 'data.json'
# 2. Run this function
clear_names_in_file('users/index.html', 'users/index.html')