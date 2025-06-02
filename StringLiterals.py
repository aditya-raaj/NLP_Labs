# Program: Demonstrate String Literals vs Raw Strings in Python

# Normal string with escape sequences
print("Normal String with Escape Sequences:")
normal_string = "This is a line.\nThis is a new line.\tThis is a tabbed line."
print(normal_string)

# Explanation:
# \n creates a new line
# \t adds a tab space
print("-" * 50)

# Raw string where escape sequences are NOT interpreted
print("Raw String (Escape characters are printed as-is):")
raw_string = r"This is a line.\nThis is a new line.\tThis is a tabbed line."
print(raw_string)

# Explanation:
# r"" tells Python to treat backslashes as literal characters
# So \n and \t appear exactly as \n and \t in output

print("-" * 50)

# Example: File path in Windows (with and without raw string)
print("Windows File Path Examples:")

# Normal string (may cause unintended behavior)
path_normal = "C:\newfolder\docs"
print("Normal String Path:", path_normal)

# Explanation:
# \n is interpreted as newline → causes formatting issues

# Raw string (recommended for file paths)
path_raw = r"C:\newfolder\docs"
print("Raw String Path   :", path_raw)

# Explanation:
# Raw strings preserve the full path, avoiding unintended escapes

print("-" * 50)

# Example: Regex pattern with and without raw string
print("Regular Expression Pattern Examples:")

# Normal string - has to escape the backslash again
pattern_normal = "[a-zA-Z0-9\\.]+@gmail\\.com"
print("Normal String Regex Pattern:", pattern_normal)

# Raw string - no need to double escape backslashes
pattern_raw = r"[a-zA-Z0-9\.]+@gmail\.com"
print("Raw String Regex Pattern   :", pattern_raw)

# Explanation:
# Raw strings simplify regex patterns — more readable and accurate
