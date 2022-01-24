fn main() {
    let mut a = 2+3*4;
    let mut b = 4+6*66;
    let mut c:i64 = 329023*218293+21;
    a = a + 12;
    b = b /14;
    c = c/22;

    println!("The value of a is a = {}",a);
    println!("The value of b is a = {}",b);
    println!("The value of c is a = {}",c);

    let mut val:f64 = 13.0;
    println!("The value of remainder from ");
    let val_to_pi:f64 = f64::powf(val, std::f64::consts::PI);
    println!("The value of 13 powered to pi is {} ", val_to_pi);
}
