from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate sample blob data with obvious clusters.
# Warning: do not override pre existing files!!! All the data generated is perfect for testing.
n_samples = 10000
centers = 4
filepath = f"../input/{n_samples}-{centers}-blob.txt"

x, y = make_blobs(n_samples=n_samples, centers=centers, n_features=2)

plt.scatter(x[:, 0], x[:, 1], c=y, s=10)

with open(filepath, "w") as fout:
    for i, x_coord in enumerate(x[:, 0]):
        y_coord = x[i, 1]
        fout.write(f"{x_coord} {y_coord}\n")

plt.savefig("../plots/blobs-groundtruth.svg", format="svg")
plt.show()
