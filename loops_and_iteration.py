def useWhileLoop():
    n=0
    while True:
        line = input('>')
        if line == '#':
            continue
        if line == 'done':
            break
        print(line)
    print('Done!')

useWhileLoop()



