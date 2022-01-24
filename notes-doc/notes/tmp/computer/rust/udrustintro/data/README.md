The keyword for structure data structure is struct
The syntax for strcutre data structure is struct variable_name {  var1: data_type, var2: data_type}
To initialize the structure m the syntax is let var = struct_var { var1: [value] , var2: [value]}
To get the particular value of x from a structure struct_var  the syntax is struct_var.x


 To initialize the enumeration construct the syntax is enum enum_var { [value1], [value2] , [value3]}
 To assign value for enumeration data type , the syntax is let var:enum_var = enum_var:[value1]
 In pattern matching from enumerations all entries of enumeration must be included or otherwise a variable with name of _

 To initialize the union the syntax is union union_var { var1:data_type, var2:data_type}
 In union it is not necessary to initialize all variables.
 In struct it is necessary to initialize all variables.

 The syntax for option data type is let var:Option[data_type in angular brackets] = 
 The possible values of  Option data type are Some and None.
 The option data type is backed by if and else statement.

The syntaxes for destructuring some is using if let or while let.
 The syntax for de structuring some  by using if is if let Some(var) = var_result { }

 The variable type for array is [variable_type;number of elements]
 The function for number of elements is var_array.len()
 To get the first element from the array the syntax is var_array[0]

 To print the debug value in the print statement the syntax is {:[question_mark]}
 To bulk fill a array , the syntax is [ value ; number_of_times_to_store_value]
If you don't know the fixed size of the number of items in the array then the data type to use is vector.
The syntax for a new vector is let var_vec = Vec::new();
To add new value to vector the syntax is var_var.push(value);
To get a value from vector the syntax is var_vec.get(index);
To remove the last element from vector the syntax is var_vec.pop();




 