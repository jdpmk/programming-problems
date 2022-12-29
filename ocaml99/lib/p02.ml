let rec solve l =
  match l with
  | [] -> None
  | _ :: [] -> None
  | [ x; y ] -> Some (x, y)
  | _ :: xs -> solve xs

let last_two l = solve l
let test1 () = last_two [ "a"; "b"; "c"; "d" ]
let test2 () = last_two [ "a" ]
let run_tests () = [ test1 (); test2 () ]
