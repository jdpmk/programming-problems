let solve l =
  let rec aux l r = match l with [] -> r | x :: xs -> aux xs (x :: r) in
  aux l []

let rev l = solve l
let test1 () = rev [ "a"; "b"; "c" ]
let run_tests () = [ test1 () ]
