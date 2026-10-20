# Part 1 - a menu-driven text interface (TUI) for a simple "piggy bank".
#
# This is a terminal program: it shows a menu, reads a choice, does something, and
# loops until the user quits. The menu loop is written for you - fill in the three
# TODO branches. Keep the exact wording shown (the tests look for it).

import time

def main():
    balance = 0.0
    while True:
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Balance")
        print("4) Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            depAmount = input("Deposit Amount: ").strip()
            balance += float(depAmount)
            print(f"New Balance: {balance: .2f}")
            time.sleep(1)
        elif choice == "2":
           withAmount = input("Withdrawl Amount: ").strip()
           if float(withAmount) > balance:
               print("Insufficient funds")
               time.sleep(1)
               continue
           balance -= float(withAmount)
           print(f"New Balance: {balance: .2f}")
           time.sleep(1)
        elif choice == "3":
            print(f"Current Balance: {balance: .2f}")
            time.sleep(1)
        elif choice == "4":
            print("Goodbye")
            time.sleep(1)
            break
        else:
            print("Invalid choice")
            time.sleep(1)


if __name__ == "__main__":
    main()
