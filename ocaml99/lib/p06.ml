let solve l = l = List.rev l
let is_palindrome l = solve l
let test1 () = is_palindrome [ "x"; "a"; "m"; "a"; "x" ]
let test2 () = not (is_palindrome [ "a"; "b" ])
let run_tests () = [ test1 (); test2 () ]
