cache = {}

def get_cache(question):
    return cache.get(question)

def set_cache(question, result):
    cache[question] = result