#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    /*
     * Check if total = num[0] + num[1] + num[2] or total = num[0] * num[1] * num[2]
     * or total = num[0] + num[1] * num[2] or total = num[0] * num[1] + num[2]
     * So there are 2^(n-1) possibilities for each total, where n is the length of the nums
     * Check them and if any is true, add the total to the sum
     */
    let mut sum = 0;

    input.lines().for_each(|line| {
        let mut parts = line.split(": ");
        let total = parts.next().unwrap().parse::<usize>().unwrap();
        let nums = parts.next().unwrap().split(" ").map(|x| x.parse::<usize>().unwrap()).collect::<Vec<usize>>();

        let n = nums.len();
        for i in 0..(1 << (n - 1)) {
            let mut total_ = nums[0];
            for j in 0..(n - 1) {
                if i & (1 << j) > 0 {
                    total_ += nums[j + 1];
                } else {
                    total_ *= nums[j + 1];
                }
            }

            if total_ == total {
                sum += total;
                break;
            }
        }
    });

    Ok(sum.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
";
        assert_eq!("3749", process(input)?);
        Ok(())
    }
}
