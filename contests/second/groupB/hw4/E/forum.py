def func():
    from operator import itemgetter
    with open('input.txt', encoding="utf8", mode='r') as f:
        messages: list[str] = [int(f.readline().strip())]
        topics: dict[str, int] = {}
        for i in range(1, messages[0] + 1):
            link = int(f.readline().strip())
            if link == 0:
                topic = f.readline().strip()
                topics[topic] = 1
                messages.append(topic)
            else:
                topics[messages[link]] += 1
                messages.append(messages[link])
            f.readline()
    
    with open('output.txt', encoding="utf8", mode='w') as f:
        f.write(max(topics.items(), key=itemgetter(1))[0])

if __name__ == '__main__':
    func()