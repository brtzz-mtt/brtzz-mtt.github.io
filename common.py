def text_decorate(text: str,
    type: str = 'bold'
) -> str:
    if type == 'bold':
        text = '\033[1m' + text + '\033[0m'
    elif type == 'error':
        text = '\033[91m' + text + '\033[0m'
    elif type == 'ok':
        text = '\033[92m' + text + '\033[0m'
    elif type == 'warn':
        text = '\033[93m' + text + '\033[0m'
    elif type == 'underline':
        text = '\033[4m' + text + '\033[0m'
    return text
