processCommand :: [Int] -> [String] -> [Int]
processCommand [x, y] [dir, mag]
  | dir == "forward" = [x + mag_, y]
  | dir == "up"      = [x, y - mag_]
  | dir == "down"    = [x, y + mag_]
  where
    mag_ = read mag :: Int

solve :: [String] -> Int
solve commands = x * y
  where
    [x, y] = foldl processCommand [0, 0] (map words commands)

main :: IO ()
main = do
  input <- readFile "input/2.data"
  putStrLn $ (show . solve) (lines input)
