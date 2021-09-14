def func():
    from functools import cmp_to_key
    with open('input.txt', 'r') as f:
        text = f.read()
   
    parties: dict[str, list[int]] = {}
    votesSum = 0
    for partyResults in text.strip().split('\n'):
        [name, votes] = partyResults.rsplit(' ', 1)
        votesSum += int(votes)
        parties[name] = [int(votes)]
    
    firstQuotinent = votesSum / 450 

    def compare(party1, party2):
        _temp1 = party1[1][0] % firstQuotinent
        _temp2 = party2[1][0] % firstQuotinent
        if _temp1 != _temp2:
            return _temp2 - _temp1
        else:
            return party2[1][0] - party1[1][0]

    leftVotes = 450
    for name in parties.keys():
        currentVotes = int(parties[name][0] // firstQuotinent)
        leftVotes -= currentVotes
        parties[name].append(currentVotes)
    
    if leftVotes > 0:
        index = 0
        sortedParties = sorted(parties.items(), key=cmp_to_key(compare))
        while leftVotes > 0:
            parties[sortedParties[index][0]][1] += 1
            leftVotes -= 1
            if index == len(parties) - 1:
                index = 0
            else :
                index += 1            

    with open('output.txt', 'w') as f:
        f.write('\n'.join([f'{party[0]} {party[1][1]}' for party in parties.items()]))

if __name__ == '__main__':
    func()