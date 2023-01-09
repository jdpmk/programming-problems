mod part1;
mod part2;

fn main() {
    let manhattan: i32 = part1::solve();
    println!("{}", manhattan);

    // TODO: this is a little slow...
    let manhattan: i32 = part2::solve();
    println!("{}", manhattan);
}
