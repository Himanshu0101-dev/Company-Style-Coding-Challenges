use std::collections::HashMap;

fn first_rate_limit_exceeded(requests: Vec<i32>, k: i32) -> i32 {
    let mut freq: HashMap<i32, i32> = HashMap::new();

    for user in requests {
        let count = freq.entry(user).or_insert(0);
        *count += 1;

        if *count > k {
            return user;
        }
    }

    -1
}

fn main() {
    let requests = vec![101, 102, 101, 103, 101, 102, 101];
    let k = 3;

    let result = first_rate_limit_exceeded(requests, k);

    println!("{}", result);
}
