use std::collections::{BTreeSet, HashMap, HashSet};

#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let mut sum = 0;
    let mut ord_rules: HashMap<u32, HashSet<u32>> = HashMap::new();
    let mut lines = input.lines();

    while let Some(line) = lines.next() {
        if line.is_empty() {
            break;
        }

        let mut values = line.split('|');
        let a: u32 = values
            .next()
            .unwrap()
            .parse()
            .expect("values should be numbers");
        let b: u32 = values
            .next()
            .unwrap()
            .parse()
            .expect("values should be numbers");

        ord_rules.entry(a).or_insert(HashSet::new()).insert(b);
    }

    for line in lines {
        let mut values = line
            .split(',')
            .map(|v| v.parse().expect("values should be numbers"))
            .collect::<Vec<u32>>();

        if check_rules(&values, &ord_rules) {
            continue;
        }

        reorder_values(&mut values, &ord_rules);
        let mid_value = values[values.len() / 2];
        sum += mid_value;
    }

    Ok(sum.to_string())
}

fn check_rules(values: &[u32], ord_rules: &HashMap<u32, HashSet<u32>>) -> bool {
    if values.len() < 2 {
        return true;
    }
    let curr = values[0];
    for &value in values.iter().skip(1) {
        match ord_rules.get(&value) {
            Some(set) => {
                return !set.contains(&curr) && check_rules(&values[1..], ord_rules);
            }
            None => return check_rules(&values[1..], ord_rules),
        }
    }
    false
}

fn compute_in_degree(
    values: &[u32],
    ord_rules: &HashMap<u32, HashSet<u32>>,
) -> HashMap<u32, usize> {
    let value_set: HashSet<u32> = values.iter().copied().collect();
    let mut in_degree: HashMap<u32, usize> = values.iter().map(|&v| (v, 0)).collect();

    for (&before, after_set) in ord_rules {
        if !value_set.contains(&before) {
            continue;
        }
        for &after in after_set {
            if value_set.contains(&after) {
                *in_degree.entry(after).or_insert(0) += 1;
            }
        }
    }

    in_degree
}

fn reorder_values(values: &mut Vec<u32>, ord_rules: &HashMap<u32, HashSet<u32>>) {
    let mut in_degree = compute_in_degree(values, ord_rules);

    let mut queue: BTreeSet<u32> = values
        .iter()
        .filter(|&v| in_degree.get(v).unwrap_or(&0) == &0)
        .copied()
        .collect();

    let mut sorted_values = Vec::with_capacity(values.len());
    while let Some(value) = queue.iter().next().copied() {
        queue.remove(&value);
        sorted_values.push(value);

        if let Some(set) = ord_rules.get(&value) {
            for &v in set {
                if in_degree.get_mut(&v).map_or(false, |d| {
                    *d -= 1;
                    *d == 0
                }) {
                    queue.insert(v);
                }
            }
        }
    }

    *values = sorted_values;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
";
        assert_eq!("123", process(input)?);
        Ok(())
    }
}
