use std::collections::{HashSet, HashMap};

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
        let a: u32 = values.next().unwrap().parse().expect("values should be numbers");
        let b: u32 = values.next().unwrap().parse().expect("values should be numbers");

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

fn reorder_values(values: &mut Vec<u32>, ord_rules: &HashMap<u32, HashSet<u32>>) {
    todo!("reorder {:?} with {:?}", values, ord_rules);
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
