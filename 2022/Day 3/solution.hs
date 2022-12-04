module Main where
import Control.Monad (unless)
import Data.List
import System.Environment

splitHalf l = splitAt ((length  l + 1) `div` 2) l

-- Part 1
priority :: Char -> Int
priority x = (elemIndices x alphabet)!!0 + 1
    where alphabet = ['a','b'..'z']++['A','B'..'Z']

getIntersect :: (String,String) -> Char
getIntersect (a,b) = (intersect a b)!!0

getPriority :: String -> Int
getPriority x = priority (getIntersect (splitHalf x))

applyPriority :: [String] -> [Int]
applyPriority [] = []
applyPriority (x:y) = [getPriority x] ++ applyPriority y

-- Part 2

getPriority2 :: [String] -> Int
getPriority2 x = priority ((intersect (intersect (x!!0) (x!!1)) (x!!2))!!0)

applyPriority2 :: [String] -> [Int]
applyPriority2 [] = []
applyPriority2 x = [getPriority2 (take 3 x)] ++ applyPriority2 (drop 3 x)

-- Input Output Part

main :: IO ()
main = do
    args <- getArgs
    s <- readFile (args !! 0)
    print "Part 1:"
    print (sum (applyPriority $ lines s))
    print "Part 2:"
    print (sum (applyPriority2 $ lines s))