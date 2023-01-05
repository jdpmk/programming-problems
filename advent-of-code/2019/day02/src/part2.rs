const OP_ADD: u32 = 1;
const OP_MULT: u32 = 2;
const OP_HALT: u32 = 99;

fn parse(filename: &str) -> Vec<u32> {
    std::fs::read_to_string(filename)
        .unwrap()
        .trim()
        .split(",")
        .map(|x| x.parse::<u32>().unwrap())
        .collect()
}

fn execute(program: &mut Vec<u32>) {
    let mut i: usize = 0;
    while i < program.len() {
        match program[i] {
            OP_ADD => {
                let a: u32 = program[program[i + 1] as usize];
                let b: u32 = program[program[i + 2] as usize];
                let d: usize = program[i + 3] as usize;
                program[d] = a + b;
                i += 4;
            }
            OP_MULT => {
                let a: u32 = program[program[i + 1] as usize];
                let b: u32 = program[program[i + 2] as usize];
                let d: usize = program[i + 3] as usize;
                program[d] = a * b;
                i += 4;
            }
            OP_HALT => return,
            _ => panic!("unreachable"),
        }
    }
}

pub fn solve() -> u32 {
    let program: Vec<u32> = parse("input/02.data");

    for a in 0..program.len() {
        for b in 0..program.len() {
            let mut candidate = program.clone();
            candidate[1] = a as u32;
            candidate[2] = b as u32;
            execute(&mut candidate);
            
            if candidate[0] == 19690720 {
                return 100 * (a as u32) + (b as u32);
            }
        }
    }

    panic!("unable to find suitable candidate noun and verb");
}
