mod part1;
mod part2;

fn main() {
    let value: u32 = part1::solve();
    println!("{}", value);

    let value: u32 = part2::solve();
    println!("{}", value);
}
