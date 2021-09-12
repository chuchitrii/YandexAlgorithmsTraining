def func():
    with open('input.txt') as f:
        text = f.read()
    parties = {}
    for partyResults in text.strip().split('\n'):
        [name, votes] = partyResults.rsplit(' ', 1)
        if name not in parties: 
            parties[name] = 0
        parties[name] += int(votes)
    with open('output.txt', 'x') as f:
        f.write('\n'.join[parties])