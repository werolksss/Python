moves = 0
def hanoi(n, a, c, b):
    global moves
    if n == 1:
        moves += 1
        print(f"переместить диск 1: {a} -> {c}")
        return
    hanoi(n - 1, a, b, c)
    moves += 1
    print(f"переместить диск {n}: {a} -> {c}")
    hanoi(n - 1, b, c, a)
n = int(input("введите количество дисков: "))
hanoi(n, 'a', 'c', 'b')
print("\nобщее количество перемещений:", moves)
