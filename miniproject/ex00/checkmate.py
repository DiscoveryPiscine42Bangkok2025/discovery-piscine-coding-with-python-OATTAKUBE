PIECES : {"K" , "Q", "R", "B", "P"}
def _parse_board(board: str) -> list[list[str]]:
    lines = board.splitlines()
    if not lines:
        raise ValueError("Empty board")
    n = len(lines)
    if any(len(row) != n for row in lines):
        raise ValueError("Board must be square (NxN)")
    return [list(row) for row in lines]
  
def _find_king(grid: list[list[str]]) -> tuple[int, int]:
    positions = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "K"]
    if len(positions) != 1:
        raise ValueError("Board must contain exactly one King")
    return positions[0]

def _in_bounds(r: int, c: int, n: int) -> bool:
    return 0 <= r < n and 0 <= c < n

def _checked_by_pawn(grid: list[list[str]], kr: int, kc: int) -> bool:
    n = len(grid)
    for r, c in [(kr + 1, kc - 1), (kr + 1, kc + 1)]:
        if _in_bounds(r, c, n) and grid[r][c] == "P":
            return True
    return False

def _checked_by_sliders(grid: list[list[str]], kr: int, kc: int) -> bool:
    n = len(grid)

    # แนวตรง (R, Q)
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        r, c = kr + dr, kc + dc
        while _in_bounds(r, c, n):
            ch = grid[r][c]
            if ch in PIECES:
                return ch in {"R", "Q"}
            r += dr
            c += dc

    # แนวทแยง (B, Q)
    for dr, dc in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        r, c = kr + dr, kc + dc
        while _in_bounds(r, c, n):
            ch = grid[r][c]
            if ch in PIECES:
                return ch in {"B", "Q"}
            r += dr
            c += dc

    return False

def checkmate(board: str) -> None:
    try:
        grid = _parse_board(board)
        kr, kc = _find_king(grid)

        in_check = _checked_by_pawn(grid, kr, kc) or _checked_by_sliders(grid, kr, kc)
        print("Success" if in_check else "Fail")
    except Exception:
        print("Error")

