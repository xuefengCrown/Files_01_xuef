;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname chap1-exer) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t write repeating-decimal #f #t none #f () #f)))

(define duple
  (lambda (times x)
    (if (eq? times 0)
        '()
        (cons x (duple (- times 1) x)))))
(duple 7 3)
(duple 4 '(ha ha))


(define invert
  (lambda (lst)
    (if (null? lst)
        '()
        (cons (list (cadar lst) (caar lst)) (invert (cdr lst))))))
(invert '((a 1) (a 2) (1 b) (2 b)))
