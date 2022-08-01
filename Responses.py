from  random import choice 


def replay(txt_user):

    ##################################### 
    user_message = str(txt_user).lower()

    ch1 = ["Heyyy! How's it going?", "Hi! How are you?", "yooyoo broo! Long time no see👀"] 

    if user_message in ("good morning", "good morning!","hi", "hi!", "yo", "good evening", "good evening",):
        return choice(ch1)
    


   


    if user_message in ("who are you", "who are you?", "who you are", "who you are?", "what is you'r name", "what is you'r name?",
    "what is your name", "what is your name?"):
        return "I am suuiiiii ^ooo^"


    choice3 = ["nothing much 🤖","I feel great 🤖","Trying to imporve myself 🤖","Feeling good 🤖","Happy all the time 🤖","Treying to find meaning in life🤖","I don't know how I am feeling right now 🤖",]
    if user_message in("how are you", "how are u?", "how are u" ,"how are you?","what's up","what's up?","whats up","whats up?", "what's new?","what's new",
                        "how are you doing?", "how are you doing", "how have you been?", "how have you been", "how's everything?", "how is everything?",
                        "how's everything", "how is everything", "what are you doing", "what are you doing?"):
        return choice(choice3)




    ch4 = ["Great!","👍","Be like that always.","I am happy to know that.",] 
    if user_message in ("I am fine","nothin much","good","fine","i am good","still surviving","i am happy","feelig good"):
        return choice(ch4)



    choice5 = ["i am sad","sad","i am alone","alone","i don't know","i am not okay","not okay","bad","feeling bad","just bad","just sad","just alone",]
    if user_message in ("Don't be, I am here always for you🤖","I hope you can feel okay with me","Be patent my friend","I am here if you want toy talk about it","We need to chane that"): 
        return choice(choice5) 


    ch6 = ["Just a 🤖 trying to help you)","Waiting for someone to talk to me 🕥","I'm trying to come up with idea how to destroy the  world 🌏"]  
    if user_message in ("what you do", "what you do?", "what's your purpose","what's your purpose?", "what do you do", "what do you do?"):
        return choice(ch6)

    return "Sorry buddy, I don't understand you😕. "