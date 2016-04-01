(*
 * Zadanie domowe 1, czesc 1
 *  structure file
 *)
structure id283111 :> PART_ONE =
struct
  exception NotImplemented

  datatype 'a tree= Leaf of 'a | Node of 'a tree * 'a * 'a tree

  fun sum n =
	 if n = 1 then 1
	 else n + sum(n-1)

  fun fac n =
	 if n = 1 then 1
	 else n * fac(n-1)

  fun fib n =
	 if n = 1 then 1
	 else if n = 2 then 1
	 else fib(n-1)+fib(n-2)

  fun gcd (n, m) =
    if n = m then n
    else if n < m then gcd (m-n, n)
    else gcd (n-m, m)

  fun max [] = 0
      | max[x] = x
      | max(x::xs) = 
      let
        val y = max(xs)
      in
        if y>x then y else x
      end
    

  fun sumTree (T:int tree) =
    case T of
      Leaf l => l
    | Node (l,w,p) => w + sumTree (l) + sumTree (p)

  fun depth (T:'a tree) =
    case T of
      Leaf l => 0
    | Node (l, _, p) =>
        1 + (fn (x,y) => if x>y then x else y)(depth l,depth p)

  fun binSearch (T:int tree) (x:int) =
    case T of
      Leaf l => l=x
    | Node (l,v,p) =>
        if x=v then true
        else if x<v then binSearch l x
        else binSearch p x

  fun preorder (T:'a tree) =
    case T of
      Leaf l => [l]
    | Node(l,v,r) => [v] @ preorder l @ preorder r

  fun listAdd [] (y:int list) = y
    | listAdd (x:int list) [] = x
    | listAdd (x:int list as hx :: tx) (y:int list as hy :: ty) =
        (hx + hy) :: listAdd tx ty

  fun insert (m:int) [] = [m]
    | insert (m:int) (l:int list as h::t) =
        if m < h then m :: l
        else h :: insert m t

  fun insort (l:int list) =
    let
      fun sort [] res = res
        | sort (h::t) res = sort t (insert h res)
    in
      sort l nil
    end

  fun compose f g  = (fn x => g (f x))
  fun curry f g h  =  f(g,h) 

  fun uncurry f (g,h) = f g h

  fun multifun f n = 
    if n=1 then (fn x => f x)
     else (fn x => f((multifun f (n-1)) x ))

    fun ltake (l:'a list) 0 = []
    |ltake [] (x:int) = []
    |ltake (x::xs) n = x::(ltake xs (n-1))

   fun lall f [] = true
    | lall f (x::xs)= if (f x) then (lall f xs) else false

  fun lmap f [] = []
    |lmap f (x::xs)= (f x)::(lmap f xs)

  fun lrev [] = []
    |lrev (x::xs) = (lrev xs) @ [x]

  fun lzip ([],(m:'b list)) = []
    |lzip ((l:'a list),[]) = []
    |lzip ((x::xs),(y::ys)) = (x,y)::(lzip (xs,ys))

  fun split [] = ([],[])
    |split [x] = ([x],[])
    |split (x1::x2::xs) = let
     val (x1s,x2s) = split xs
     in ((x1::x1s),(x2::x2s)) 
     end;

  fun cartprod (l:'a list) [] =[]
    |cartprod [] (m:'b list) = []
    |cartprod (x::xs) ys = (lmap (fn y=> (x,y)) ys) @ (cartprod xs ys)

end
