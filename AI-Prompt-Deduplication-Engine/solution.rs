use std::collections::HashMap;

fn largest_prompt_group(prompts: Vec<String>) -> usize {
    let mut freq: HashMap<String, usize> = HashMap::new();
    let mut answer = 0;

    for prompt in prompts {
        let cleaned: String = prompt
            .to_lowercase()
            .chars()
            .filter(|c| *c != ' ')
            .collect();

        let mut chars: Vec<char> = cleaned.chars().collect();
        chars.sort();

        let key: String = chars.into_iter().collect();

        let count = freq.entry(key).or_insert(0);
        *count += 1;

        answer = answer.max(*count);
    }

    answer
}

fn main() {
    let prompts = vec![
        "Open AI".to_string(),
        "AI Open".to_string(),
        "Hello".to_string(),
        "Olelh".to_string(),
        "Jarvis".to_string(),
    ];

    println!("{}", largest_prompt_group(prompts));
}
