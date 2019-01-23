#lang plai-typed

#|

This is the core language; it is just borrowing a few things from 
ParselTongue.

|#

(define-type CExp
  ;[CNum (n : number)]
  ;[CStr (s : string)]
  ;[CTrue]
  [CSeq (e1 : CExp) (e2 : CExp)]
  [CError (e1 : CExp)]
  [CIf (test : CExp) (then : CExp) (else : CExp)]
  [CId (x : symbol)]
  [CLet (x : symbol) (bind : CExp) (body : CExp)]
  [CList (mutable : boolean) (elts : (listof CExp))]
  ;; Should we have a CSet! case? Or just desugar into something
  ;; that adds a value to a global hashmap?
  [CSet! (x : symbol) (bind : CExp)]
  [CApp (fun : CExp) (args : (listof CExp))]
  [CFunc (args : (listof symbol)) (body : CExp)]
  [CPrim1 (prim : symbol) (arg : CExp)]
  [CPrim2 (prim : symbol) (left : CExp) (right : CExp)]
  [CPass]
  [CObject (type : PrimVal) (val : PrimVal) (fields : (hashof string CExp))]
  [CSetField (obj : CExp) (field : CExp) (value : CExp)]
  [CGetField (obj : CExp) (field : CExp)]
  )

(define-type PrimVal
  [VNum (n : number)]
  [VStr (s : string)]
  [VTrue]
  [VFalse]
  [VNone]
  [VList (mutable : boolean) (data : (listof CVal))]
  [VClosure (env : Env) (args : (listof symbol)) (body : CExp)])

;; why?
(define-type CVal
  [VObject (val : PrimVal) (fields : (hashof string CVal))])

;(define-type-alias Env (hashof symbol CVal))
(define-type Binding
  [bind (name : symbol) (val : CVal)])
 
(define-type-alias Env (listof Binding))
(define mt-env empty)
(define extend-env cons)
(define (lookup [for : symbol] [env : Env]) : CVal
  (cond
    [(empty? env) (error 'lookup "name not found")]
    [else (cond
            [(symbol=? for (bind-name (first env)))
             (bind-val (first env))]
            [else (lookup for (rest env))])]))

