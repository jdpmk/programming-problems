let rec solve l = match l with [] -> 0 | _ :: xs -> 1 + solve xs
let length l = solve l
let test1 () = length [ "a"; "b"; "c" ]
let test2 () = length []
let run_tests () = [ test1 (); test2 () ]
