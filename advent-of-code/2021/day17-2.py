"""
==================
initial conditions
==================
  x_0, y_0   = 0, 0
  vx_0, vy_0 = ?, ? <-- find the best such values using simulation

============
recurrences:
============
[velocity]
  vx_i = vx_(i-1) - sgn(vx_(i-1))
       = vx_(i-2) - sgn(vx_(i-2)) - sgn(vx_(i-1))                 (def. vx_i)
       = vx_(i-3) - sgn(vx_(i-3)) - sgn(vx_(i-2)) - sgn(vx_(i-1)) (def. vx_i)
       = ...
       = vx_(i-k) - Σ_j∈[1..k] sgn(vx_(i-k))                      (apply k times; def. vx_i)

  base case: find k s.t. vx_(i-k) -> vx_0 --> k = i
  vx_i = vx_(i-i) - Σ_j∈[1..i] sgn(vx_(i-i))
       = vx_0 - Σ_j∈[1..i] sgn(vx_0)
       = vx_0 - i*sgn(vx_0)

  vy_i = vy_(i-1) - 1
       = vy_(i-2) - 1 - 1     (def. vy_i)
       = vy_(i-3) - 1 - 1 - 1 (def. vy_i)
       = ...
       = vy_(i-k) - k         (apply k times; def. vy_i)

  base case: find k s.t. vy_(i-k) -> vy_0 --> k = i
  vy_i = vy_(i-k) - k
       = vy_(i-i) - i
       = vy_0 - i

  --> vx_i = | vx_0 - i*sign(vx_0) if i < vx_0
             | 0                   otherwise
  --> vy_i = vy_0 - i

[position]
  x_i = x_(i-1) + vx_(i-1)                                                                   (def. vx_i)
      = x_(i-1) + vx_0 - (i-1)*sgn(vx_0)                                                     (def. x_i)
      = x_(i-2) + vx_(i-2) + vx_0 - (i-1)*sgn(vx_0)                                          (def. vy_i)
      = x_(i-2) + vx_0 - (i-2)*sgn(vx_0) + vx_0 - (i-1)*sgn(vx_0)                            (def. x_i)
      = ...
      = x_(i-k) + Σ_j∈[1..min(vx_0,k)] vx_0 - Σ_j∈[1..min(vx_0,k)] (min(vx_0,i)-j)*sgn(vx_0) (apply k times)

  base case: find k s.t. x_(i-k) -> x_0 --> k = i
  x_i = x_(i-k) + Σ_j∈[1..min(vx_0,k)] vx_0 - Σ_j∈[1..min(vx_0,k)] (min(vx_0,i)-j)*sgn(vx_0)
      = x_(i-i) + Σ_j∈[1..min(vx_0,i)] vx_0 - Σ_j∈[1..min(vx_0,i)] (min(vx_0,i)-j)*sgn(vx_0)
      = x_0 + min(vx_0,i)*vx_0 - (Σ_j∈[1..min(vx_0,i)] min(vx_0,i)*sgn(vx_0) - Σ_j∈[1..min(vx_0,i)] j*sgn(vx_0))
      = x_0 + min(vx_0,i)*vx_0 - (sgn(vx_0)*(Σ_j∈[1..min(vx_0,i)] min(vx_0,i) - Σ_j∈[1..min(vx_0,i)] j))
      = x_0 + min(vx_0,i)*vx_0 - (sgn(vx_0)*(min(vx_0,i)*min(vx_0,i) - min(vx_0,i)*(min(vx_0,i)+1)/2))
      = x_0 + min(vx_0,i)*vx_0 - sgn(vx_0)*min(vx_0,i)*min(vx_0,i) + sgn(vx_0)*min(vx_0,i)*(min(vx_0,i)+1)/2
      = x_0 + min(vx_0,i)*(vx_0 - sgn(vx_0)*min(vx_0,i) + (min(vx_0,i)+1)/2)

  y_i = y_(i-1) + vy_(i-1)
      = y_(i-1) + vy_0 - (i-1)                               (def. vy_i)
      = y_(i-2) + vy_(i-2) + vy_0 - (i-1)                    (def. y_i)
      = y_(i-2) + vy_0 - (i-2) + vy_0 - (i-1)                (def. vy_i)
      = y_(i-3) + vy_(i-3) + vy_0 - (i-2) + vy_0 - (i-1)     (def. y_i)
      = y_(i-3) + vy_0 - (i-3) + vy_0 - (i-2) + vy_0 - (i-1) (def. vy_i)
      = ...
      = y_(i-k) + Σ_j∈[1..k] vy_0 - Σ_j∈[1..k] (i-j)         (apply k times)

  base case: find k s.t. y_(i-k) -> y_0 --> k = i
  y_i = y_(i-k) + Σ_j∈[1..k] vy_0 - Σ_j∈[1..k] (i-j)
      = y_(i-i) + Σ_j∈[1..i] vy_0 - Σ_j∈[1..i] (i-j)
      = y_0     + i*vy_0          - (Σ_j∈[1..i] i - Σ_j∈[1..i] j)
      = y_0     + i*vy_0          - (i*i - i*(i+1)/2)
      = y_0     + i*vy_0          - i*i + i*(i+1)/2
      = y_0     + i*(vy_0 - i + (i+1)/2)

  --> x_i = x_0 + min(vx_0,i)*(vx_0 - sgn(vx_0)*min(vx_0,i) + (min(vx_0,i)+1)/2)
  --> y_i = y_0 + i*(vy_0 - i + (i+1)/2)
"""

sgn = lambda x: 0 if x == 0 else abs(x) / x

def solve(xub, xlb, yub, ylb):
    x_0, y_0 = 0, 0
    num_good_initial_v = 0
    num_iterations = 250

    for vx_0 in range(0, xub * 2):
        for vy_0 in range(yub, abs(yub)):
            for i in range(num_iterations):
                x_i = x_0 + min(vx_0, i) * (vx_0 - sgn(vx_0) * min(vx_0, i) + (min(vx_0, i) + 1) / 2)
                y_i = y_0 + i * (vy_0 - i + (i + 1) / 2)
                if xub <= x_i <= xlb and yub <= y_i <= ylb:
                    num_good_initial_v += 1
                    break

    return num_good_initial_v

def main():
    with open("input/17.data") as f:
        target = f.readline()
        _, dims = target.split(": ")
        x_dims, y_dims = dims.split(", ")
        _, x_bounds = x_dims.split("=")
        _, y_bounds = y_dims.split("=")
        xub, xlb = map(int, x_bounds.split(".."))
        yub, ylb = map(int, y_bounds.split(".."))

        print(solve(xub, xlb, yub, ylb))

if __name__ == "__main__":
    main()
