use std::collections::{HashMap, VecDeque};

fn detect_fraud(
    transactions: Vec<(i32, i32)>,
    k: usize,
    t: i32,
) -> i32 {

    let mut user_logs: HashMap<i32, VecDeque<i32>> =
        HashMap::new();

    for (user, time) in transactions {

        let queue = user_logs
            .entry(user)
            .or_insert(VecDeque::new());

        while let Some(&front) = queue.front() {
            if time - front > t {
                queue.pop_front();
            } else {
                break;
            }
        }

        queue.push_back(time);

        if queue.len() > k {
            return user;
        }
    }

    -1
}

fn main() {
    let transactions = vec![
        (101, 1),
        (102, 2),
        (101, 3),
        (101, 5),
        (102, 6),
        (101, 8),
    ];

    let result =
        detect_fraud(transactions, 3, 10);

    println!("{}", result);
}
