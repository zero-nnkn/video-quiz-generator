def strip_response(response):
    """
    Remove the opening and ending sentence from the LLM service responses.
    """
    lines = response.strip().split('\n')
    if len(lines) > 2:
        result = '\n'.join(lines[1:-1])
    else:
        result = '\n'.join(lines[:])
    return result
