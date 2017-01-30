assignments = []

def cross(a, b):
    # Cross product of elements in A and elements in B
    return [s+t for s in a for t in b]

# set out the constraints of rows, colums, peers and diagonals
rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units

# adding two diagonals to unitlist
unitlist.append([c[0]+c[1] for c in zip(rows, cols)])
unitlist.append([c[0]+c[1] for c in zip(rows, cols[::-1])])

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    naked_twins= []

    for unit in unitlist:
        potential_twins = [box for box in unit if len(values[box])==2]
        # check to see if digits are shared by both twin boxes
        if len(potential_twins) == 2:
            if values[potential_twins[0]] == values[potential_twins[1]]:
                naked_twins = values[potential_twins[0]]
                # Find peer squares in 3 x 3 groupings 
                relevant_peers = []
                for box in unit:
                    if (box != potential_twins[0]) & (box != potential_twins[1]):
                        relevant_peers.append(box)
                # delete matching digits from relevant boxes
                for peer in relevant_peers:
                    for digit in values[peer]:
                        if (digit == naked_twins[0]) or (digit == naked_twins[1]):
                            values[peer] = values[peer].replace(digit,'')
    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print

def eliminate(values):
    # delete solved values from other peer boxes 
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):
    # find single box in unit which can allow a certain digit
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            #assign to necessary box
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        # check how many boxes have determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # use eliminate, only_choice, naked_twins
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        # check how many boxes have determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # if no new values added, stop the loop
        stalled = solved_values_before == solved_values_after
        # return False if there is a box with zero available value
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False

    if all(len(values[s]) == 1 for s in boxes):
        return values

    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for values in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    diagonal_sudoku_funtime = search(grid_values(grid))
    return diagonal_sudoku_funtime

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
