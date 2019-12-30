extern crate regex; //this crate here provides a library for analizing strings in computer language
use regex::Regex; //regex is a library for compiling and exequting regular expressions

use std::io; //this will give us acess to standard instruct or string

fn main() {

	let re = Regex::new(r"^[a-z0-9]+@[a-z][.]?[a-z]".unwrap(); // here we are declaring the format of email address and using here unwrap for not letting the condition to fail

	let mut input_emailid = String::new(); //declaring a new string  and it is the input from the user
	
	println!("Hey mate! Say something :");
	
	match io::stdin().read_line(&mut input_emailid) //to get the statement we get match function and passing the line that was read into input

	if re.is_match(&mut input_emailid) == true{
		

		println!("correct email format {}",input_emailid)
	
	
	}
	else {

		println!("Invalid email format {}" , input_emailid)

	}

	
}
