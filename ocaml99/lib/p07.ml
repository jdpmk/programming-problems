type 'a node = One of 'a | Many of 'a node list

let solve l =
  let rec aux l f =
    match l with
    | [] -> f
    | One x :: rest -> aux rest (x :: f)
    | Many xs :: rest -> aux rest (aux xs f)
  in
  List.rev (aux l [])

let flatten l = solve l

let test1 () =
  flatten [ One "a"; Many [ One "b"; Many [ One "c"; One "d" ]; One "e" ] ]

let run_tests () = [ test1 () ]
