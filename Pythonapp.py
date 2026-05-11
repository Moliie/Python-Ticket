# movie ticket booking app
# by me lol
# started this for my CS class project, took forever but it works!!
# TODO: maybe add more movies later

import tkinter as tk
from tkinter import ttk
import random

# ok so these are all the movies we can pick from
# i just made up the seat numbers, in real life this would come from a database or something
movies_list = [
    {"key": "A", "title": "How To Train You Dragon", "genre": "Animation", "price": 20, "available_tickets": 50},
    {"key": "B", "title": "Sherk", "genre": "Animation", "price": 15, "available_tickets": 50},
    {"key": "C", "title": "Hotel For Dogs", "genre": "Action", "price": 18, "available_tickets": 25},
    {"key": "D", "title": "The Ring", "genre": "Horror", "price": 18, "available_tickets": 35},
    {"key": "E", "title": "title": "Lord of the Ring", "genre": "High Fantasy & Adventure", "price": 18, "available_tickets": 60},
    {"key": "F", "title": "Your Mine & Ours", "genre": "Romance", "price": 18, "available_tickets": 25},
  

# coupon codes - told my friend about these lmao
# 5%, 10%, 15% off
valid_coupons = {
    "SAVE5": 5,
    "POPCORN10": 10,
    "VIP15": 15,
}

# state taxes - i had to look all of these up, took forever
# some states have 0 tax which is nice
state_taxes = {
    "AL": 0.04, "AK": 0.00, "AZ": 0.056, "AR": 0.065, "CA": 0.0725,
    "CO": 0.029, "CT": 0.0635, "DE": 0.00, "FL": 0.06, "GA": 0.04,
    "HI": 0.04, "ID": 0.06, "IL": 0.0625, "IN": 0.07, "IA": 0.06,
    "KS": 0.065, "KY": 0.06, "LA": 0.0445, "ME": 0.055, "MD": 0.06,
    "MA": 0.0625, "MI": 0.06, "MN": 0.06875, "MS": 0.07, "MO": 0.04225,
    "MT": 0.00, "NE": 0.055, "NV": 0.0685, "NH": 0.00, "NJ": 0.06625,
    "NM": 0.05125, "NY": 0.08625, "NC": 0.0475, "ND": 0.05, "OH": 0.0575,
    "OK": 0.045, "OR": 0.00, "PA": 0.06, "RI": 0.07, "SC": 0.06,
    "SD": 0.045, "TN": 0.07, "TX": 0.0625, "UT": 0.0485, "VT": 0.06,
    "VA": 0.053, "WA": 0.065, "WV": 0.06, "WI": 0.05, "WY": 0.04,
}

# needed the full names too for the dropdown
state_names = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming",
}

# build the dropdown list - format is like "New York (NY)"
dropdown_states = []
for code in sorted(state_names.keys()):
    dropdown_states.append(state_names[code] + " (" + code + ")")

# global variables to keep track of stuff
# yeah i know globals are bad but it was easier lol
chosen_movie = None
num_tickets = 1
chosen_state = ""
coupon_applied = None
coupon_discount_pct = 0

# the main window
window = tk.Tk()
window.title("CineBook - Buy Movie Tickets")
window.geometry("680x660")
window.configure(bg="#f5f5f0")
window.resizable(True, True)

# keeping track of what page we're on
current_page = 1

# this holds whatever is on screen right now
# i clear it and rebuild it when switching pages
main_area = tk.Frame(window, bg="#f5f5f0")
main_area.pack(fill="both", expand=True, padx=20, pady=10)


# helper to wipe the screen
def clear_screen():
    for widget in main_area.winfo_children():
        widget.destroy()


