message = input('>\t')

emoji = {
    "morning": "😇",
    "happy": "😀",
    "sad": "😔",
    "fun": "😎",
    "driving": "🚗",
}
result = ""
y = message.split(" ")
for x in y:
    # if x in emoji:
    result += emoji.get(x, x) + " "
print(result)

