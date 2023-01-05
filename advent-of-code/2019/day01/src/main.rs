mod part1;
mod part2;

fn main() {
    let requirements: i32 = part1::solve();
    println!("{}", requirements);

    let requirements: i32 = part2::solve();
    println!("{}", requirements);
}
