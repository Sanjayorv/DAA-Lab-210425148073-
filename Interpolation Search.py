import customtkinter as ctk

# ----------------------------
# Interpolation Search (fixed)
# ----------------------------
def interpolation(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:
        if arr[low] == arr[high]:
            if arr[low] == x:
                return low
            return -1

        pos = low + ((high - low) * (x - arr[low])) // (arr[high] - arr[low])

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# ----------------------------
# UI setup
# ----------------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Interpolation Search")
app.geometry("480x420")
app.resizable(False, False)

MAIN_PAD = 24

container = ctk.CTkFrame(app, corner_radius=16)
container.pack(fill="both", expand=True, padx=MAIN_PAD, pady=MAIN_PAD)

title_label = ctk.CTkLabel(
    container,
    text="Interpolation Search",
    font=ctk.CTkFont(size=22, weight="bold"),
)
title_label.pack(pady=(24, 4))

subtitle_label = ctk.CTkLabel(
    container,
    text="Enter a sorted, comma-separated array and a value to search",
    font=ctk.CTkFont(size=12),
    text_color="gray50",
)
subtitle_label.pack(pady=(0, 20))

# Array input
array_label = ctk.CTkLabel(container, text="Array (sorted, comma-separated)", anchor="w")
array_label.pack(fill="x", padx=24)

array_entry = ctk.CTkEntry(
    container,
    placeholder_text="e.g. 10,20,30,40,50,60,70,80,90,100",
    height=38,
)
array_entry.pack(fill="x", padx=24, pady=(4, 16))
array_entry.insert(0, "10,20,30,40,50,60,70,80,90,100")

# Target input
target_label = ctk.CTkLabel(container, text="Value to find", anchor="w")
target_label.pack(fill="x", padx=24)

target_entry = ctk.CTkEntry(container, placeholder_text="e.g. 70", height=38)
target_entry.pack(fill="x", padx=24, pady=(4, 20))

# Result display
result_label = ctk.CTkLabel(
    container,
    text="",
    font=ctk.CTkFont(size=14, weight="bold"),
    wraplength=380,
)
result_label.pack(pady=(0, 16))


def run_search():
    raw_arr = array_entry.get().strip()
    raw_x = target_entry.get().strip()

    if not raw_arr or not raw_x:
        result_label.configure(text="Please fill in both fields.", text_color="#d9534f")
        return

    try:
        arr = [int(v.strip()) for v in raw_arr.split(",") if v.strip() != ""]
    except ValueError:
        result_label.configure(text="Array must contain integers only.", text_color="#d9534f")
        return

    if arr != sorted(arr):
        result_label.configure(text="Array must be sorted in ascending order.", text_color="#d9534f")
        return

    try:
        x = int(raw_x)
    except ValueError:
        result_label.configure(text="Value to find must be an integer.", text_color="#d9534f")
        return

    idx = interpolation(arr, x)

    if idx != -1:
        result_label.configure(
            text=f"Element found at index {idx}",
            text_color="#2e7d32",
        )
    else:
        result_label.configure(
            text="Element not found",
            text_color="#d9534f",
        )


search_button = ctk.CTkButton(
    container,
    text="Search",
    height=40,
    command=run_search,
)
search_button.pack(fill="x", padx=24, pady=(0, 8))

app.mainloop()
