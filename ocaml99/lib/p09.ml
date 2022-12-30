let solve l =
  let rec aux l acc packed =
    match l with
    | [] -> acc
    | [ x ] -> (x :: packed) :: acc
    | x :: (y :: _ as rest) ->
        if x = y then aux rest acc (x :: packed)
        else aux rest ((x :: packed) :: acc) []
  in
  List.rev (aux l [] [])

let pack l = solve l

let test1 () =
  pack
    [
      "a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "d"; "e"; "e"; "e"; "e";
    ]

let run_tests () = [ test1 () ]
