# Programmers
# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def dfs(computers, visited, start):
        stack = [start]

        while stack:
