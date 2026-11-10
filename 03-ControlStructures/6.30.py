for row in range(1, 8):
    for col in range(7):
        num = row + col * 7
        print(f"{num:2d}", end=" ")
    print()
