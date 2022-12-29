let rec solve l =
  match l with [] -> None | x :: [] -> Some x | _ :: xs -> solve xs

let last l = solve l
let test1 () = last [ "a"; "b"; "c"; "d" ]
let test2 () = last []
let run_tests () = [ test1 (); test2 () ]