# draws those little step indicators at the top
def draw_steps(active_step):
    # remove old step bar if there is one
    for w in window.winfo_children():
        if hasattr(w, "_is_stepbar"):
            w.destroy()

    step_bar = tk.Frame(window, bg="#f5f5f0")
    step_bar._is_stepbar = True
    step_bar.pack(fill="x", padx=20, pady=(0, 6))

    step_labels = ["1 - Movie", "2 - Seats", "3 - Info", "4 - Review"]

    for i, label in enumerate(step_labels):
        step_num = i + 1
        if step_num == active_step:
            bg = "#dceeff"
            fg = "#1a5fa8"
            font_style = ("Arial", 10, "bold")
        elif step_num < active_step:
            bg = "#f5f5f0"
            fg = "#2a7a2a"
            font_style = ("Arial", 10)
        else:
            bg = "#f5f5f0"
            fg = "#999999"
            font_style = ("Arial", 10)

        lbl = tk.Label(step_bar, text=label, bg=bg, fg=fg,
                       font=font_style, padx=10, pady=5)
        lbl.grid(row=0, column=i, sticky="ew", padx=2)
        step_bar.columnconfigure(i, weight=1)

    # gotta push main_area below the step bar
    main_area.pack_forget()
    main_area.pack(fill="both", expand=True, padx=20, pady=(0, 10))


# -----------------------------------------------
# PAGE 1 - pick a movie
# -----------------------------------------------
def show_page1():
    global current_page
    current_page = 1
    clear_screen()
    draw_steps(1)

    tk.Label(main_area, text="🎬 Pick a Movie", font=("Arial", 15, "bold"),
             bg="#f5f5f0", fg="#1a1a1a").pack(anchor="w", pady=(4, 8))

    # put movies in a scrollable frame because there's a bunch of them
    container = tk.Frame(main_area, bg="#ffffff", relief="solid", bd=1)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container, bg="#ffffff", highlightthickness=0)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    scroll_frame = tk.Frame(canvas, bg="#ffffff")
    canvas_id = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    # make the inner frame resize with the canvas
    def on_canvas_resize(event):
        canvas.itemconfig(canvas_id, width=event.width)
    canvas.bind("<Configure>", on_canvas_resize)

    def update_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    scroll_frame.bind("<Configure>", update_scroll)

    # mousewheel scrolling - found this on stackoverflow
    def scroll_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", scroll_mousewheel)

    # draw each movie as a row
    for movie in movies_list:
        make_movie_row(scroll_frame, movie)

    # hint text
    tk.Label(main_area, text="Tip: press A, B, C etc. on your keyboard to select",
             font=("Arial", 9), bg="#f5f5f0", fg="#aaaaaa").pack(anchor="w", pady=3)

    # next button
    btn_frame = tk.Frame(main_area, bg="#f5f5f0")
    btn_frame.pack(fill="x", pady=(6, 0))

    tk.Button(btn_frame, text="Continue to Seats →",
              bg="#1a5fa8", fg="white", font=("Arial", 11, "bold"),
              relief="flat", padx=20, pady=8, cursor="hand2",
              command=go_to_page2).pack(side="left")

    # keyboard shortcuts for movie selection
    window.bind("<Key>", keyboard_select)


def make_movie_row(parent, movie):
    # figure out seat availability color
    seats = movie["seats"]
    if seats == 0:
        seat_text = "✕ Sold out"
        seat_fg = "#cc2222"
        seat_bg = "#ffecec"
        row_bg = "#fafafa"
        disabled = True
    elif seats <= 5:
        seat_text = f"⚠ Only {seats} left!"
        seat_fg = "#885500"
        seat_bg = "#fff5d6"
        row_bg = "#ffffff"
        disabled = False
    else:
        seat_text = f"✓ {seats} seats open"
        seat_fg = "#1a6b1a"
        seat_bg = "#e8f7e8"
        row_bg = "#ffffff"
        disabled = False

    row = tk.Frame(parent, bg=row_bg, highlightbackground="#dddddd",
                   highlightthickness=1)
    row.pack(fill="x", padx=6, pady=3)

    # the letter badge on the left
    letter_bg = "#dceeff" if not disabled else "#eeeeee"
    letter_fg = "#1a5fa8" if not disabled else "#bbbbbb"
    tk.Label(row, text=movie["key"],
             font=("Arial", 16, "bold"),
             bg=letter_bg, fg=letter_fg,
             width=3, pady=10).pack(side="left")

    # movie info in the middle
    info = tk.Frame(row, bg=row_bg)
    info.pack(side="left", fill="both", expand=True, padx=10, pady=8)

    title_color = "#1a1a1a" if not disabled else "#aaaaaa"
    tk.Label(info, text=movie["title"],
             font=("Arial", 12, "bold"),
             bg=row_bg, fg=title_color, anchor="w").pack(fill="x")

    meta = movie["genre"] + "  ·  " + movie["time"] + "  ·  $" + str(movie["price"])
    tk.Label(info, text=meta,
             font=("Arial", 10),
             bg=row_bg, fg="#888888", anchor="w").pack(fill="x")

    # seat badge
    tk.Label(info, text=seat_text, bg=seat_bg, fg=seat_fg,
             font=("Arial", 9), padx=5, pady=2).pack(anchor="w", pady=(3, 0))

    # click to select (only if not sold out)
    if not disabled:
        row.bind("<Button-1>", lambda e, m=movie: select_movie(m))
        info.bind("<Button-1>", lambda e, m=movie: select_movie(m))
        for child in info.winfo_children():
            child.bind("<Button-1>", lambda e, m=movie: select_movie(m))


