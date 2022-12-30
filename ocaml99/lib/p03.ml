let rec solve l n =
  match l with
  | [] -> raise (Failure "nth")
  | x :: xs -> if n = 0 then x else solve xs (n - 1)

let nth l n = solve l n
let test1 () = nth [ "a"; "b"; "c"; "d"; "e" ] 2
let test2 () = nth [ "a" ] 2
let run_tests () = [ test1 (); (try test2 () with Failure msg -> msg) ]
