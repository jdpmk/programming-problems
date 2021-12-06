solve :: [Int] -> Int
solve xs = length $ filter (> 0) (zipWith (-) (tail windows) windows)
  where
    windows = zipWith3 (add3) (xs) (tail xs) (tail $ tail xs)
    add3 a b c = a + b + c

main :: IO ()
main = do
  input <- readFile "input/1.data"
  putStrLn $ (show . solve) [read x :: Int | x <- lines input]
