# Lexical Analyzer for Mini Programming Language
# Automata / Compiler Construction Project

KEYWORDS = {"if", "else", "while", "return"}
OPERATORS = {"+", "-", "*", "/", "=", "=="}
SYMBOLS = {"(", ")", "{", "}", ";"}


def is_letter(ch):
    return ch.isalpha()


def is_digit(ch):
    return ch.isdigit()


def lexical_analyzer(code):
    tokens = []
    i = 0
    n = len(code)

    while i < n:
        ch = code[i]

        # Ignore whitespace
        if ch.isspace():
            i += 1
            continue

        # ---------- IDENTIFIER or KEYWORD ----------
        if is_letter(ch):
            start = i
            i += 1
            while i < n and (is_letter(code[i]) or is_digit(code[i])):
                i += 1
            word = code[start:i]

            if word in KEYWORDS:
                tokens.append(f"[KEYWORD: {word}]")
            else:
                tokens.append(f"[IDENTIFIER: {word}]")

        # ---------- NUMBER (INTEGER / FLOAT) ----------
        elif is_digit(ch):
            start = i
            has_dot = False
            i += 1

            while i < n and (is_digit(code[i]) or code[i] == "."):
                if code[i] == ".":
                    if has_dot:
                        break
                    has_dot = True
                i += 1

            number = code[start:i]
            tokens.append(f"[NUMBER: {number}]")

        # ---------- OPERATOR ----------
        elif ch == "=":
            if i + 1 < n and code[i + 1] == "=":
                tokens.append("[OPERATOR: ==]")
                i += 2
            else:
                tokens.append("[OPERATOR: =]")
                i += 1

        elif ch in {"+", "-", "*", "/"}:
            tokens.append(f"[OPERATOR: {ch}]")
            i += 1

        # ---------- SPECIAL SYMBOL ----------
        elif ch in SYMBOLS:
            tokens.append(f"[SYMBOL: {ch}]")
            i += 1

        # ---------- UNKNOWN CHARACTER ----------
        else:
            print(f"Unknown character skipped: {ch}")
            i += 1

    return tokens


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    source_code = input("Enter source code:\n")
    print("\nTOKENS:")
    output = lexical_analyzer(source_code)
    for token in output:
        print(token)
