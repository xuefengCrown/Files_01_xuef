;; building an unit test framewordk
; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/unit_test.lisp")
(load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/pcl_util.lisp")

(defvar *test-name* nil)

(defun test-+ ()
  (and (= (+ 1 2) 3)
       (= (+ 1 2 3) 6)
	   (= (+ -1 -3) -4)))
;;;;;;;;;;;;;;;;;;;;;;;
(defun test-+_v2 ()
  (format t "~:[fail~;pass~] ... ~a~%" (= (+ 1 2) 3) '(= (+ 1 2) 3))
  (format t "~:[fail~;pass~] ... ~a~%" (= (+ 1 2 3) 6) '(= (+ 1 2 3) 6))
  (format t "~:[fail~;pass~] ... ~a~%" (= (+ -1 -3) -4) '(= (+ -1 -3) -4))
  )	   
;;;;;;;;;;;;;;;;;;;;;;;
(defun report-result (result form)
  (format t "~:[fail~;pass~] ... ~a: ~a~%" result *test-name* form)
  result)
(defun test-+_v3 ()
  (report-result (= (+ 1 2) 3) '(= (+ 1 2) 3))
  (report-result (= (+ 1 2 3) 6) '(= (+ 1 2 3) 6))
  (report-result (= (+ -1 -3) -4) '(= (+ -1 -3) -4)))
;;;;;;;;;;;;;;;;;;;;;;;
(defun test-+_v4 ()
  (check
    (= (+ 1 2) 3)
	(= (+ 1 2 3) 6)
	(= (+ -1 -3) -4)))

;;; (macroexpand-1 '(check a b c))
(defmacro check (&body forms)
  `(progn
    ,@(loop for f in forms collect `(report-result ,f ',f))))	
	
;;;;;;;;;;;;;;;;;;;;;;;;
(defmacro combine-results (&body forms)
  (with-gensyms (result)
    `(let ((,result t))
      ,@(loop for f in forms collect `(unless ,f (setf ,result nil)))
      ,result)))	
(defmacro check2 (&body forms)
  `(combine-results
    ,@(loop for f in forms collect `(report-result ,f ',f))))	
	
(defun test-+_v5 ()
  (let ((*test-name* 'test-+_v5))
	  (check2
		(= (+ 1 2) 3)
		(= (+ 1 2 3) 7)
		(= (+ -1 -3) -4))))	
(defun test-* ()
  (let ((*test-name* 'test-*))
	  (check2
	  (= (* 2 3) 6)
	  (= (* 4 3) 12))))	
	  
(defmacro deftest (func-name parameters &body body)
  `(defun ,func-name ,parameters
    (let ((*test-name* (append *test-name* (list ',func-name))))
	  ,@body)))
(deftest test-+_v6 ()
  (check2
		(= (+ 1 2) 3)
		(= (+ 1 2 3) 7)
		(= (+ -1 -3) -4)))
(deftest test-*_v2 ()
  (check2
	  (= (* 2 3) 6)
	  (= (* 4 3) 12)))		
(defun test-arith ()
  (combine-results
    (test-+_v5)
    (test-*)))
(deftest test-arithmetic ()
  (combine-results
    (test-+_v6)
	(test-*_v2)))	
(deftest test-math()
  (test-arithmetic))	
	
	
	
	
	