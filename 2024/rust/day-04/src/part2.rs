use std::collections::VecDeque;

const MAS: &str = "MAS";

/**
 * Count all the occurrences of X-MAS in the input.
 * M.M
 * .A.
 * S.S
 *
 * @param input: The input string to process.
 * @return String: The number of occurrences of X-MAS in the input.
 */
#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let mut count: u32 = 0;
    let mut grid = VecDeque::new();

    for line in input.lines() {
        grid.push_back(line.chars().collect());

        if grid.len() == 3 {
            check_diagonals(&grid, &mut count);
            grid.pop_front();
        }
    }

    Ok(count.to_string())
}

/**
 * Check if both strings (normal or reversed) are equal.
 * If they are, return true.
 * Otherwise, return false.
 *
 * @param input1: The first string to compare.
 * @param input2: The second string to compare.
 * @return bool: True if the strings are equal, false otherwise.
 */
fn check_mach(input1: &str, input2: &str) -> bool {
    let input1_rev = input1.chars().rev().collect::<String>();
    let input2_rev = input2.chars().rev().collect::<String>();

    (input1 == MAS || input1_rev == MAS) && (input2 == MAS || input2_rev == MAS)
}

/**
 */
fn check_diagonals(grid: &VecDeque<Vec<char>>, count: &mut u32) {
    let mut diag_str1 = String::new();
    let mut diag_str2 = String::new();

    for i in 0..grid[0].len() - 2 {
        for j in 0..grid.len() - 2 {
            // Top-left to bottom-right
            diag_str1.push(grid[j][i]);
            diag_str1.push(grid[j + 1][i + 1]);
            diag_str1.push(grid[j + 2][i + 2]);

            // Bottom-left to top-right
            diag_str2.push(grid[j + 2][i]);
            diag_str2.push(grid[j + 1][i + 1]);
            diag_str2.push(grid[j][i + 2]);

            if check_mach(&diag_str1, &diag_str2) {
                *count += 1;
            }

            diag_str1.clear();
            diag_str2.clear();
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = ".M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
";
        assert_eq!("9", process(input)?);
        Ok(())
    }
}
