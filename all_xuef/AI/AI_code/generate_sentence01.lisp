
; (mapcar #'self-and-double '(1 10 300)) ==> ((1 2) (10 20) (300 600))
; (mappend #'self-and-double '(1 10 300)) ==> (1 2 10 20 300 600)
(defun mappend (fn origin_list)
  (apply #'append (mapcar fn origin_list))
  )
(defun x-square (x) (list x (* x x)))
;;(mappend #'x-square '((1 2 ) (3 4 5)))
(defparameter *simple-grammar*
	'((sentence -> (noun-phrase verb-phrase))
	(noun-phrase -> (Article Noun))
	(verb-phrase -> (Verb noun-phrase))
	(Article -> the a)
	(Noun -> man ball woman table)
	(Verb -> hit took saw liked))
  "A grammar for a trivial subset of English.")
(defvar *grammar* *simple-grammar*
	"The grammar used by generate. Initially, this is
	*simple-grammar*, but we can switch to other grammars.")
(defun rule-lhs (rule)
	"The left-hand side of a rule."
	(first rule))
(defun rule-rhs (rule)
	"The right-hand side of a rule. "
	(rest (rest rule)))

(defun rewrites (category)
	"Return a list of the possible rewrites for this category."
	(rule-rhs (assoc category *grammar*)))
;;(rewrites 'noun)

(defun random-elt (choices)
  (elt choices (random (length choices)))
  )
(defun generate (phrase)
  "Generate a random sentence or phrase"
  (let ((choices (rewrites phrase)))
	(cond ((listp phrase)
	       (mappend #'generate phrase))
	       (choices (generate (random-elt choices)))
	       (t (list phrase)))
	       ))

;(defun generate2 (phrase))
