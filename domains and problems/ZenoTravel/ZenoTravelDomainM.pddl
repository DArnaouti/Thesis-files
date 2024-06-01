;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (domain zenotravel)
(:requirements :typing :fluents)
(:types locatable city - object
	aircraft person - locatable)
(:predicates (located ?x - locatable  ?c - city)
             (in ?p - person ?a - aircraft))
(:functions (fuel ?a - aircraft)
            (distance ?c1 - city ?c2 - city)
            (slow-burn ?a - aircraft)
            (fast-burn ?a - aircraft)
            (capacity ?a - aircraft)
            (total-fuel-used)
	    (onboard ?a - aircraft)
            (zoom-limit ?a - aircraft)
            )




(:action board-fly-slow
 :parameters (?p - person ?a - aircraft  ?c1 ?c2 - city)
 :precondition (and (located ?a ?c1) (>= (fuel ?a) (* (distance ?c1 ?c2) (slow-burn ?a))) (located ?p ?c1))
 :effect (and (not (located ?a ?c1)) (located ?a ?c2) (increase (total-fuel-used) (* (distance ?c1 ?c2) (slow-burn ?a))) (decrease (fuel ?a) (* (distance ?c1 ?c2) (slow-burn ?a))) (not (located ?p ?c1)) (in ?p ?a) (increase (onboard ?a) 1)))



(:action board-fly-fast
 :parameters (?p - person ?a - aircraft  ?c1 ?c2 - city)
 :precondition (and (located ?a ?c1) (>= (fuel ?a) (* (distance ?c1 ?c2) (fast-burn ?a))) (<= (onboard ?a) (zoom-limit ?a)) (located ?p ?c1))
 :effect (and (not (located ?a ?c1)) (located ?a ?c2) (increase (total-fuel-used) (* (distance ?c1 ?c2) (fast-burn ?a))) (decrease (fuel ?a) (* (distance ?c1 ?c2) (fast-burn ?a))) (not (located ?p ?c1)) (in ?p ?a) (increase (onboard ?a) 1)))
 
 
 
(:action fly-slow-debark
 :parameters (?a - aircraft ?c1 ?c2 - city ?p - person)
 :precondition (and (>= (fuel ?a) (* (distance ?c1 ?c2) (slow-burn ?a))) (in ?p ?a) (located ?a ?c1))
 :effect (and (not (in ?p ?a)) (located ?p ?c2) (decrease (onboard ?a) 1) (not (located ?a ?c1)) (located ?a ?c2) (increase (total-fuel-used) (* (distance ?c1 ?c2) (slow-burn ?a))) (decrease (fuel ?a) (* (distance ?c1 ?c2) (slow-burn ?a)))))
 

 
(:action fly-fast-debark
 :parameters (?a - aircraft ?c1 ?c2 - city ?p - person)
 :precondition (and (<= (onboard ?a) (zoom-limit ?a)) (located ?a ?c1) (>= (fuel ?a) (* (distance ?c1 ?c2) (fast-burn ?a))) (in ?p ?a))
 :effect (and (not (in ?p ?a)) (located ?p ?c2) (decrease (onboard ?a) 1) (not (located ?a ?c1)) (located ?a ?c2) (increase (total-fuel-used) (* (distance ?c1 ?c2) (fast-burn ?a))) (decrease (fuel ?a) (* (distance ?c1 ?c2) (fast-burn ?a)))))





(:action board
 :parameters (?p - person ?a - aircraft ?c - city)
 :precondition (and (located ?p ?c)
                 (located ?a ?c))
 :effect (and (not (located ?p ?c))
              (in ?p ?a)
		(increase (onboard ?a) 1)))


(:action debark
 :parameters (?p - person ?a - aircraft ?c - city)
 :precondition (and (in ?p ?a)
                 (located ?a ?c))
 :effect (and (not (in ?p ?a))
              (located ?p ?c)
		(decrease (onboard ?a) 1)))

(:action fly-slow
 :parameters (?a - aircraft ?c1 ?c2 - city)
 :precondition (and (located ?a ?c1)
                 (>= (fuel ?a) 
                         (* (distance ?c1 ?c2) (slow-burn ?a))))
 :effect (and (not (located ?a ?c1))
              (located ?a ?c2)
              (increase (total-fuel-used)
                         (* (distance ?c1 ?c2) (slow-burn ?a)))
              (decrease (fuel ?a) 
                         (* (distance ?c1 ?c2) (slow-burn ?a)))))
                                  
(:action fly-fast
 :parameters (?a - aircraft ?c1 ?c2 - city)
 :precondition (and (located ?a ?c1)
                 (>= (fuel ?a) 
                         (* (distance ?c1 ?c2) (fast-burn ?a)))
                 (<= (onboard ?a) (zoom-limit ?a)))
 :effect (and (not (located ?a ?c1))
              (located ?a ?c2)
              (increase (total-fuel-used)
                         (* (distance ?c1 ?c2) (fast-burn ?a)))
              (decrease (fuel ?a) 
                         (* (distance ?c1 ?c2) (fast-burn ?a)))
	)
) 

(:action refuel	
 :parameters (?a - aircraft)
 :precondition (and (> (capacity ?a) (fuel ?a))

		)
 :effect (and (assign (fuel ?a) (capacity ?a)))
)



)
