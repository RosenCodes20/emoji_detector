import re
some_text = input()
found_emojis = r"::[A-Z]{1}[a-z]{2,}::|\*\*[A-Z]{1}[a-z]{2,}\*\*"
nums = []
find_emoji = re.findall(found_emojis, some_text)
threshold = 1
ascci_value = 0
for letter in some_text:
    find_num = r"\d"
    found_num = re.findall(find_num,letter)
    if found_num:
        for num in found_num:
            threshold *= int(num)
cool_emojis = [emoji for emoji in find_emoji if sum(map(ord, emoji[2:-2])) > threshold]

print(f"Cool threshold: {threshold}")
print(f"{len(find_emoji)} emojis found in the text. The cool ones are:")
for emojies in cool_emojis:
    print(emojies)


