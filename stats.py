def get_num_words(text):
    split = text.split()
    count = len(split)
    return count



def count_chars(text):
    text = text.lower()
    counts = {}
    for c in text:
        counts[c] = counts.get(c, 0) + 1
    return counts

def sorted_char_count(count_chars):
    sorted = []
    for char, num in count_chars.items():
        if char.isalpha():
            item = {"char": char, "num": num}
            sorted.append(item)
    def sort_on(item):
        return item["num"]
    sorted.sort(reverse=True, key=sort_on)
    return sorted
