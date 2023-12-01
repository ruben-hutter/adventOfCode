fn main() {
    let input = include_str!("./input.txt");
    println!("Sum of calibration values: {}", part1(input));
}

fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let mut nums_iter = line.chars().filter(|c| c.is_digit(10));
            let first = nums_iter.next().expect("should be a digit");
            let last = nums_iter.last().unwrap_or(first);
            match format!("{first}{last}").parse::<u32>() {
                Ok(n) => n,
                Err(_) => 0,
            }
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let input = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";
        assert_eq!(142, part1(input));
    }
}
