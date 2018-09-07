;; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/PoAIP/chap2-rs2.lisp")
(defparameter *simple-grammar*
  '((sentence -> (noun-phrase verb-phrase))
    (noun-phrase -> (Article Noun))
    (verb-phrase -> (Verb noun-phrase))
    (Article -> the a)
    (Noun -> man ball woman table)
    (Verb -> hit took saw liked))
    "A grammar for a trivial subset of English.")

(defparameter *bigger-grammar*
  '((sentence -> (noun-phrase verb-phrase))
    (noun-phrase -> (Article Adj* Noun PP*) (Name) (Pronoun))
    (verb-phrase -> (Verb noun-phrase PP*))
    (PP* -> () (PP PP*))
    (Adj* -> () (Adj Adj*))
    (PP -> (Prep noun-phrase))
    (Prep -> to in by with on)
	(Adj ->  big little blue green adiabatic)
	(Article -> the a)
	(Name -> Pat Kim Lee Terry Robin)
	(Noun -> man ball woman table)
	(Verb -> hit took saw 1iked)
	(Pronoun -> he she it these those that)))
	
	
(defvar *grammar* *bigger-grammar* ;*simple-grammar*
"The grammar used by generate. Initially, this is
*simple-grammar*, but we can switch to other grammars.")

(defun one-of (choices)
  "pick one element of set, and make a list of it"
  (list (random-elt choices)))
(defun random-elt (choices)
  "Choose an element from a list at random"
  (elt choices (random (length choices))))
  
(defun rule-lhs (rule)
"The left-hand side of a rule."
  (first rule))
(defun rule-rhs (rule)
"The right-hand side of a rule."
  (rest (rest rule)))
(defun rewrites (category)
"Return a list of the possible rewrites for this category."
  (rule-rhs (assoc category *grammar*)))

(defun generate (phrase)
  "Generate a random sentence or phrase"
  (cond ((listp phrase)
           (mappend #'generate phrase))
        ((rewrites phrase)
            (generate (random-elt (rewrites phrase))))
        (t (list phrase))))
  
;; (mappend #'self-and-double '(1 2 3 4 5))
(defun mappend (fn lst)
  (cond
    ((null lst) nil)
	(t (append (funcall fn (car lst)) (mappend fn (cdr lst))))
  ))

  
  
  








