import re

def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])

def extract_session_id(session_str: str):
    match = re.search(r"sessions\/(.*?)\/contexts", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

if __name__ == "__main__":
    print(get_str_from_food_dict({"apple":2, "oranges": 5}))
    print(extract_session_id("projects/zira-chatbot-for-food-del-icns/agent/sessions/cd85883a-0189-4e30-78d8-300a7abf6ef5/contexts/ongoing-order"))