def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check for uppercase and lowercase characters
    has_upper = False
    has_lower = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
            
    if not has_upper or not has_lower:
        return "Weak: Password must contain both uppercase and lowercase characters."
    
    # Check for digits
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
    
    if not has_digit:
        return "Weak: Password must contain at least one digit."
    
    # Check for special characters
    has_special = False
    special_chars = "!@#$%^&*()-=_+[]{}|;':\"<>,.?/~`"
    for char in password:
        if char in special_chars:
            has_special = True
    
    if not has_special:
        return "Weak: Password must contain at least one special character."
    
    return "Strong: Password is strong."

# Example usage
password = input("Enter password: ")
strength = check_password_strength(password)
print(strength)