def select_movie(movie):
    global chosen_movie
    chosen_movie = movie
    # little popup to confirm - maybe i should highlight the row instead but this works
    popup = tk.Toplevel(window)
    popup.title("")
    popup.geometry("300x90")
    popup.configure(bg="#ffffff")
    popup.grab_set()
    tk.Label(popup, text="✓  Selected: " + movie["title"],
             font=("Arial", 11, "bold"), bg="#ffffff", fg="#1a6b1a",
             pady=20).pack()
    tk.Button(popup, text="OK", bg="#1a5fa8", fg="white",
              font=("Arial", 10), relief="flat", padx=16, pady=5,
              command=popup.destroy).pack()


def keyboard_select(event):
    key = event.char.upper()
    for movie in movies_list:
        if movie["key"] == key and movie["seats"] > 0:
            select_movie(movie)
            break


def go_to_page2():
    if chosen_movie is None:
        show_error("Please pick a movie first!")
        return
    window.unbind("<Key>")
    show_page2()


# -----------------------------------------------
# PAGE 2 - how many tickets
# -----------------------------------------------
def show_page2():
    global current_page, num_tickets
    current_page = 2
    num_tickets = 1  # reset to 1 each time we come here
    clear_screen()
    draw_steps(2)

    tk.Label(main_area, text="🎟 How Many Tickets?",
             font=("Arial", 15, "bold"), bg="#f5f5f0").pack(anchor="w", pady=(4, 10))

    # show which movie they picked
    movie_card = tk.Frame(main_area, bg="#ffffff", relief="solid", bd=1)
    movie_card.pack(fill="x", pady=(0, 12))

    tk.Label(movie_card,
             text="  " + chosen_movie["key"] + "  ",
             font=("Arial", 14, "bold"),
             bg="#dceeff", fg="#1a5fa8",
             padx=8, pady=8).pack(side="left")

    detail = tk.Frame(movie_card, bg="#ffffff")
    detail.pack(side="left", padx=10, pady=8)
    tk.Label(detail, text=chosen_movie["title"],
             font=("Arial", 12, "bold"), bg="#ffffff").pack(anchor="w")
    tk.Label(detail,
             text=chosen_movie["genre"] + "  ·  " + chosen_movie["time"] + "  ·  $" + str(chosen_movie["price"]) + "/ticket",
             font=("Arial", 10), fg="#888888", bg="#ffffff").pack(anchor="w")

    # +/- buttons for quantity
    qty_frame = tk.Frame(main_area, bg="#f5f5f0")
    qty_frame.pack(anchor="w", pady=4)

    tk.Label(qty_frame, text="Tickets: ", font=("Arial", 11),
             bg="#f5f5f0", fg="#555555").pack(side="left")

    tk.Button(qty_frame, text="−", font=("Arial", 13, "bold"),
              bg="#ffffff", relief="solid", bd=1, width=2,
              cursor="hand2", command=decrease_qty).pack(side="left")

    # this label shows the current count
    qty_label = tk.Label(qty_frame, text=str(num_tickets),
                         font=("Arial", 14, "bold"), bg="#f5f5f0",
                         width=3, anchor="center")
    qty_label.pack(side="left", padx=6)

    tk.Button(qty_frame, text="+", font=("Arial", 13, "bold"),
              bg="#ffffff", relief="solid", bd=1, width=2,
              cursor="hand2", command=increase_qty).pack(side="left")

    # store these so update functions can reach them
    main_area._qty_label = qty_label

    # seat availability message
    feedback_lbl = tk.Label(main_area, text="",
                            font=("Arial", 10), bg="#f5f5f0", anchor="w")
    feedback_lbl.pack(fill="x", pady=4)
    main_area._feedback_lbl = feedback_lbl

    # subtotal line
    subtotal_lbl = tk.Label(main_area, text="",
                            font=("Arial", 11), fg="#555555", bg="#f5f5f0")
    subtotal_lbl.pack(anchor="w", pady=2)
    main_area._subtotal_lbl = subtotal_lbl

    # update both labels right away
    refresh_qty_display()

    # nav buttons
    nav = tk.Frame(main_area, bg="#f5f5f0")
    nav.pack(fill="x", pady=(10, 0))

    tk.Button(nav, text="← Back", bg="#ffffff", fg="#333333",
              font=("Arial", 10), relief="solid", bd=1,
              padx=14, pady=7, cursor="hand2",
              command=show_page1).pack(side="left", padx=(0, 8))

    tk.Button(nav, text="Continue →", bg="#1a5fa8", fg="white",
              font=("Arial", 11, "bold"), relief="flat",
              padx=20, pady=8, cursor="hand2",
              command=go_to_page3).pack(side="left")


