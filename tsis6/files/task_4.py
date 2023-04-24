txtfile = input("write the path to the file:\n")

f = open(txtfile, "r")

print(len(f.readlines()))

f.close()