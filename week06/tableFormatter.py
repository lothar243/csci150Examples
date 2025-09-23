#!/usr/bin/env python3
"""
tableFormatter.py

A very simple table formatter:
- Left-aligns everything
- Uses fixed column widths
- Truncates with "…" if content is too long
"""

# Column spec list: (header, width)
DEFAULT_COLS = [
    ("Item",   25),
    ("Qty",     5),
    ("Price",   8),
    ("Total",   9),
    ("Notes",  30),
]

def truncate(text, width):
    """Truncate text to fit width, adding … if needed."""
    text = str(text)
    if len(text) <= width:
        return text
    if width < 3:
        return text[:width]
    return text[: width - 1] + "…"

def format_cell(value, width):
    """Make value a string, truncate, and left-align to width."""
    return f"{truncate(value, width):<{width}}"

def format_row(row, cols=DEFAULT_COLS, col_sep=" | "):
    """Format a single row of data."""
    parts = []
    num_cols = len(cols)
    for i in range(num_cols):
        # Get the value if present; otherwise use empty string
        value = row[i] if i < len(row) else ""
        _, width = cols[i]
        parts.append(format_cell(value, width))
    return col_sep.join(parts)

def separator_line(cols=DEFAULT_COLS, col_sep=" | ", sep_char="-"):
    """Build a separator line that matches the table width."""
    segments = []
    for name, width in cols:
        segments.append(sep_char * width)
    return col_sep.join(segments)

def format_table(rows, cols=DEFAULT_COLS, show_header=True):
    """Format rows of data into a simple text table."""
    lines = []
    if show_header:
        header = [cols[i][0] for i in range(len(cols))]
        lines.append(format_row(header, cols))
        lines.append(separator_line(cols))
    for row in rows:
        lines.append(format_row(row, cols))
    return "\n".join(lines)

# ---------- Demo ----------
if __name__ == "__main__":
    demo_rows = [
        ("Mechanical Keyboard (TKL)", 1, 129.99, 129.99, "Hot-swappable, blue switches"),
        ("USB-C Cable (2m braided)", 3, 12.5, 37.5, "Charge + data; lifetime warranty"),
        ("4K Monitor", 2, 349.00, 698.0, "Great color accuracy — factory calibrated"),
        ("Ergonomic Chair w/ Lumbar", 1, 499.0, 499.0, "Mesh back; adjustable arms"),
        ("Desk Mat — Very long name to demonstrate truncation", 1, 24.0, 24.0, "Dark gray"),
    ]

    print(format_table(demo_rows))