def decrease_qty():
    global num_tickets
    if num_tickets > 1:
        num_tickets -= 1
        refresh_qty_display()


def increase_qty():
    global num_tickets
    if num_tickets < 10:
        num_tickets += 1
        refresh_qty_display()


def refresh_qty_display():
    # update the number label
    if hasattr(main_area, "_qty_label"):
        main_area._qty_label.config(text=str(num_tickets))

    # figure out seat situation
    seats_left = chosen_movie["seats"]
    remaining_after = seats_left - num_tickets

    if remaining_after < 0:
        msg = "⚠  Not enough seats! Only " + str(seats_left) + " available."
        fg = "#cc2222"
        bg = "#ffecec"
    elif remaining_after == 0:
        msg = "⚡  You're taking the last " + str(num_tickets) + " seat(s)!"
        fg = "#885500"
        bg = "#fff5d6"
    elif remaining_after <= 5:
        msg = "⚠  Only " + str(remaining_after) + " seat(s) left after your booking - hurry!"
        fg = "#885500"
        bg = "#fff5d6"
    else:
        msg = "✓  " + str(remaining_after) + " seat(s) will remain after your booking."
        fg = "#1a6b1a"
        bg = "#e8f7e8"

    if hasattr(main_area, "_feedback_lbl"):
        main_area._feedback_lbl.config(text=msg, fg=fg, bg=bg)

    # update subtotal
    subtotal = round(chosen_movie["price"] * num_tickets, 2)
    if hasattr(main_area, "_subtotal_lbl"):
        main_area._subtotal_lbl.config(
            text="Subtotal: " + str(num_tickets) + " x $" + str(chosen_movie["price"]) + " = $" + str(subtotal))


def go_to_page3():
    if chosen_movie["seats"] < num_tickets:
        show_error("Not enough seats available!\nOnly " + str(chosen_movie["seats"]) + " seats left.")
        return
    show_page3()


