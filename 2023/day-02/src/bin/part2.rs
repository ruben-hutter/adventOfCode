use std::collections::HashMap;

use nom::{
    IResult,
    multi::separated_list1,
    character::complete::{line_ending, digit1, alpha1, self},
    sequence::{preceded, separated_pair},
    bytes::complete::tag, combinator::map_res
};

fn main() {
    let input = include_str!("./input.txt");
    println!("Sum of possible IDs: {}", part2(input));
}

#[derive(Debug)]
struct Cube<'a> {
    amount: u32,
    color: &'a str,
}

#[derive(Debug)]
struct Game<'a> {
    id: u32,
    game_set: Vec<Vec<Cube<'a>>>,
}

impl<'a> Game<'a> {
    fn minimum_cube_set(&self) -> u32 {
        let map: HashMap<&str, u32> = HashMap::new();
        self.game_set
            .iter()
            .fold(map, |mut acc, round| {
                for cube in round.iter() {
                    acc.entry(cube.color)
                        .and_modify(|v| {
                            *v = (*v).max(cube.amount);
                        })
                        .or_insert(cube.amount);
                }
                return acc;
            })
            .values()
            .product()
    }
}

// 4 red
fn cube_parser(input: &str) -> IResult<&str, Cube> {
    let (input, (amount, color)) = separated_pair(
        complete::u32, tag(" "), alpha1
        )(input)?;
    Ok((input, Cube { amount, color }))
}

// 3 blue, 4 red
fn game_set_parser(input: &str) -> IResult<&str, Vec<Cube>> {
    let (input, cubes) = separated_list1(tag(", "), cube_parser)(input)?;
    Ok((input, cubes))
}

// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
fn game_parser(input: &str) -> IResult<&str, Game> {
    let (input, id) = preceded(
        tag("Game "), map_res(digit1, str::parse)
        )(input)?;
    let (input, game_set) = preceded(
        tag(": "),
        separated_list1(tag("; "), game_set_parser)
        )(input)?;
    Ok((input, Game { id, game_set }))
}

fn parse_games(input: &str) -> IResult<&str, Vec<Game>> {
    let (input, games) = separated_list1(line_ending, game_parser)(input)?;
    Ok((input, games))
}

fn part2(input: &str) -> u32 {
    let games = parse_games(input).expect("should parse games");
    games
        .1
        .iter()
        .map(|game| game.minimum_cube_set())
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part2() {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
        assert_eq!(2286, part2(input));
    }
}
