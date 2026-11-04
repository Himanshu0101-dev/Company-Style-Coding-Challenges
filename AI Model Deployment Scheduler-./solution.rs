use std::collections::BinaryHeap;

fn max_deployments(
    deploy_time: Vec<i32>,
    deadline: Vec<i32>,
) -> i32 {

    let mut models: Vec<(i32, i32)> = deploy_time
        .into_iter()
        .zip(deadline.into_iter())
        .collect();

    models.sort_by_key(|x| x.1);

    let mut heap = BinaryHeap::new();
    let mut total = 0;

    for (time, limit) in models {

        total += time;
        heap.push(time);

        if total > limit {
            if let Some(longest) = heap.pop() {
                total -= longest;
            }
        }
    }

    heap.len() as i32
}

fn main() {

    let deploy_time = vec![3,2,4,1];
    let deadline = vec![5,6,8,3];

    println!(
        "{}",
        max_deployments(deploy_time, deadline)
    );
}
