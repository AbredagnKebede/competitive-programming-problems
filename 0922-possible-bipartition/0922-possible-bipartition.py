class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(curr, c):
            nonlocal colors

            colors[curr] = c

            for neigh in adj[curr]:

                if colors[neigh] != 0 and colors[neigh] != - c:
                    return False

                if colors[neigh] == 0 and not dfs(neigh, - c):
                    return False

            return True

        colors = [0] * (n + 1)

        adj = defaultdict(list)
        for src, des in dislikes:
            adj[src] += [des]
            adj[des] += [src]

        for i in range(1, n + 1):
            if colors[i] != 0:
                continue

            if not dfs(i, -1):
                return False

        return True