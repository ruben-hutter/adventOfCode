use std::collections::VecDeque;

const XMAS: &str = "XMAS";

/**
 * Count all the occurrences of XMAS in the input.
 * XMAS can be in any direction (up, down, left, right, diagonal).
 */
#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let mut count: u32 = 0;
    let mut grid = VecDeque::new();

    for line in input.lines() {
        grid.push_back(line.chars().collect());

        check_row(grid.back().unwrap(), &mut count);

        if grid.len() == 4 {
            check_columns(&grid, &mut count);
            check_diagonals(&grid, &mut count);

            grid.pop_front();
        }
    }

    Ok(count.to_string())
}

fn check_mach(input: &str, count: &mut u32) {
    let mut start = 0;
    while let Some(pos) = input[start..].find(XMAS) {
        *count += 1;
        start += pos + 1;
    }
}

/**
 * Check a row for all occurrences of XMAS. This includes checking from left
 * to right and right to left. A row can contain multiple occurrences of XMAS.
 * @param row The row to check
 * @param count The count of XMAS occurrences
 */
fn check_row(row: &Vec<char>, count: &mut u32) {
    let row_str = row.iter().collect::<String>();
    check_mach(&row_str, count);

    let row_str = row.iter().rev().collect::<String>();
    check_mach(&row_str, count);
}

/**
 * Check all columns for all occurrences of XMAS. This includes checking from
 * top to bottom and bottom to top. A column can contain multiple occurrences
 * of XMAS.
 * @param grid The grid to check
 * @param count The count of XMAS occurrences
 */
fn check_columns(grid: &VecDeque<Vec<char>>, count: &mut u32) {
    for col in 0..grid[0].len() {
        let mut col_str = grid.iter().map(|row| row[col]).collect::<String>();
        check_mach(&col_str, count);

        col_str = grid.iter().rev().map(|row| row[col]).collect::<String>();
        check_mach(&col_str, count);
    }
}

/**
 * Check all diagonals for all occurrences of XMAS. This includes checking from
 * top-left to bottom-right and bottom-left to top-right. A diagonal can contain
 * multiple occurrences of XMAS.
 * @param grid The grid to check
 * @param count The count of XMAS occurrences
 */
fn check_diagonals(grid: &VecDeque<Vec<char>>, count: &mut u32) {
    let mut diag_str = String::new();

    for i in 0..grid[0].len() - 3 {
        for j in 0..grid.len() - 3 {
            // Top-left to bottom-right
            diag_str.push(grid[j][i]);
            diag_str.push(grid[j + 1][i + 1]);
            diag_str.push(grid[j + 2][i + 2]);
            diag_str.push(grid[j + 3][i + 3]);
            check_mach(&diag_str, count);

            diag_str = diag_str.chars().rev().collect();
            check_mach(&diag_str, count);
            diag_str.clear();

            // Bottom-left to top-right
            diag_str.push(grid[j + 3][i]);
            diag_str.push(grid[j + 2][i + 1]);
            diag_str.push(grid[j + 1][i + 2]);
            diag_str.push(grid[j][i + 3]);
            check_mach(&diag_str, count);

            diag_str = diag_str.chars().rev().collect();
            check_mach(&diag_str, count);
            diag_str.clear();
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
";
        assert_eq!("18", process(input)?);
        Ok(())
    }
}
