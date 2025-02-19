#[derive(Debug, PartialEq, Clone)]
enum Tile {
    Empty,
    Obstruction,
    Visited,
    OutOfMap,
}

impl From<char> for Tile {
    fn from(c: char) -> Self {
        match c {
            '.' => Self::Empty,
            '#' => Self::Obstruction,
            'X' => Self::Visited,
            _ => panic!("Invalid tile"),
        }
    }
}

#[derive(Debug)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

#[derive(Debug, PartialEq)]
struct Position {
    x: usize,
    y: usize,
}

impl From<(usize, usize)> for Position {
    fn from((x, y): (usize, usize)) -> Self {
        Self { x, y }
    }
}

#[derive(Debug)]
struct Guard {
    position: Position,
    direction: Direction,
}

impl Guard {
    fn new(position: Position, direction: Direction) -> Self {
        Self {
            position,
            direction,
        }
    }

    fn step(&mut self) {
        let (x, y) = (self.position.x, self.position.y);
        self.position = match self.direction {
            Direction::Up => (x, y - 1).into(),
            Direction::Down => (x, y + 1).into(),
            Direction::Left => (x - 1, y).into(),
            Direction::Right => (x + 1, y).into(),
        };
    }

    fn turn_right(&mut self) {
        self.direction = match self.direction {
            Direction::Up => Direction::Right,
            Direction::Down => Direction::Left,
            Direction::Left => Direction::Up,
            Direction::Right => Direction::Down,
        };
    }

    fn check_next(&self, map: &Vec<Vec<Tile>>) -> Tile {
        let (x, y) = (self.position.x, self.position.y);
        match self.direction {
            Direction::Up => {
                if y == 0 {
                    return Tile::OutOfMap;
                } else {
                    map[y - 1][x].clone()
                }
            }
            Direction::Down => {
                if y == map.len() - 1 {
                    return Tile::OutOfMap;
                } else {
                    map[y + 1][x].clone()
                }
            }
            Direction::Left => {
                if x == 0 {
                    return Tile::OutOfMap;
                } else {
                    map[y][x - 1].clone()
                }
            }
            Direction::Right => {
                if x == map[y].len() - 1 {
                    return Tile::OutOfMap;
                } else {
                    map[y][x + 1].clone()
                }
            }
        }
    }
}

/**
 * Parse the input into a map and a starting position
 * The map is a 2D vector of Tiles
 * The starting position is a Guard struct
 *
 * @param input The input string
 * @return A tuple containing the map and the starting position
 */
fn parse_input(input: &str) -> (Vec<Vec<Tile>>, Guard) {
    let mut guard: Guard = Guard::new((0, 0).into(), Direction::Up);
    let map: Vec<Vec<Tile>> = input
        .lines()
        .enumerate()
        .map(|(y, line)| {
            line.chars()
                .enumerate()
                .map(|(x, mut c)| {
                    match c {
                        '^' => {
                            guard = Guard::new((x, y).into(), Direction::Up);
                            c = '.';
                        }
                        'v' => {
                            guard = Guard::new((x, y).into(), Direction::Down);
                            c = '.';
                        }
                        '<' => {
                            guard = Guard::new((x, y).into(), Direction::Left);
                            c = '.';
                        }
                        '>' => {
                            guard = Guard::new((x, y).into(), Direction::Right);
                            c = '.';
                        }
                        _ => {}
                    }
                    c.into()
                })
                .collect()
        })
        .collect();
    (map, guard)
}

#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let (mut map, mut guard) = parse_input(input);

    let mut visited = 1;
    loop {
        let (x, y) = (guard.position.x, guard.position.y);
        match guard.check_next(&map) {
            Tile::Empty => {
                map[y][x] = Tile::Visited;
                guard.step();
                visited += 1;
            }
            Tile::Obstruction => {
                guard.turn_right();
            }
            Tile::OutOfMap => {
                break;
            }
            Tile::Visited => {
                map[y][x] = Tile::Visited;
                guard.step();
            }
        }
    }

    Ok(visited.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
";
        assert_eq!("6", process(input)?);
        Ok(())
    }
}
