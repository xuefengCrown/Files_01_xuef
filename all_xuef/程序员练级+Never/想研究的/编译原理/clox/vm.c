#include <stdio.h>
#include "common.h"
#include "vm.h"    
#include "debug.h"

VM vm; 

void initVM() {
	resetStack();
}                  

void freeVM() {    
}

InterpretResult interpret(Chunk* chunk) {
  //store the chunk being executed in the VM
  vm.chunk = chunk;                      
  vm.ip = vm.chunk->code;                
  return run();                          
}

static InterpretResult run() {          
#define READ_BYTE() (*vm.ip++)  
//READ_CONSTANT() reads the next byte from the bytecode, treats the resulting number as an index, 
//and looks up the corresponding location in the chunk’s constant table
#define READ_CONSTANT() (vm.chunk->constants.values[READ_BYTE()])

#define BINARY_OP(op) \                                          
    do { \                                                       
      double b = pop(); \                                        
      double a = pop(); \                                        
      push(a op b); \                                            
    } while (false)     
  //ip points to the instruction about to be executed
  
  /**
  The READ_BYTE macro reads the byte currently pointed at by ip and then advances the instruction pointer. 
  The first byte of any instruction is the opcode. Given a numeric opcode, we need to get to the right C code 
  that implements that instruction’s semantics. This process is called “decoding” or “dispatching” the instruction.
  **/
  for (;;) {
#ifdef DEBUG_TRACE_EXECUTION
    printf("          ");                                           
	for (Value* slot = vm.stack; slot < vm.stackTop; slot++) {      
	  printf("[ ");                                                 
	  printValue(*slot);                                            
	  printf(" ]");                                                 
	}                                                               
	printf("\n");                                     
    disassembleInstruction(vm.chunk, (int)(vm.ip - vm.chunk->code));
#endif	  
    uint8_t instruction;                
    switch (instruction = READ_BYTE()) {
	  case OP_CONSTANT: {                
        Value constant = READ_CONSTANT();
        push(constant);                   
        break;                           
      }
	  case OP_NEGATE:   push(-pop()); break;
	  
	  case OP_ADD:      BINARY_OP(+); break;
      case OP_SUBTRACT: BINARY_OP(-); break;
      case OP_MULTIPLY: BINARY_OP(*); break;
      case OP_DIVIDE:   BINARY_OP(/); break;
	  
      case OP_RETURN: {
		printValue(pop());  
        printf("\n");
        return INTERPRET_OK;            
      }                                 
    }                                   
  }                                     

#undef READ_BYTE
#undef READ_CONSTANT
#undef BINARY_OP                    
}

static void resetStack() {
  vm.stackTop = vm.stack; 
}

void push(Value value) {
  *vm.stackTop = value; 
  vm.stackTop++;        
} 

Value pop() {         
  vm.stackTop--;      
  return *vm.stackTop;
}


