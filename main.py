from Substract import Substract
import sys
import os

def main():
    start_state = int(sys.argv[1])
    allowed_set = {int(x) for x in sys.argv[2:]}
    substract = Substract(allowed_set)
    substract.reach(start_state)
    p_s = sorted(substract.p_states)
    n_s = sorted(substract.n_states)
    print(f"P: {p_s}")
    print(f"N: {n_s}")

if __name__ == "__main__":
    main()