from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import time


num_points = 150
num_clusters = 3

start = time.time()


class Datasets:
    def __init__(self, points, clusters):
        self._points = points
        self._clusters = clusters
        self.POINTS = {"path": f"../input/{self._points}points.txt", "name": "points"}
        self.BLOBS = {"path": f"../input/{self._points}-{self._clusters}-blob.txt", "name": "blobs"}
        self.IRIS = {"path": "../input/iris.txt", "name": "iris"}

    def get_data(self, path):
        data = []
        with open(path, "r") as fin:
            lines = fin.readlines()
            for line in lines:
                x = float(line.split(" ")[0])
                y = float(line.split(" ")[1])
                data.append([x, y])
        return np.array(data)


ds = Datasets(num_points, num_clusters)
sel = ds.IRIS
raw_dataset = ds.get_data(sel["path"])


plt.title("Python sklearn clustering")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")

start_kmeans = time.time()
# kmeans in sklearn uses all threads by default with openmp (cython). Set env variable OMP_NUM_THREADS!!!
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(raw_dataset)
end_kmeans = time.time()
end = time.time()

serial_time = round(start_kmeans - start, 5)
kmeans_time = round(end_kmeans - start_kmeans, 5)
print(f"code took {serial_time + kmeans_time} sec from start to finish while kmeans alone took {kmeans_time} sec")

# LOG RUN TIMINGS
# timestamp,execution (s/p),language (p/c),dataset type,no. of points,no. of clusters,threads,no. of iterations,wall time,kmeans time
with open("../output/runs.csv", "a+") as stats:
    stats.write(f"{int(time.time())},{'s'},{'p'},{sel['name']},{num_points},{num_clusters},{1},{kmeans.n_iter_},{serial_time},{kmeans_time}\n")

plt.scatter(raw_dataset[:, 0], raw_dataset[:, 1], s=20, c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=90, marker="*", c="red")
plt.tight_layout()
plt.savefig("../plots/iris-sklearn.svg", format="svg")
plt.show()
