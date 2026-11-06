function findReleaseOrder(
    n: number,
    dependencies: number[][]
): number[] {

    const graph: number[][] = Array.from(
        { length: n },
        () => []
    );

    const indegree: number[] = new Array(n).fill(0);

    for (const [feature, prereq] of dependencies) {
        graph[prereq].push(feature);
        indegree[feature]++;
    }

    const queue: number[] = [];

    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) {
            queue.push(i);
        }
    }

    const order: number[] = [];

    while (queue.length > 0) {
        const node = queue.shift()!;

        order.push(node);

        for (const neighbor of graph[node]) {
            indegree[neighbor]--;

            if (indegree[neighbor] === 0) {
                queue.push(neighbor);
            }
        }
    }

    return order.length === n ? order : [];
}
