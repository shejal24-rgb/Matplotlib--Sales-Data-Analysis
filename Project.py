import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Create Dataset
# -------------------------

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 130, 120, 160, 180, 200],
    "Profit": [20, 30, 25, 40, 50, 60]
}

df = pd.DataFrame(data)

print(df)

# -------------------------
# Line Chart
# -------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o",
    linewidth=2,
    label="Sales"
)

for i in range(len(df)):
    plt.text(
        df["Month"][i],
        df["Sales"][i] + 5,
        str(df["Sales"][i]),
        ha="center"
    )

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()

# -------------------------
# Bar Chart
# -------------------------

plt.figure(figsize=(8, 5))

bars = plt.bar(df["Month"], df["Sales"])

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        str(bar.get_height()),
        ha="center"
    )

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# -------------------------
# Scatter Plot
# -------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Sales"],
    df["Profit"]
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.grid(True)

plt.show()

# -------------------------
# Histogram
# -------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["Profit"], bins=5)

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.show()

# Matplotlib
#     ↓
# Line Chart       → Trend
# Bar Chart        → Comparison
# Barh             → Horizontal comparison
# Pie Chart        → Proportion
# Histogram        → Distribution
# Scatter Plot     → Relationship
# Subplot          → Multiple charts
# Legend           → Data labels
# Grid             → Readability
# Annotation       → Highlight information
# Savefig          → Save chart
# Pandas + Matplotlib → Data analysis + visualization
# plt.plot()
# plt.bar()
# plt.barh()
# plt.pie()
# plt.hist()
# plt.scatter()
# plt.subplot()
# plt.title()
# plt.xlabel()
# plt.ylabel()
# plt.legend()
# plt.grid()
# plt.annotate()
# plt.savefig()
# plt.show()