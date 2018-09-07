;; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/on_lisp/chap6_net_closure.lisp")

(defun *nodes* (make-hash-table))

(defun defnode (name conts &optional yes no)
  (setf (gethash name *nodes*)
    (if yes
		#’(lambda ()
			(format t ”~A~%>> ” conts)
			(case (read)
			  (yes (funcall (gethash yes *nodes*)))
			  (t (funcall (gethash no *nodes*)))))
		#’(lambda () conts))))

