use aho_corasick::AhoCorasick;

fn main() {
    let input = include_str!("./input.txt");
    println!("Sum of calibration values: {}", part2(input));
}

fn part2(input: &str) -> u32 {
    let nums = [
        "one", "1", "two", "2", "three", "3", "four", "4", "five", "5",
        "six", "6", "seven", "7", "eight", "8", "nine", "9"
    ];

    let ac = AhoCorasick::new(nums).unwrap();
    input
        .lines()
        .map(|line| {
            let matches = ac.find_overlapping_iter(line).collect::<Vec<_>>();
            let first = matches.iter().next().unwrap().pattern().as_u32();
            let last = matches.iter().last().unwrap().pattern().as_u32();
            // So that "one" & "1" => 1, "two" & "2" => 2, ...
            (first / 2 + 1) * 10 + (last / 2 + 1)
        })
    .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part2() {
        let input = "two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen";
        assert_eq!(281, part2(input));
    }
}
