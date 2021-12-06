solve :: [Int] -> Int
solve xs = length $ filter (> 0) (zipWith (-) (tail xs) xs)

main :: IO ()
main = do
  input <- readFile "input/1.data"
  putStrLn $ (show . solve) [read x :: Int | x <- lines input]
