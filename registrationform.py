import csv
import os
import re
import tkinter as tk
from tkinter import ttk, messagebox

STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry",
]

CSV_FILE = "candidates.csv"


class CandidateForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Candidate Registration Form")
        self.geometry("460x520")
        self.resizable(False, False)

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="Candidate Registration",
                  font=("Segoe UI", 15, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

        self.name_var = tk.StringVar()
        self.mobile_var = tk.StringVar()
        self.state_var = tk.StringVar()
        self.district_var = tk.StringVar()
        self.taluka_var = tk.StringVar()
        self.pincode_var = tk.StringVar()

        self._add_row(frame, 1, "Full Name *", ttk.Entry(frame, textvariable=self.name_var))
        self._add_row(frame, 2, "Mobile Number *", ttk.Entry(frame, textvariable=self.mobile_var))
        self._add_row(frame, 3, "State *", ttk.Combobox(frame, textvariable=self.state_var,
                                                       values=STATES, state="readonly"))
        self._add_row(frame, 4, "District *", ttk.Entry(frame, textvariable=self.district_var))
        self._add_row(frame, 5, "Taluka *", ttk.Entry(frame, textvariable=self.taluka_var))

        self.address_text = tk.Text(frame, height=4, width=28, wrap="word")
        self._add_row(frame, 6, "Address *", self.address_text)

        self._add_row(frame, 7, "Pincode *", ttk.Entry(frame, textvariable=self.pincode_var))

        ttk.Button(frame, text="Submit", command=self.submit).grid(
            row=8, column=0, columnspan=2, pady=20, ipadx=20, ipady=4)

    @staticmethod
    def _add_row(parent, row, label, widget):
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="nw", pady=6, padx=(0, 10))
        widget.grid(row=row, column=1, sticky="ew", pady=6)

    def validate(self):
        errors = []
        name = self.name_var.get().strip()
        mobile = self.mobile_var.get().strip()
        state = self.state_var.get().strip()
        district = self.district_var.get().strip()
        taluka = self.taluka_var.get().strip()
        address = self.address_text.get("1.0", "end").strip()
        pincode = self.pincode_var.get().strip()

        if not name:
            errors.append("Full name is required.")
        elif not re.fullmatch(r"[A-Za-z][A-Za-z .'-]{2,}", name):
            errors.append("Enter a valid full name (letters only, min 3 characters).")

        if not mobile:
            errors.append("Mobile number is required.")
        elif not re.fullmatch(r"[6-9]\d{9}", mobile):
            errors.append("Mobile number must be 10 digits and start with 6, 7, 8 or 9.")

        if not state:
            errors.append("Please select a state.")
        if not district:
            errors.append("District is required.")
        if not taluka:
            errors.append("Taluka is required.")

        if not address:
            errors.append("Address is required.")
        elif len(address) < 10:
            errors.append("Address is too short (min 10 characters).")

        if not pincode:
            errors.append("Pincode is required.")
        elif not re.fullmatch(r"[1-9]\d{5}", pincode):
            errors.append("Pincode must be 6 digits and cannot start with 0.")

        return errors, [name, mobile, state, district, taluka, address, pincode]

    def submit(self):
        errors, data = self.validate()
        if errors:
            messagebox.showerror("Invalid Input", "\n".join(errors))
            return

        new_file = not os.path.exists(CSV_FILE)
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if new_file:
                writer.writerow(["Full Name", "Mobile", "State", "District",
                                 "Taluka", "Address", "Pincode"])
            writer.writerow(data)

        messagebox.showinfo("Success", "Form submitted successfully!")
        self.reset()

    def reset(self):
        for var in (self.name_var, self.mobile_var, self.state_var,
                    self.district_var, self.taluka_var, self.pincode_var):
            var.set("")
        self.address_text.delete("1.0", "end")


if __name__ == "__main__":
    CandidateForm().mainloop()