from Substract import Substract
from Chocolate import Chocolate
from SubstractLimited import SubstractLimited
from Nim import Nim
from ForceNim import ForceNim
import sys
import os
import traceback

def main():
    try:
        max_stack = [5,5,5,5,5]
        to_move = 2
        sys.setrecursionlimit(50000)
        nim = ForceNim(max_stack, to_move)
        nim.reach(tuple(max_stack))
        p_s = nim.p_states
        filename = f"ForceNim-{max_stack}-{to_move}.csv"
        print(f"Saving to {filename}")
        with open(filename, 'w') as f:
            for p in p_s:
                for i in p[:-1]:
                    f.write(f"{i},")
                f.write(f"{p[-1]}\n")
    except Exception as e:
        traceback.print_exc()
    # slim = SubstractLimited()
    # slim.reach((31,4,4,4,4,4,4))
    # p_s = sorted(slim.p_states)
    # n_s = sorted(slim.n_states)
    # print(f"P: {p_s}")
    # print(f"N: {n_s}")
    # start_state = int(sys.argv[1])
    # allowed_set = {int(x) for x in sys.argv[2:]}
    # substract = Substract(allowed_set)
    # substract.reach(start_state)
    # p_s = sorted(substract.p_states)
    # n_s = sorted(substract.n_states)
    # print(f"P: {p_s}")
    # print(f"N: {n_s}")
    # chocolate = Chocolate(2, 2)
    # chocolate.reach(chocolate.get_start_state())
    # p_s = chocolate.p_states
    # n_s = chocolate.n_states
    # print(f"P: {p_s}")
    # print(f"N: {n_s}")

if __name__ == "__main__":
    main()