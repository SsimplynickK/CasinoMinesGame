# Modules
import random
import math
import customtkinter as ctk
from PIL import Image

# Config
side_length = 5
total_cells = side_length ** 2
mine_count = 10

# Main application window
app = ctk.CTk()

# Game state
cells = []


def place_mines():
    """Initialize the cell list and randomly place mines."""
    cells.clear()

    for _ in range(total_cells):
        cells.append("💎")

    if mine_count >= total_cells:
        print("ERROR: mine_count must be smaller than total cells.")
        return

    for _ in range(mine_count):
        idx = random.randint(0, total_cells - 1)
        # avoid collisions: re-roll while slot already has a mine
        while cells[idx] == "💣":
            idx = random.randint(0, total_cells - 1)
        cells[idx] = "💣"


def print_cells():
    """Simple console view of cells (row-separated)."""
    out = []
    for i, val in enumerate(cells):
        out.append(str(val))
        if (i + 1) % side_length == 0:
            out.append("\n")
        else:
            out.append(" ")
    print("".join(out))


def init_ui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("ctk_theme.json")

    theme = ctk.ThemeManager.theme["CTk"]["fg_color"]

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    screen_center_x = int((screen_width / 2) - (500 / 2))
    screen_center_y = int((screen_height / 2) - (500 / 2))

    app.configure(fg_color=theme)
    app.geometry(f"500x500+{screen_center_x}+{screen_center_y}")
    app.title("Casino Mines Game")
    app.attributes("-topmost", True)
    app.overrideredirect(True)

    app.update_idletasks()

    global control_win
    control_win = ctk.CTkToplevel(app)
    control_win.configure(fg_color=theme)
    control_win.title("Manager")
    control_win.geometry(f"250x500+{screen_center_x-250}+{screen_center_y}")
    control_win.attributes("-topmost", True)
    control_win.overrideredirect(True)

    global tracker_win
    tracker_win = ctk.CTkToplevel(app)
    tracker_win.configure(fg_color=theme)
    tracker_win.title("Tracker")
    tracker_win.geometry(f"250x500+{screen_center_x+500}+{screen_center_y}")
    tracker_win.attributes("-topmost", True)
    tracker_win.overrideredirect(True)

    global topbar_win
    topbar_win = ctk.CTkToplevel(app)
    topbar_win.configure(fg_color="#0F0D25")
    topbar_win.title("Topbar")
    topbar_win.geometry(f"1000x35+{screen_center_x-250}+{screen_center_y-60}")
    topbar_win.attributes("-topmost", True)
    topbar_win.overrideredirect(True)

    global bottom_pad
    bottom_pad = ctk.CTkToplevel(app)
    bottom_pad.configure(fg_color=theme)
    bottom_pad.title("bottom_padding_window")
    bottom_pad.geometry(f"1000x25+{screen_center_x-250}+{screen_center_y-25}")
    bottom_pad.attributes("-topmost", True)
    bottom_pad.overrideredirect(True)

    global top_pad
    top_pad = ctk.CTkToplevel(app)
    top_pad.configure(fg_color=theme)
    top_pad.title("top_padding_window")
    top_pad.geometry(f"1000x25+{screen_center_x-250}+{screen_center_y+500}")
    top_pad.attributes("-topmost", True)
    top_pad.overrideredirect(True)


def build_board():
    """Create the grid of buttons in the main window."""
    col = 0
    row = 0
    for _ in range(total_cells):
        button_size = (500 * 0.9) / side_length
        padding_size = (500 * 0.1) / (side_length + 1)

        if col == 0:
            padx = (padding_size, padding_size / 2)
        elif col == side_length - 1:
            padx = (padding_size / 2, padding_size)
        else:
            padx = (padding_size / 2, padding_size / 2)

        if row == 0:
            pady = (padding_size, padding_size / 2)
        elif row == side_length - 1:
            pady = (padding_size / 2, padding_size)
        else:
            pady = (padding_size / 2, padding_size / 2)

        button = ctk.CTkButton(app, width=button_size, height=button_size, text="")
        button.grid(row=row, column=col, padx=padx, pady=pady)

        if (col + 1) % side_length == 0:
            row += 1
            col = 0
        else:
            col += 1


