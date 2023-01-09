use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

#[derive(Clone, Copy, Eq, Hash, PartialEq)]
struct Point(i32, i32);

enum Direction {
    Up,
    Down,
    Left,
    Right,
}

struct Step {
    direction: Direction,
    magnitude: i32,
}

impl Step {
    fn parse(s: &str) -> Step {
        let direction = match s.chars().next().unwrap() {
            'U' => Direction::Up,
            'D' => Direction::Down,
            'L' => Direction::Left,
            'R' => Direction::Right,
            _ => panic!("Could not parse unknown direction"),
        };

        let magnitude = match s[1..].parse::<i32>() {
            Ok(v) => v,
            Err(error) => panic!("Could not parse magnitude: {:?}", error),
        };

        Step {
            direction,
            magnitude,
        }
    }
}

fn parse(filename: &str) -> Vec<Vec<Step>> {
    BufReader::new(File::open(filename).unwrap())
        .lines()
        .map(|line| line.unwrap().split(",").map(Step::parse).collect())
        .collect()
}

fn points_visited(path: &Vec<Step>) -> (Vec<Point>, HashMap<Point, i32>) {
    let mut visited: Vec<Point> = Vec::new();
    let mut steps: HashMap<Point, i32> = HashMap::new();

    let mut x: i32 = 0;
    let mut y: i32 = 0;
    let mut steps_taken: i32 = 0;

    for step in path {
        let (dx, dy) = match step.direction {
            Direction::Up => (0, 1),
            Direction::Down => (0, -1),
            Direction::Left => (-1, 0),
            Direction::Right => (1, 0),
        };

        for _ in 0..step.magnitude {
            x += dx;
            y += dy;
            steps_taken += 1;

            let p = Point(x, y);

            visited.push(p);

            if !steps.contains_key(&p) {
                steps.insert(p, steps_taken);
            }
        }
    }

    (visited, steps)
}

pub fn solve() -> i32 {
    let paths: Vec<Vec<Step>> = parse("input/03.data");

    let (visited_a, steps_a) = points_visited(&paths[0]);
    let (visited_b, steps_b) = points_visited(&paths[1]);

    let a: HashSet<Point> = HashSet::from_iter(visited_a);
    let b: HashSet<Point> = HashSet::from_iter(visited_b);

    a.intersection(&b)
        .into_iter()
        .map(|p| steps_a.get(p).unwrap() + steps_b.get(p).unwrap())
        .min()
        .unwrap()
}
