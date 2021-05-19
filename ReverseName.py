def reverse(fname,lname):
    print(f"First Name:{fname}\nLast Name:{lname}")
    print("---------------reverse------------------ ")
    print(f"{lname}"+"   "+f"{fname}")
def main():
    fname = input("Please enter your First Name:")
    lname = input("Please enter your Last Name:")
    reverse(fname, lname)
main()