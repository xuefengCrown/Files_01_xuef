; my common lisp util pack

(defun mklist (x) (if (listp x) x (list x)))

(defmacro with-gensyms ((&rest names) &body body)
  `(let ,(loop for n in names collect `(,n (make-symbol ,(string n))))
     ,@body))
	 
	 