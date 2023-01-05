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
    let mut program: Vec<u32> = parse("input/02.data");

    program[1] = 12;
    program[2] = 2;
    execute(&mut program);

    program[0]
}
