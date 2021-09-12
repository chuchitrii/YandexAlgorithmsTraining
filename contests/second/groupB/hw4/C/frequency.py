def func():
    from functools import cmp_to_key

    with open('input.txt', 'r') as f:
        text = f.read()
    dictionary = {}
    
    for word in text.strip().split():
        if word not in dictionary: 
            dictionary[word] = 0
        dictionary[word] += 1

    def compare(item1, item2):
        if item2[1] != item1[1]:
            return item2[1] - item1[1]
        else:
            if item1[0] > item2[0]:
                return 1
            else:
                return - 1

    with open('output.txt', 'w') as f:
        f.write('\n'.join([word for (word, _) in sorted(dictionary.items(), key=cmp_to_key(compare))]))
    
if __name__ == '__main__':
    func()