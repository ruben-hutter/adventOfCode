#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let mut left = vec![];
    let mut right = vec![];

    let _ = input.lines().for_each(|line| {
        let mut parts = line.split_whitespace();
        left.push(parts.next().unwrap().parse::<i32>().unwrap());
        right.push(parts.next().unwrap().parse::<i32>().unwrap());
    });

    let result: i32 = left
        .iter()
        .map(|l| l * right.iter().filter(|r| &l == r).count() as i32)
        .sum();

    Ok(result.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "3   4
4   3
2   5
1   3
3   9
3   3";
        assert_eq!("31", process(input)?);
        Ok(())
    }
}
