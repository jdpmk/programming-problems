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

rating :: [[Int]] -> Int -> (Int -> Int -> Bool) -> Int
rating xs i cmp
  | length xs == 1 = binToDec $ xs !! 0
  | otherwise      = rating (filter (\x -> cmp (x !! i) mostCommonBit) xs) (i + 1) cmp
  where
    columnBits    = transpose xs
    mostCommonBit = mostCommon (columnBits !! i)

solve :: [[Int]] -> Int
solve xs = oxygen * co2
  where
    oxygen = rating xs 0 (==)
    co2    = rating xs 0 (/=)

main :: IO ()
main = do
  input <- readFile "input/3.data"
  putStrLn $ (show . solve) (map strToIntArr (lines input))
