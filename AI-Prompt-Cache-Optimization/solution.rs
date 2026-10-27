use std::collections::HashMap;
use std::io;

fn main() {
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).unwrap();
    let n: usize = n_str.trim().parse().unwrap();

    let mut freq: HashMap<String, i32> = HashMap::new();
    let mut answer = 0;

    for _ in 0..n {
        let mut prompt = String::new();
        io::stdin().read_line(&mut prompt).unwrap();

        let mut words: Vec<&str> = prompt.trim().split_whitespace().collect();
        words.sort();

        let key = words.join(" ");

        let count = freq.entry(key).or_insert(0);
        *count += 1;

        answer = answer.max(*count);
    }

    println!("{}", answer);
}
