; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/mp3_db_v1.lisp")

;;; a mp3 database
(defvar *db* nil)

;; make a cd
;;; (make-cd "Roses" "Kathy Mattea" 7 t)
(defun make-cd (title artist rating ripped?)
  (list :title title :artist artist :rating rating :ripped? ripped?)
)

(defun add-record (cd)
  (push cd *db*)
)

(defun dump-db ()
  (dolist (cd *db*)
    (format t "~{~a:~10t~a~%~}~%" cd)))



;;; test
;; (add-record (make-cd "Roses" "Kathy Mattea" 7 t))  
;; (add-record (make-cd "Fly" "Dixie Chicks" 8 t))  
;; (add-record (make-cd "Home" "Dixie Chicks" 9 t))

(defun prompt-read (prompt)
  (format *query-io* "~a: " prompt)
  (force-output *query-io*)
  (read-line *query-io*))
 
(defun prompt-for-cd ()
  (make-cd
   (prompt-read "Title")
   (prompt-read "Artist")
   (or (parse-integer (prompt-read "Rating") :junk-allowed t) 0)
   (y-or-n-p "Ripped? [y/n]: ")))

(defun add-cds ()
  (loop (add-record (prompt-for-cd))
      (if (not (y-or-n-p "Another? [y/n]: ")) (return))))

	
;; save 2 file	
;; on unix: (save-db "~/my-cds.db")
;; on windows: (save-db "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/xuef_cds.db")
(defun save-db (filename)
  (with-open-file (out filename
						:direction :output
						:if-exists :supersede)
	(with-standard-io-syntax (print *db* out))
  )
)	
;; Unlike FORMAT, PRINT prints Lisp objects in a form that can be read back in by the Lisp reader.
;; WITH-STANDARD-IO-SYNTAX ensures that certain variables that affect the behavior of PRINT are 
;; set to their standard values.  
	 
;; (load-db "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/Practical_CL/xuef_cds.db")	 
(defun load-db (filename)
  (with-open-file (in filename)
    (with-standard-io-syntax
      (setf *db* (read in)))))

;; Querying the Database
;; (select-by-artist '|Dixie Chicks|)
(defun select-by-artist (artist)
  (remove-if-not #'(lambda (cd) (string-equal (getf cd :artist) artist))
				*db*))
(defun select-by-title (title)
  (remove-if-not #'(lambda (cd) (string-equal (getf cd :title) title))
				*db*))

;; general select with higher-order function
(defun select (selector-fn)
  (remove-if-not selector-fn *db*))
  
(defun artist-selector (artist)
  #'(lambda (cd) (string-equal (getf cd :artist) artist)))

(defun title-selector (title)
  #'(lambda (cd) (string-equal (get cd :title) title)))

;; (select (where :rating 10 :ripped nil))
(defun where (&key title artist rating (ripped nil ripped-p))
  #'(lambda (cd)
      (and
       (if title    (equal (getf cd :title)  title)  t)
       (if artist   (equal (getf cd :artist) artist) t)
       (if rating   (equal (getf cd :rating) rating) t)
       (if ripped-p (equal (getf cd :ripped) ripped) t))))
	   
(defun update (selector-fn &key title artist rating (ripped nil ripped-p))
  (setf *db*
        (mapcar
         #'(lambda (row)
             (when (funcall selector-fn row)
               (if title    (setf (getf row :title) title))
               (if artist   (setf (getf row :artist) artist))
               (if rating   (setf (getf row :rating) rating))
               (if ripped-p (setf (getf row :ripped) ripped)))
             row) *db*)))

(defun delete-rows (selector-fn)
  (setf *db* (remove-if selector-fn *db*)))

(defun make-comparison-expr (field value)
  `(equal (getf cd ,field) ,value))

(defun make-comparisons-list (fields)
  (loop while fields
     collecting (make-comparison-expr (pop fields) (pop fields))))
	 
(defmacro where (&rest clauses)
  `#'(lambda (cd) (and ,@(make-comparisons-list clauses))))
