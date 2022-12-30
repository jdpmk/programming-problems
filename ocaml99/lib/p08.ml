let rec solve l =
  match l with
  | x :: (y :: _ as rest) -> if x = y then solve rest else x :: solve rest
  | one_or_none -> one_or_none

let compress l = solve l

let test1 () =
  compress
    [ "a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e" ]

let run_tests () = [ test1 () ]
