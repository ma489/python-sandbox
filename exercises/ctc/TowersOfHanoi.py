# Towers of Hanoi puzzle


def solve_hanoi(number_of_rings_to_move, pegs, input_peg, target_peg, intermediary_peg):
    if number_of_rings_to_move == 0:
        # print("Nothing to solve")
        return
    #   solve_hanoi(input, intermediary, target) #stash top (n-1) rings
    solve_hanoi(number_of_rings_to_move - 1, pegs, input_peg, intermediary_peg, target_peg)
    #   solve bottom (nth) ring
    bottom_ring = (pegs[input_peg]).pop()
    (pegs[target_peg]).append(bottom_ring)
    print("Move ring %d to peg %d" % (bottom_ring, target_peg+1))
    #   solve_hanoi(intermediary, target, input) #solve top (n-1) rings
    solve_hanoi(number_of_rings_to_move - 1, pegs, intermediary_peg, target_peg, input_peg)


p1 = [1,2,3]
p2 = []
p3 = []
pegs = [p1, p2, p3]

print("Pegs", pegs)
solve_hanoi(3, pegs, 0, 1, 2)
print("Pegs", pegs)