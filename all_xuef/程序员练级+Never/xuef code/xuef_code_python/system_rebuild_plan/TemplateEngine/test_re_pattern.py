import re

text = "<p>Topics for {{name}}: {% for t in topics %}{{t}}, {% endfor %}</p>"

"""
re.DOTALL
    Make the '.' special character match any character at all, including a newline;
    without this flag, '.' will match anything except a newline.
    Corresponds to the inline flag (?s).
"""
pat = r"({{.*?}}|{%.*?%}|{#.*?#})"
#pat = r"(?s){{.*?}}|{%.*?%}|{#.*?#}"
tokens = re.split(pat, text)

print(tokens)