def init_topbar():
    button = ctk.CTkButton(topbar_win, width=25, height=25, text="❌", command=app.destroy, fg_color="#6C3131", hover_color="#794F4F", corner_radius=0)
    button.pack(side="right", padx=5, pady=5)

    icon = ctk.CTkImage(dark_image=Image.open("bomb_emoji.png"), size=(25, 25))
    icon_label = ctk.CTkLabel(topbar_win, width=25, height=25, image=icon, text="")
    icon_label.pack(side="left", padx=5, pady=5)

    title = ctk.CTkLabel(topbar_win, width=100, height=25, text="Casino Mines Game")
    title.pack(side="left", padx=0, pady=5)


def set_total_cells(new_total):
    """Change the grid size; expects a perfect-square string or int value."""
    global side_length, total_cells

    new_total = int(new_total)
    side_length = int(math.sqrt(new_total))
    total_cells = new_total

    for widget in app.winfo_children():
        if isinstance(widget, ctk.CTkButton):
            widget.destroy()

    place_mines()
    build_board()
    print_cells()


def init_manager():
    # Current Balance
    balance_frame = ctk.CTkFrame(control_win, fg_color="transparent")
    balance_frame.pack(padx=15, pady=15, fill="x")

    balance_title_label = ctk.CTkLabel(balance_frame, text="Current Balance", anchor="w")
    balance_title_label.pack(side="top", anchor="w")

    balance_label = ctk.CTkLabel(balance_frame, text="$1000.00", anchor="w", font=ctk.CTkFont(size=25, weight="bold"))
    balance_label.pack(side="top", anchor="w")

    # Bet amount entry
    input_frame = ctk.CTkFrame(control_win, fg_color="transparent")
    input_frame.pack(padx=15, pady=15, fill="x")

    bet_label = ctk.CTkLabel(input_frame, text="Bet Amount", anchor="w")
    bet_label.pack(side="top", anchor="w")

    bet_input = ctk.CTkEntry(input_frame, placeholder_text="$0.00")
    bet_input.pack(side="top", fill="x", pady=(5, 0))

    # Grid size
    grid_frame = ctk.CTkFrame(control_win, fg_color="transparent")
    grid_frame.pack(padx=15, pady=15, fill="x")

    grid_label = ctk.CTkLabel(grid_frame, text="Grid Size", anchor="w")
    grid_label.pack(side="top", anchor="w")

    grid_options = ["25", "36", "49", "64"]
    segmented_button = ctk.CTkSegmentedButton(grid_frame, values=grid_options, command=lambda value: set_total_cells(value))
    segmented_button.set("25")
    segmented_button.pack(side="top", fill="x", pady=(5, 0))

    # Mines selector
    mines_selector_frame = ctk.CTkFrame(control_win, fg_color="transparent")
    mines_selector_frame.pack(padx=15, pady=15, fill="x")

    mines_label = ctk.CTkLabel(mines_selector_frame, text="Number of Mines", anchor="w")
    mines_label.pack(side="top", anchor="w")

    def on_mines_slider_change(value):
        value = round(value)
        mines_slider.set(value)
        print(int(value))

    mines_slider = ctk.CTkSlider(mines_selector_frame, from_=1, to=(total_cells - 1), command=on_mines_slider_change)
    mines_slider.configure(number_of_steps=(total_cells - 2))
    mines_slider.pack(side="top", fill="x", pady=(5, 0))

    # Bet Button
    bet_button_frame = ctk.CTkFrame(control_win, fg_color="transparent")
    bet_button_frame.pack(padx=15, pady=15, fill="x")

    bet_button = ctk.CTkButton(bet_button_frame, text="Bet", fg_color="#7734eb", hover_color="#9264e3", height=35)
    bet_button.pack(side="top", fill="x", pady=(5, 0))


# Run
place_mines()
print_cells()
init_ui()
build_board()
init_topbar()
init_manager()
app.mainloop()