





def replay(txt_user):
    user_message = str(txt_user).lower()

    if user_message in ("good morning", "good morning!","hi", "hi!", "yo", "good evening", "good evening",):
        return "Heyyy! How's it going?"
    
    if user_message in ("who are you", "who are you?", "who you are", "who you are?", "what is you'r name", "what is you'r name?",
    "what is your name", "what is your name?"):
        return "I am suuiiiii ^o^ bot ^_*"
    
    if user_message in("how are you","how are you?","what's up","what's up?","whats up","whats up?", "what's new?","what's new",
    "how are you doing?", "how are you doing", "how have you been?", "how have you been", "how's everything?", "how is everything?",
    "how's everything", "how is everything"):
        return "nothing much 🤖"
    
    if user_message in ("what you do", "what you do?", "what's your purpose","what's your purpose?", "what do you do", "what do you do?"):
        return "Just a 🤖 trying to help you)"

    return "Sorry buddy, I don't understand you😕. "