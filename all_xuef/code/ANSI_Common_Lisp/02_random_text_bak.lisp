;; (load "C:/code_dxf/xuefgit/Files_01_xuef/all_xuef/code/ANSI_Common_Lisp/01_Run-length_encoding.lisp")

;; 导出的数据，会被存在哈希表 *words* 里。这个哈希表的键是代表单词的符号，而值会像是下列的关联列表（assoc-lists）:
;; ((|sin| . 1) (|wide| . 2) (|sights| . 1))
;; 使用弥尔顿的失乐园作为示例文件时，这是与键 |discover| 有关的值。
;; 它指出了 “discover” 这个单词，在诗里面用了四次，与 “wide” 用了两次，而 “sin” 与 ”sights” 各一次。

(defparameter *words* (make-hash-table :size 10000))
(defconstant maxword 100)

(defun read-text (pathname)
  (with-open-file (s pathname :direction :input)
    (let ((buffer (make-string maxword))
         (pos 0))
      (do ((c (read-char s nil :eof) 
				 (read-char s nil :eof)))
          ((eql c :eof))
        (if (or (alpha-char-p c) (char= c #\'))
            (progn
              (setf (aref buffer pos) c)
              (incf pos))
            (progn
              (unless (zerop pos)
                (see (intern (string-downcase
                               (subseq buffer 0 pos))))
                (setf pos 0))
              (let ((p (punc c)))
                (if p (see p)))))))))

(defun punc (c)
  (case c
    (#\. '|.|) (#\, '|,|) (#\; '|;|)
    (#\! '|!|) (#\? '|?|) ))

;; 函数 see 注册每一个我们看过的单词。
;; 它需要知道前一个单词，以及我们刚确认过的单词 ── 这也是为什么要有变量 prev 存在。
;; 起初这个变量设为伪单词里的句点；在 see 函数被调用后， prev 变量包含了我们最后见过的单词。
(let ((prev `|.|))
  (defun see (symb)
    (let ((pair (assoc symb (gethash prev *words*))))
      (if (null pair)
          (push (cons symb 1) (gethash prev *words*))
          (incf (cdr pair))))
    (setf prev symb))) ;; 将prev设置为新单词
	
	
