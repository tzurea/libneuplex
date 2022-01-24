By default a scope of variable is limited in an environment by { }
If the same variable name is present in the scope limiters, the variable outside is shadowed.

To initialize constants , they may be initialized by const or static keyword.
const keyword has no memory address whereas static has.
Static constant keywords can be mutable.
To operate mutability with static keywords , you should add the unsafe keyword before {} limiters.

Stack is short term storage.
Heap is long term storage.
To declare a public  function the pub keyword is added before fn.

 The heap construct is given by Box::
 To make a new heap you should specify as let var = Box::new(value)
 