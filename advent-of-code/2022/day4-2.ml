let read_file f =
  let ic = open_in f in
  let rec read_all_lines ic acc =
    try
      let line = input_line ic in
      read_all_lines ic (line :: acc)
    with End_of_file ->
      close_in ic;
      acc
  in
  List.rev (read_all_lines ic [])

let extract pair =
  match String.split_on_char ',' pair with
  | [ a; b ] -> (
      let elf1 = String.split_on_char '-' a in
      let elf2 = String.split_on_char '-' b in
      match (elf1, elf2) with
      | [ p; q ], [ r; s ] ->
          (int_of_string p, int_of_string q, int_of_string r, int_of_string s)
      | _ -> raise (Failure "unexpected pattern"))
  | _ -> raise (Failure "unexpected pattern")

let overlap_at_all (p, q, r, s) = not (q < r || s < p)

let solve pairs =
  List.length (List.filter overlap_at_all (List.map extract pairs))

let main =
  let pairs = read_file "input/4.data" in
  print_int (solve pairs)