# -----------------------------------------------
# PAGE 3 - state & coupon
# -----------------------------------------------
def show_page3():
    global current_page
    current_page = 3
    clear_screen()
    draw_steps(3)

    tk.Label(main_area, text="📍 Your Info & Discounts",
             font=("Arial", 15, "bold"), bg="#f5f5f0").pack(anchor="w", pady=(4, 10))

    # state selector
    state_card = tk.Frame(main_area, bg="#ffffff", relief="solid", bd=1)
    state_card.pack(fill="x", pady=(0, 10))

    tk.Label(state_card, text="What state are you in? (we need this for tax)",
             font=("Arial", 10), bg="#ffffff", fg="#666666",
             pady=8).pack(anchor="w", padx=12)

    state_var = tk.StringVar()

    # if they already picked a state before, keep it selected
    if chosen_state != "":
        state_var.set(chosen_state)

    state_dropdown = ttk.Combobox(state_card, textvariable=state_var,
                                  values=dropdown_states,
                                  state="readonly", font=("Arial", 11), width=38)
    state_dropdown.pack(anchor="w", padx=12, pady=(0, 6))

    # shows the tax rate once they pick a state
    tax_info_lbl = tk.Label(state_card, text="", font=("Arial", 10),
                            bg="#ffffff", fg="#666666", pady=4)
    tax_info_lbl.pack(anchor="w", padx=12)

    def on_state_pick(event):
        global chosen_state
        chosen_state = state_var.get()
        # pull out the state code from "New York (NY)"
        code = chosen_state.split("(")[-1].replace(")", "").strip()
        rate = state_taxes.get(code, 0)
        if rate == 0:
            tax_info_lbl.config(text="Nice - no state sales tax here!", fg="#1a6b1a")
        else:
            pct = round(rate * 100, 3)
            tax_info_lbl.config(text="Tax rate: " + str(pct) + "%", fg="#555555")

    state_dropdown.bind("<<ComboboxSelected>>", on_state_pick)

    # trigger it if already selected
    if chosen_state != "":
        on_state_pick(None)

    # coupon section
    tk.Frame(main_area, bg="#dddddd", height=1).pack(fill="x", pady=8)

    coupon_card = tk.Frame(main_area, bg="#ffffff", relief="solid", bd=1)
    coupon_card.pack(fill="x")

    tk.Label(coupon_card, text="Got a coupon? Enter it below (optional)",
             font=("Arial", 10), bg="#ffffff", fg="#666666",
             pady=8).pack(anchor="w", padx=12)

    coupon_row = tk.Frame(coupon_card, bg="#ffffff")
    coupon_row.pack(anchor="w", padx=12, pady=(0, 6))

    coupon_var = tk.StringVar()
    # keep whatever they typed before
    if coupon_code_typed != "":
        coupon_var.set(coupon_code_typed)

    coupon_entry = tk.Entry(coupon_row, textvariable=coupon_var,
                            font=("Arial", 11), relief="solid", bd=1,
                            width=20, fg="#333333")
    coupon_entry.pack(side="left", ipady=5, padx=(0, 8))

    coupon_status_lbl = tk.Label(coupon_card, text="",
                                  font=("Arial", 10), bg="#ffffff")
    coupon_status_lbl.pack(anchor="w", padx=12, pady=(0, 8))

    # pre-fill status if coupon already applied
    if coupon_applied is not None:
        coupon_status_lbl.config(
            text="✓ Code applied: " + str(coupon_applied) + "% off!",
            fg="#1a6b1a", bg="#e8f7e8")

    def try_coupon():
        global coupon_applied, coupon_code_typed
        code = coupon_var.get().strip().upper()
        coupon_code_typed = code
        if code == "":
            coupon_status_lbl.config(text="Type a code first", fg="#cc2222", bg="#ffecec")
            return
        if code in valid_coupons:
            coupon_applied = valid_coupons[code]
            coupon_status_lbl.config(
                text="✓ Nice! " + str(coupon_applied) + "% off applied",
                fg="#1a6b1a", bg="#e8f7e8")
        else:
            coupon_applied = None
            coupon_status_lbl.config(
                text="✗ Hmm, that code didn't work. Try SAVE5, POPCORN10 or VIP15",
                fg="#cc2222", bg="#ffecec")

    tk.Button(coupon_row, text="Apply", bg="#1a5fa8", fg="white",
              font=("Arial", 10, "bold"), relief="flat",
              padx=10, pady=5, cursor="hand2",
              command=try_coupon).pack(side="left")

    tk.Label(coupon_card, text="hint: codes are SAVE5, POPCORN10, VIP15",
             font=("Arial", 9), bg="#ffffff", fg="#bbbbbb").pack(anchor="w", padx=12, pady=(0, 8))

    # error label (hidden until needed)
    err_lbl = tk.Label(main_area, text="", font=("Arial", 10),
                       bg="#ffecec", fg="#cc2222")
    main_area._page3_err = err_lbl

    # nav buttons
    nav = tk.Frame(main_area, bg="#f5f5f0")
    nav.pack(fill="x", pady=(12, 0))

    tk.Button(nav, text="← Back", bg="#ffffff", fg="#333333",
              font=("Arial", 10), relief="solid", bd=1,
              padx=14, pady=7, cursor="hand2",
              command=show_page2).pack(side="left", padx=(0, 8))

    tk.Button(nav, text="Review Order →", bg="#1a5fa8", fg="white",
              font=("Arial", 11, "bold"), relief="flat",
              padx=20, pady=8, cursor="hand2",
              command=lambda: go_to_page4(state_var)).pack(side="left")


