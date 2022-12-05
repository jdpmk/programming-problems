File.open("input/5.data", "r") do |f|
  contents = f.readlines

  max_stack_height = contents
    .index {|element| element.match?(/[[:space:]]1/) }

  num_stacks = contents[max_stack_height]
    .strip
    .split[-1]
    .to_i

  stacks = Array.new(num_stacks) { Array.new }

  (0...max_stack_height).reverse_each do |i|
    s = contents[i].chomp

    (1...s.length).step(2) do |j|
      stacks[j / 4].push(s[j]) if s[j] != " "
    end
  end

  (max_stack_height + 2...contents.size).each do |i|
    instruction = contents[i].chomp.split
    cnt = instruction[1].to_i
    src = instruction[3].to_i - 1
    dst = instruction[5].to_i - 1

    buffer = Array.new

    cnt.times do
      buffer.push(stacks[src].pop)
    end

    cnt.times do
      stacks[dst].push(buffer.pop)
    end
  end

  top = ""
  num_stacks.times do |i|
    top << stacks[i].pop
  end

  puts top
end
