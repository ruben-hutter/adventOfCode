#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    input
        .lines()
        .try_fold(0, |acc, line| -> miette::Result<usize> {
        let mut parts = line.split(": ");
        let total = parts
            .next()
            .ok_or_else(|| miette::miette!("No total"))?
            .parse::<usize>()
            .map_err(|_| miette::miette!("Failed to parse total"))?;

        let nums = parts
            .next()
            .ok_or_else(|| miette::miette!("No nums"))?
            .split(' ')
            .map(|x| x.parse::<usize>().map_err(|_| miette::miette!("Failed to parse num")))
            .collect::<Result<Vec<usize>, _>>()?;

        let n = nums.len();
        for i in 0..(1 << (n - 1)) {
            let mut total_ = nums[0];
            for j in 0..(n - 1) {
                if i & (1 << j) != 0 {
                    total_ += nums[j + 1];
                } else {
                    total_ *= nums[j + 1];
                }
            }

            if total_ == total {
                return Ok(acc + total);
            }
        }

        Ok(acc)
        })
    .map(|sum| sum.to_string())
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
