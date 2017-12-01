def chessBoardCellColor(cell1, cell2):
    d=lambda l:ord(l[0])-ord('A')+int(l[1])
    return d(cell1)%2==d(cell2)%2
