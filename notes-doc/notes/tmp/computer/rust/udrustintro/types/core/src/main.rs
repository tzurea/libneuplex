use std::mem;

fn main() {
    let a:u8 = 123;
    println!("a = {}", a);
    let mut a:i16 = 415;
    println!("a = {} and size of a is  {}", a , mem::size_of_val(&a));
    a = 416;
    println!("The value of a now is a = {}",  a);     
    let b:usize = 123;
    println!("The value of b is {} and it's size is {}", b, mem::size_of_val(&b));
    let c = true;   
    let d = 283921.22 ;
    println!("c and d are {} and {} repectively", c, d)


}
