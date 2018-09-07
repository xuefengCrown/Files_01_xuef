
;; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/PoAIP/chap2-random_sentence.lisp")


(defun one-of (choices)
  "pick one element of set, and make a list of it"
  (list (random-elt choices)))

(defun random-elt (choices)
  "Choose an element from a list at random"
  (elt choices (random (length choices))))

(defun sentence () (append (noun-phrase) (verb-phrase)))
(defun noun-phrase () (append (Article) (Noun)))
(defun verb-phrase () (append (Verb) (noun-phrase)))
(defun Article () (one-of '(the a)))
(defun Noun () (one-of '(man ball woman table)))
(defun Verb () (one-of '(hit took saw liked)))







