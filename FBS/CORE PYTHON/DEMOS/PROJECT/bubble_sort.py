# Project Bubble Sort Visualizer

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math

# arr = [5, 2, 7, 1, 6, 3, 4, 23, 32, 6, 34, 56, 56, 77, 100, 444, 500, 4333]
arr = list(map(int, input("Enter Values By Space To Add Numbers In List: ").split()))

steps = []
a = arr.copy()
swaps = 0

steps.append((a.copy(), swaps, -1, -1, "Start", False))

for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        msg = "No swap"
        swapped = False

        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps += 1
            msg = "Swap done"
            swapped = True

        steps.append((a.copy(), swaps, j, j + 1, msg, swapped))

# Final completed state
steps.append((a.copy(), swaps, -1, -1, "Sorting completed!", False))

fig, ax = plt.subplots(figsize=(12, 6), facecolor="white")
plt.subplots_adjust(bottom=0.3)
fig.suptitle("BUBBLE SORT VISUALIZER [Press Two Times On Slider To Slide]", fontsize=24, fontweight="bold", color="blue")
# fig.suptitle("Press Two Times On Slider To Scroll", fontsize=15, fontweight="bold", color="red")


bars = ax.bar(
    range(len(arr)),
    [math.log1p(x) for x in arr],
    color="black",
    edgecolor="black"
)

labels = [
    ax.text(i, math.log1p(v) + 0.1, str(v),
            ha="center", color="black")
    for i, v in enumerate(arr)
]

ax.set_ylim(0, max(math.log1p(x) for x in arr) + 1)
ax.axis("off")

info = fig.text(0.5, 0.18, "Swaps: 0", ha="center")
status = fig.text(0.5, 0.12, "Start", ha="center")

slider_ax = plt.axes([0.2, 0.06, 0.6, 0.04])
slider = Slider(
    slider_ax, "Step", 0, len(steps) - 1, valstep=1
)

def update(step):
    idx = int(step)
    values, total, x, y, msg, swapped = steps[idx]
    finished = idx == len(steps) - 1

    for k, bar in enumerate(bars):
        height = math.log1p(values[k])
        bar.set_height(height)

        if finished:
            bar.set_facecolor("green")
        elif swapped and (k == x or k == y):
            bar.set_facecolor("red")
        else:
            bar.set_facecolor("black")

        labels[k].set_position((k, height + 0.1))
        labels[k].set_text(str(values[k]))

    info.set_text(f"Swaps: {total}")
    status.set_text(msg)

    # Disable slider when sorting is complete
    slider.set_active(not finished)

    fig.canvas.draw_idle()

slider.on_changed(update)
update(0)
plt.show()


#  Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/PROJECT/bubble_sort.py"