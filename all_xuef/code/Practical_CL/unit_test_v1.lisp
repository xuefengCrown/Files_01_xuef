;; building an unit test framewordk
; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/unit_test_v1.lisp")
(load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/pcl_util.lisp")

(defvar *test-name* nil)

(defun report-result (result form)
  (format t "~:[fail~;pass~] ... ~a: ~a~%" result *test-name* form)
  result)
	
;;;;;;;;;;;;;;;;;;;;;;;;
(defmacro combine-results (&body forms)
  (with-gensyms (result)
    `(let ((,result t))
      ,@(loop for f in forms collect `(unless ,f (setf ,result nil)))
      ,result)))	
;;; (macroexpand-1 '(check a b c))
(defmacro check (&body forms)
  `(combine-results
    ,@(loop for f in forms collect `(report-result ,f ',f))))	
	
(defun test-+ ()
  (let ((*test-name* 'test-+_v5))
	  (check
		(= (+ 1 2) 3)
		(= (+ 1 2 3) 7)
		(= (+ -1 -3) -4))))	
(defun test-* ()
  (let ((*test-name* 'test-*))
	  (check
	  (= (* 2 3) 6)
	  (= (* 4 3) 12))))	

(defun test-arithmetic()
  (combine-results
    (test-+)
	(test-*)))	  
	
	
	
	
	
	