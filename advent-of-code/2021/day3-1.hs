import Data.List

strToIntArr :: String -> [Int]
strToIntArr s = [if x == '0' then 0 else 1 | x <- s]

binToDec :: [Int] -> Int
binToDec xs = foldl (\acc x -> 2 * acc + x) 0 xs

mostCommon :: [Int] -> Int
mostCommon xs = if zerosCount > onesCount then 0 else 1
  where
    count x    = length . filter (== x)
    zerosCount = count 0 xs
    onesCount  = count 1 xs

solve :: [[Int]] -> Int
solve xs = gamma * epsilon
  where
    columnBits      = transpose xs
    mostCommonBits  = map mostCommon columnBits
    leastCommonBits = map (\x -> 1 - x) mostCommonBits
    gamma           = binToDec mostCommonBits
    epsilon         = binToDec leastCommonBits

main :: IO ()
main = do
  input <- readFile "input/3.data"
  putStrLn $ (show . solve) (map strToIntArr (lines input))
