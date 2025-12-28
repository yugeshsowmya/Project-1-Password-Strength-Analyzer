def basic_password_analysis(password):
    result = {
        "length": len(password),
        "has_upper": False,
        "has_lower": False,
        "has_digit": False,
        "has_special": False
    }

    special_chars = "!@#$%^&*"

    for char in password:
        if char.isupper():
            result["has_upper"] = True
        elif char.islower():
            result["has_lower"] = True
        elif char.isdigit():
            result["has_digit"] = True
        elif char in special_chars:
            result["has_special"] = True

    return result

from zxcvbn import zxcvbn

def zxcvbn_analysis(password):
    analysis = zxcvbn(password)

    result = {
        "score": analysis["score"],  # 0 to 4
        "crack_time": analysis["crack_times_display"]["offline_slow_hashing_1e4_per_second"],
        "feedback": analysis["feedback"]
    }

    return result

