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
    println!("Sum of possible IDs: {}", part1(input));
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
    fn valid_for_set(&self, available_cubes: &HashMap<&str, u32>) -> Option<u32> {
        self.game_set
            .iter()
            .all(|set| {
                set.iter().all(|cube| {
                    cube.amount <= *available_cubes
                        .get(cube.color).expect("cube should be valid")
                })
            })
        .then_some(self.id)
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

fn part1(input: &str) -> u32 {
    let available_cubes = HashMap::from([
                                        ("red", 12),
                                        ("green", 13),
                                        ("blue", 14)
    ]);
    let games = parse_games(input).expect("should parse games");
    games
        .1
        .iter()
        .filter_map(|game| game.valid_for_set(&available_cubes))
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
        assert_eq!(8, part1(input));
    }
}
