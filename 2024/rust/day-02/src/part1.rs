#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let mut count = 0;

    for line in input.lines() {
        let nums: Vec<i32> = line
            .split_whitespace()
            .map(|num| num.parse::<i32>().unwrap())
            .collect();

        let mut safe = true;
        let mut increasing;
        for i in 0..nums.len() - 1 {
            increasing = nums[0] < nums[1];
            let curr = nums[i];
            let next = nums[i + 1];
            let diff = next - curr;
            if (increasing && diff <= 0)
                || (!increasing && diff >= 0)
                || diff.abs() < 1
                || 3 < diff.abs()
            {
                safe = false;
                break;
            }
        }
        if safe {
            count += 1;
        }
    }

    Ok(count.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
";
        assert_eq!("2", process(input)?);
        Ok(())
    }
}
