def f(n=1):
    return {
        0: "You typed zero.\n",
        1: "You are in top.\n",
        2: "n is an even number\n"
        }.get(n,  "Only single-digit numbers are allowed\n")


print(f(2))  # ---> n is an even number
