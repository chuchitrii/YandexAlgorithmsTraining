def func():
    def are_sides_alike(p1, p2, p3, p4):
        return p1[0] - p2[0] == p3[0] - p4[0] and p1[1] - p2[1] == p3[1] - p4[1] or p1[0] - p2[0] == p4[0] - p3[0] and p1[1] - p2[1] == p4[1] - p3[1]
    
    with open('input.txt', 'r') as f:
        N = int(f.readline().strip())
        result = []
        for i in range(N):
            points = list(map(int, f.readline().strip().split()))
            points = [[points[i], points[i + 1]] for i in range(0, 8, 2)]
            if are_sides_alike(points[0], points[1], points[2], points[3]) or are_sides_alike(points[0], points[2], points[1], points[3]):
                result.append('YES')
            else:
                result.append('NO')

    with open('output.txt', 'w') as f:
        f.write('\n'.join(result))

if __name__ == '__main__':
    func()