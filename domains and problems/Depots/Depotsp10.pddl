(define (problem depotprob7654) (:domain depot)
(:objects
	depot0 depot1 depot2 - depot
	distributor0 distributor1 distributor2 - distributor
	truck0 truck1 - truck
	pallet0 pallet1 pallet2 pallet3 pallet4 pallet5 - pallet
	crate0 crate1 crate2 crate3 crate4 crate5 - crate
	hoist0 hoist1 hoist2 hoist3 hoist4 hoist5 - hoist)
(:init
	(at pallet0 depot0)
	(clear crate1)
	(at pallet1 depot1)
	(clear crate0)
	(at pallet2 depot2)
	(clear crate4)
	(at pallet3 distributor0)
	(clear crate5)
	(at pallet4 distributor1)
	(clear pallet4)
	(at pallet5 distributor2)
	(clear crate3)
	(at truck0 depot1)
	(= (current_load truck0) 0)
	(= (load_limit truck0) 370)
	(at truck1 depot2)
	(= (current_load truck1) 0)
	(= (load_limit truck1) 287)
	(at hoist0 depot0)
	(available hoist0)
	(at hoist1 depot1)
	(available hoist1)
	(at hoist2 depot2)
	(available hoist2)
	(at hoist3 distributor0)
	(available hoist3)
	(at hoist4 distributor1)
	(available hoist4)
	(at hoist5 distributor2)
	(available hoist5)
	(at crate0 depot1)
	(on crate0 pallet1)
	(= (weight crate0) 96)
	(at crate1 depot0)
	(on crate1 pallet0)
	(= (weight crate1) 72)
	(at crate2 distributor2)
	(on crate2 pallet5)
	(= (weight crate2) 74)
	(at crate3 distributor2)
	(on crate3 crate2)
	(= (weight crate3) 16)
	(at crate4 depot2)
	(on crate4 pallet2)
	(= (weight crate4) 23)
	(at crate5 distributor0)
	(on crate5 pallet3)
	(= (weight crate5) 42)
	(= (fuel-cost) 0)
)

(:goal (and
		(on crate0 crate4)
		(on crate2 pallet3)
		(on crate3 pallet0)
		(on crate4 pallet5)
	)
)
(:metric minimize (total-time))
)
