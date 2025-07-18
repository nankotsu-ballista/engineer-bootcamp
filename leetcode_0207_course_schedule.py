from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # グラフ構築 + 入次数カウント
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        # 入次数ゼロの講義をキューに入れる（今すぐ取れるやつ）
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken = 0  # 受講した講義数

        while q:
            course = q.popleft()
            taken += 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)

        # 全部の講義が取れていたらOK、そうでなければサイクルあり
        return taken == numCourses
