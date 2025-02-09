use regex::Regex;

#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    // mul(a,b) or do() or don't()
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)").unwrap();
    let mut enabled = true;
    let mut result = 0;

    for line in input.lines() {
        for cap in re.captures_iter(line) {
            match cap.get(0).unwrap().as_str() {
                "do()" => enabled = true,
                "don't()" => enabled = false,
                _ if !enabled => continue,
                _ => {
                    let a: u32 = cap[1].parse().unwrap();
                    let b: u32 = cap[2].parse().unwrap();
                    result += a * b;
                }
            }
        }
    }

    Ok(result.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";
        assert_eq!("48", process(input)?);
        Ok(())
    }
}
