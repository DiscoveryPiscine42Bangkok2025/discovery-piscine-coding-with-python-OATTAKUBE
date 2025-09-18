PIECES = {"K", "Q", "R", "B", "P"} # กำหนดหมาก

def setBoard(board: str) -> list[list[str]]: # ทำเป็นตาราง 2 มิติ + เช็คเงื่อนไข input N*N
    lines = []
    for row in board.splitlines(): # รับแมพมาแล้วตัดแมพตามบรรทัด 
        if row.strip() != "":
            lines.append(row)
    if not lines:
        raise ValueError("Empty board, please input square board (NxN).")
    n = len(lines)
    error = False
    for row in lines:
        if len(row) != n:
            error = True
            break
    if error:
        raise ValueError("Board must be square (NxN).")
    grid = []
    for row in lines:
        grid.append(list(row))
    print(grid)
    return grid
  
def findKing(grid: list[list[str]]) -> tuple[int, int]: # หาตำแหน่งคิง + เช็คคิง
    positions = []                  
    for r, row in enumerate(grid):         # enumerate ทำงานแบบหา index และเอา value เอง index นั่นมาด้วย  
        for c, ch in enumerate(row):      
            if ch == "K":                
                positions.append((r, c))   # เก็บพิกัด (r, c)

    if len(positions) != 1:
        raise ValueError("Board must contain exactly one King")
    print("King at: ",positions)
    return positions[0] 

def check_boundary(r: int, c: int, n: int) -> bool: # เช็คขอบเขตกระดานตอนหมากเดิน
    return 0 <= r < n and 0 <= c < n

def check_pawn(grid: list[list[str]], kr: int, kc: int) -> bool: # กำหนดการเดินของ P ดูว่าสามารถ checkmate king ได้ไหม
    n = len(grid)
    for r, c in [(kr + 1, kc - 1), (kr + 1, kc + 1)]:
        if check_boundary(r, c, n) and grid[r][c] == "P":
            return True
    return False

def check_RQB(grid: list[list[str]], kr: int, kc: int) -> bool: # กำหนดการเดินของ RQB ดูว่าสามารถ checkmate king ได้ไหม
    n = len(grid)

    # แนวตรง (R, Q) 
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        r, c = kr + dr, kc + dc
        while check_boundary(r, c, n):
            ch = grid[r][c]
            if ch in PIECES:
                return ch in {"R", "Q"}
            r += dr
            c += dc

    # แนวทแยง (B, Q)
    for dr, dc in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        r, c = kr + dr, kc + dc
        while check_boundary(r, c, n):
            ch = grid[r][c]
            if ch in PIECES:
                return ch in {"B", "Q"}
            r += dr
            c += dc

    return False

def checkmate(board: str) -> None: 
    try:
        grid = setBoard(board)
        kr, kc = findKing(grid)

        in_check = check_pawn(grid, kr, kc) or check_RQB(grid, kr, kc)
        print("Success" if in_check else "Fail")
    except Exception:
        print("Error")