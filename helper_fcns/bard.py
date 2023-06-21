from bardapi import Bard

def ask(prompt):
    res = Bard().get_answer(prompt)
    return(res["content"])