# need this to track what they typed in the coupon box
coupon_code_typed = ""


def go_to_page4(state_var):
    global chosen_state
    chosen_state = state_var.get()
    if chosen_state == "":
        if hasattr(main_area, "_page3_err"):
            main_area._page3_err.config(text="⚠  Please pick your state before continuing!")
            main_area._page3_err.pack(fill="x", pady=(6, 0))
        return
    show_page4()


# -----------------------------------------------
# PAGE 4 - review + confirm
# -----------------------------------------------
def show_page4():
    global current_page
    current_page = 4
    clear_screen()
    draw_steps(4)

    tk.Label(main_area, text="🧾 Review Your Order",
             font=("Arial", 15, "bold"), bg="#f5f5f0").pack(anchor="w", pady=(4, 10))

    # get the state code back out
    state_code = chosen_state.split("(")[-1].replace(")", "").strip()
    tax_rate = state_taxes.get(state_code, 0)
    state_full_name = state_names.get(state_code, state_code)

    # calculate everything
    subtotal = round(chosen_movie["price"] * num_tickets, 2)
    discount_amount = 0
    if coupon_applied:
        discount_amount = round(subtotal * (coupon_applied / 100), 2)

    taxable_amount = subtotal - discount_amount
    tax_amount = round(taxable_amount * tax_rate, 2)
    total = round(taxable_amount + tax_amount, 2)

    # summary card
    card = tk.Frame(main_area, bg="#ffffff", relief="solid", bd=1)
    card.pack(fill="x")

    def add_line(label_text, value_text, bold=False, color=None):
        row = tk.Frame(card, bg="#ffffff")
        row.pack(fill="x", padx=14, pady=4)
        w = "bold" if bold else "normal"
        sz = 12 if bold else 11
        fg = color if color else "#1a1a1a"
        tk.Label(row, text=label_text, font=("Arial", sz, w),
                 bg="#ffffff", fg="#666666").pack(side="left")
        tk.Label(row, text=value_text, font=("Arial", sz, w),
                 bg="#ffffff", fg=fg).pack(side="right")

    tk.Frame(card, bg="#ffffff", height=8).pack()
    add_line(chosen_movie["title"], "")
    add_line(str(num_tickets) + " ticket(s) x $" + str(chosen_movie["price"]),
             "$" + str(subtotal))

    if discount_amount > 0:
        add_line("Coupon (" + str(coupon_applied) + "% off)", "- $" + str(discount_amount),
                 color="#1a6b1a")

    tax_label = "Tax (" + state_full_name + " " + str(round(tax_rate * 100, 3)) + "%)"
    add_line(tax_label, "$" + str(tax_amount))

    # divider line
    tk.Frame(card, bg="#dddddd", height=1).pack(fill="x", padx=14, pady=6)

    add_line("TOTAL", "$" + str(total), bold=True)
    tk.Frame(card, bg="#ffffff", height=10).pack()

    # nav buttons
    nav = tk.Frame(main_area, bg="#f5f5f0")
    nav.pack(fill="x", pady=(12, 0))

    tk.Button(nav, text="← Back", bg="#ffffff", fg="#333333",
              font=("Arial", 10), relief="solid", bd=1,
              padx=14, pady=7, cursor="hand2",
              command=show_page3).pack(side="left", padx=(0, 8))

    tk.Button(nav, text="🎟 Confirm Booking!", bg="#1a5fa8", fg="white",
              font=("Arial", 11, "bold"), relief="flat",
              padx=20, pady=8, cursor="hand2",
              command=lambda: do_confirm(subtotal, discount_amount, tax_amount, total, state_full_name, tax_rate)).pack(side="left")


def do_confirm(subtotal, discount_amount, tax_amount, total, state_full_name, tax_rate):
    # deduct the seats from inventory
    chosen_movie["seats"] -= num_tickets
    show_confirmation(subtotal, discount_amount, tax_amount, total, state_full_name, tax_rate)


