#include "common.h"
#include "chunk.h"
#include "debug.h"
#include "vm.h"

int main(int argc, const char* argv[]) {
  initVM();
  
  Chunk chunk;                          
  initChunk(&chunk);                    
  writeChunk(&chunk, OP_RETURN);
  disassembleChunk(&chunk, "test chunk");
  
  interpret(&chunk);
  
  freeVM();   
  freeChunk(&chunk); 
  
  return 0;
}