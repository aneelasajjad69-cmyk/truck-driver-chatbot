# logic.py
import re
from data import BOT_DATA

def get_ai_response(user_query, language_mode="urdu"):
    """
    Evaluates text streams using a local keyword-scoring rule network.
    Operates 100% offline without commercial NLP API calls.
    """
    query = str(user_query).lower().strip()
    query = re.sub(r'[^\w\s]', '', query) # Cleans text data punctuation noise

    if not query:
        return "Please type a valid question." if language_mode == "english" else "Kindly koi valid sawal type karein."

    best_match_key = None
    max_score = 0

    # Iterating over the knowledge layers to score hits
    for key, data_block in BOT_DATA.items():
        score = 0
        for keyword in data_block["keywords"]:
            if keyword in query:
                score += 1
        
        if score > max_score:
            max_score = score
            best_match_key = key

    # Direct response generation loop matching selected key paths
    if best_match_key and max_score > 0:
        return BOT_DATA[best_match_key]["english"] if language_mode == "english" else BOT_DATA[best_match_key]["urdu"]
    
    # Generic Fallback mechanism mapping unrecognized tokens back to standard core fields
    if language_mode == "english":
        return "I could not find a direct answer. Please ask specifically about Sajjad Ahmad's experience, truck type, license details, daily routine, or family members."
    else:
        return "System ko is sawal ka jawab nahi mila. Aap Sajjad Ahmad ke experience, truck specifications, license, routine, ya family members ke baare mein pooch sakte hain."