function! s:HasUnique(s)
  let l:seen = []
  let l:n = len(a:s)

  for i in range(0, n - 1)
    if index(l:seen, a:s[i]) >= 0
      return v:false
    endif
    call add(l:seen, a:s[i])
  endfor

  return v:true
endfunction

function! s:Solve()
  let l:lines = readfile("input/6.data")
  let l:line = lines[0]

  let l:n = len(l:line)
  for i in range(0, l:n - 4)
    let l:substr = line[i:i + 3]
    let l:result = s:HasUnique(l:substr)

    if l:result
      return l:i + 4
    endif
  endfor

  return -1
endfunction

echo s:Solve()
