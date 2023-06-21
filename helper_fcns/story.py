from helper_fcns.describer import describer
from helper_fcns.bard import ask

def story_tell():
    dig = describer()
    prompt = "Tell me a story on " + dig
    answer = ask(prompt)
    return answer
