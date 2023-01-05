use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn parse(filename: &str) -> Vec<i32> {
    BufReader::new(File::open(filename).unwrap())
        .lines()
        .map(|line| line.unwrap().parse::<i32>().unwrap())
        .collect()
}

fn step(mass: &i32) -> i32 {
    mass / 3 - 2
}

fn find_fuel(mass: &i32) -> i32 {
    return if mass <= &0 {
        0
    } else {
        mass + find_fuel(&step(mass))
    };
}

pub fn solve() -> i32 {
    let masses: Vec<i32> = parse("input/01.data");
    masses.iter().map(|mass| find_fuel(&step(mass))).sum()
}