# -----------------------------------------------
# PAGE 5 - confirmation / receipt
# -----------------------------------------------
def show_confirmation(subtotal, discount_amount, tax_amount, total, state_full_name, tax_rate):
    clear_screen()

    # hide step bar
    for w in window.winfo_children():
        if hasattr(w, "_is_stepbar"):
            w.pack_forget()

    # random confirmation number like real booking sites
    conf_num = "CB" + str(random.randint(100000, 999999))

    tk.Label(main_area, text="✅", font=("Arial", 36), bg="#f5f5f0").pack(pady=(16, 4))
    tk.Label(main_area, text="You're all set!",
             font=("Arial", 18, "bold"), bg="#f5f5f0", fg="#1a1a1a").pack()
    tk.Label(main_area, text="Confirmation #" + conf_num + "  —  enjoy the movie!",
             font=("Arial", 11), bg="#f5f5f0", fg="#888888").pack(pady=(2, 14))

    # receipt box
    receipt = tk.Frame(main_area, bg="#f0f0eb", relief="solid", bd=1)
    receipt.pack(fill="x", padx=10)

    def receipt_row(left, right, bold=False, green=False):
        row = tk.Frame(receipt, bg="#f0f0eb")
        row.pack(fill="x", padx=12, pady=3)
        w = "bold" if bold else "normal"
        sz = 12 if bold else 11
        fg_right = "#1a6b1a" if green else "#1a1a1a"
        tk.Label(row, text=left, font=("Arial", sz), bg="#f0f0eb",
                 fg="#666666").pack(side="left")
        tk.Label(row, text=right, font=("Arial", sz, w),
                 bg="#f0f0eb", fg=fg_right).pack(side="right")

    tk.Frame(receipt, bg="#f0f0eb", height=8).pack()
    receipt_row("Movie", chosen_movie["title"])
    receipt_row("Genre / Runtime", chosen_movie["genre"] + " · " + chosen_movie["time"])
    receipt_row("Tickets", str(num_tickets) + " x $" + str(chosen_movie["price"]))
    receipt_row("Subtotal", "$" + str(subtotal))

    if discount_amount > 0:
        receipt_row("Coupon (" + str(coupon_applied) + "% off)", "- $" + str(discount_amount), green=True)

    receipt_row("Tax (" + state_full_name + " " + str(round(tax_rate * 100, 3)) + "%)",
                "$" + str(tax_amount))
    tk.Frame(receipt, bg="#cccccc", height=1).pack(fill="x", padx=12, pady=5)
    receipt_row("Total Paid", "$" + str(total), bold=True)
    tk.Frame(receipt, bg="#f0f0eb", height=8).pack()

    # book again button
    tk.Button(main_area, text="🔄 Book Another Ticket",
              bg="#1a5fa8", fg="white",
              font=("Arial", 11, "bold"), relief="flat",
              padx=20, pady=10, cursor="hand2",
              command=reset_everything).pack(pady=(14, 0))


# -----------------------------------------------
# Utility stuff
# -----------------------------------------------

def show_error(msg):
    # simple popup for errors
    popup = tk.Toplevel(window)
    popup.title("Oops")
    popup.geometry("320x100")
    popup.configure(bg="#ffffff")
    popup.grab_set()
    tk.Label(popup, text=msg, font=("Arial", 11),
             bg="#ffffff", fg="#cc2222",
             wraplength=280, pady=18).pack()
    tk.Button(popup, text="OK", bg="#1a5fa8", fg="white",
              font=("Arial", 10), relief="flat", padx=16, pady=5,
              cursor="hand2", command=popup.destroy).pack()


def reset_everything():
    # reset all the global state and go back to start
    global chosen_movie, num_tickets, chosen_state, coupon_applied, coupon_code_typed
    chosen_movie = None
    num_tickets = 1
    chosen_state = ""
    coupon_applied = None
    coupon_code_typed = ""

    # show step bar again
    for w in window.winfo_children():
        if hasattr(w, "_is_stepbar"):
            w.pack(fill="x", padx=20, pady=(0, 6))
            break

    show_page1()


# -----------------------------------------------
# header at the top
# -----------------------------------------------
header = tk.Frame(window, bg="#ffffff", relief="solid", bd=1)
header.pack(fill="x")

tk.Label(header, text="🎬  CineBook",
         font=("Arial", 17, "bold"), bg="#ffffff", fg="#1a1a1a",
         pady=12).pack()
tk.Label(header, text="Buy tickets for the latest movies",
         font=("Arial", 10), bg="#ffffff", fg="#888888",
         pady=(0, 10)).pack()

# kick things off
show_page1()
window.mainloop()
