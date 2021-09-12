def func():
    with open('input.txt', 'r') as f:
        votes = f.read()
    results = {}
    for vote in votes.strip().split('\n'):
        candidate, count = vote.strip().split(' ')
        if candidate not in results:
            results[candidate] = 0
        results[candidate] += int(count)
    with open('output.txt', 'w') as f:
        f.write('\n'.join([f'{candidate} {count}' for candidate, count in sorted(results.items())]))

if __name__ == '__main__':
    func()