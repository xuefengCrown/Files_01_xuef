#ifndef clox_value_h 
#define clox_value_h 

#include "common.h"  

typedef struct sObj Obj;
typedef struct sObjString ObjString;

typedef enum {            
  VAL_BOOL,               
  VAL_NIL, 
  VAL_NUMBER,
  VAL_OBJ      
} ValueType;

//typedef double Value;
typedef struct {  
  ValueType type; 
  union {         
    bool boolean; 
    double number;
	Obj* obj;
  } as; 
} Value;

typedef struct {     
  int capacity;      
  int count;         
  Value* values;     
} ValueArray;        

void initValueArray(ValueArray* array);              
void writeValueArray(ValueArray* array, Value value);
void freeValueArray(ValueArray* array);

void printValue(Value value);
#endif