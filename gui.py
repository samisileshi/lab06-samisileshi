# Part 2 (STRETCH) - a small graphical interface (GUI) with tkinter: a tip calculator.
#
# The window and its widgets are built for you. Write the `calculate` function so that,
# when the button is clicked, it reads the bill amount, works out a 15% tip and the
# total, and shows them in the result label.
#
# There is no automated test for this part (a GUI can't be checked that way) - show it
# to your lab instructor.

import tkinter as tk


def calculateTip():
    try:
        preTipBill = float(entry.get())
        Tip = preTipBill * 0.15
        totalBill = preTipBill + Tip


        result.config(text=f"Tip: ${Tip: .2f} Total: ${totalBill: .2f} Tax : Evaded")
    except ValueError:
        result.config(text="Please enter a correct numerical value!")


def calculateTax():
    try:
        preTipBill = float(entry.get())
        Tip = preTipBill * 0.15
        preTaxtotalBill = preTipBill + Tip
        taxedBill = preTaxtotalBill * 0.13
        postTaxBill = preTaxtotalBill + taxedBill

        result.config(text=f"Tip: ${Tip: .2f} Total: ${postTaxBill: .2f} Tax: ${taxedBill:.2f}")
    except ValueError:
        result.config(text="Please enter a correct numerical value!")


def calculateEvade():
    try:
        goodBill = float(entry.get())

        result.config(text=f"Tip: Evaded! Total: ${goodBill: .2f} Tax: Evaded!")
    except ValueError:
        result.config(text="Please enter a correct numerical value!")


root = tk.Tk()
root.title("Tip Calculator")

tk.Label(root, text="Bill amount:").pack(padx=10, pady=(10, 0))
entry = tk.Entry(root)
entry.pack(padx=10, pady=4)

tk.Button(root, text="Evade Both Tax and Tip", command=calculateEvade).pack(padx=10, pady=4)
tk.Button(root, text="Calculate Ontario tax + tip", command=calculateTax).pack(padx=10, pady=4)
tk.Button(root, text="Calculate 15% tip", command=calculateTip).pack(padx=10, pady=4)

result = tk.Label(root, text="Tip: $0.00   Total: $0.00 Tax: $0.00", font=("Arial", 12))
result.pack(padx=10, pady=10)

root.mainloop()
