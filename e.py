def e():
    from time import sleep()
    print("What set of multiples would you like to have a list of?")
    exponent = int(input())
    n = 1
    print("n   e")
    while n < 1000000000000000000000000000000000000000:
      e = (1 + 1/n)**n
      sleep(0.25)
      print(n, ":  ", e)
      n += exponent
    print("Calculation of e as a limit completed.")
