# Password strength rules:
# minimum length: 12 characters
# at least two uppercase letters
# at least four lowercase letters
# at least three numbers
# at least three special characters
# can't be a common password


import string
import pwnedpasswords

def check_password_rules(password):
    """ Returns a dictionary with rule checks (True/False) """
    return{
        'length_ok': len(password) >= 12,
        'uppercase_ok': sum(1 for c in password if c.isupper()) >= 2,
        'lowercase_ok': sum(1 for c in password if c.islower()) >= 4,
        'digit_ok': sum(1 for c in password if c.isdigit()) >= 3,
        'special_ok': sum(1 for c in password if c in string.punctuation) >= 3,
    }

def check_breach(password):
    """ Check if the password has been found in data breach """
    breach_count = pwnedpasswords.check(password)
    return breach_count

def score_password(rules, breached):
    """ Calculate score and generate feedback """
    score = 0
    feedback = []

    if rules['length_ok']:
        score += 1
    else:
        feedback.append('Password must be at least 12 characters long.')

    if rules['uppercase_ok']:
        score += 1
    else:
        feedback.append('Use at least 2 uppercase letters.')

    if rules['lowercase_ok']:
        score += 1
    else:
        feedback.append('Use at least 4 lowercase letters.')

    if rules['digit_ok']:
        score += 1
    else:
        feedback.append('Include at least 3 numbers. ')

    if rules['special_ok']:
        score += 1
    else:
        feedback.append('Include at least 3 special characters.')

    if breached:
        feedback.append('This password has been leaked in real data breaches. Choose something more unique.')

    return score, feedback

def show_strength(score):
    """ Prints password strength """
    print('\nPassword Strength: ', end=' ')
    if score == 5:
        print('STRONG')
    elif score >= 3:
        print('MODERATE')
    else:
        print('WEAK')

def password_checker():
    """ Main Loop """
    print('\nWelcome to Password Strength & Security Checker\n')

    while True:
        password = input('Enter a password: ').strip()

        rules = check_password_rules(password)
        breach_count = check_breach(password)
        breached = breach_count > 0

        if breached:
            print(f'\nThis password has been found {breach_count} times in real data breaches!')

        score, feedback = score_password(rules, breached)
        show_strength(score)

        if feedback:
            print('\nSuggestions to improve your password:')
            for f in feedback:
                print(' -', f)

        again = input('\nCheck another password: (y/n): ').lower().strip()
        if again != 'y':
            print('\nThanks for using the Password Strength & Security Checker!')
            break

# Run the program
if __name__ == "__main__":
    password_checker()


