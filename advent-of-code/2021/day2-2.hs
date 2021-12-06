processCommand :: [Int] -> [String] -> [Int]
processCommand [x, y, aim] [dir, mag]
  | dir == "forward" = [x + mag_, y + aim * mag_, aim]
  | dir == "up"      = [x, y, aim - mag_]
  | dir == "down"    = [x, y, aim + mag_]
  where
    mag_ = read mag :: Int

solve :: [String] -> Int
solve commands = x * y
  where
    [x, y, _] = foldl processCommand [0, 0, 0] (map words commands)

main :: IO ()
main = do
  input <- readFile "input/2.data"
  putStrLn $ (show . solve) (lines input)
