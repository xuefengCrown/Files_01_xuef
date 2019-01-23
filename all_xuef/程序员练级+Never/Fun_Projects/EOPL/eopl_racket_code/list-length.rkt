;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname list-length) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define list-length
  (lambda (lst)
    (if (null? lst)
        0
        (+ 1 (list-length (cdr lst))))))
(list-length '(1 2 3 4))

(list-length '(a (b c) d))

(define remove-first
  (lambda (s los)
    (if (null? los)
        '()
        (if (eqv? (car los) s)
            (cdr los)
            (cons (car los) (remove-first s (cdr los)))))))
;;Exercise1.9
(define remove_all
  (lambda (s los)
    (if (null? los)
        '()
        (if (eqv? (car los) s)
            (remove_all s (cdr los))
            (cons (car los) (remove_all s (cdr los)))))))
;; test remove
(remove-first 'b '(b c e f g b b b))
(remove_all 'b '(b c e f g b b b))
