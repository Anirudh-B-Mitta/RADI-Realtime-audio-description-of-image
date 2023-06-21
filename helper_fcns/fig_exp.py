from helper_fcns.describer import describer
from helper_fcns.bard import ask

def explain_fig(class_selected, hint):
    dig = describer()
    prompt = "Explain the diagram of "+ dig + " with respect to class "+ str(class_selected) + " Hint: " + hint
    answer = ask(prompt)
    return answer
