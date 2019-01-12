import unittest
import argparse
import sys
from datetime import date
import reservation_solver

class TestReservationSolver(unittest.TestCase):
    def setUp(self):
        self.solver = reservation_solver
        
    def test_reservation_solver_returns_correct_campsites_for_campspot_test_case_and_default_minimum_reservation_length(self):
        sys.argv = ['reservation_solver.py', 'test_modules/test_cases/test-case.json']
        valid_campsites = self.solver.main()
        self.assertEqual(3, len(valid_campsites))
        self.assertEqual('Comfy Cabin', valid_campsites[0].name)
        self.assertEqual('Rickety Cabin', valid_campsites[1].name)
        self.assertEqual('Cabin in the Woods', valid_campsites[2].name)

    def test_reservation_solver_returns_correct_campsites_for_campspot_test_case_and_minimum_reservation_length_of_1(self):
        sys.argv = ['reservation_solver.py', 'test_modules/test_cases/test-case.json', '-mrl', '1']
        valid_campsites = self.solver.main()
        self.assertEqual(5, len(valid_campsites))

    def test_reservation_solver_returns_correct_campsites_for_campspot_test_case_and_minimum_reservation_length_of_3(self):
        sys.argv = ['reservation_solver.py', 'test_modules/test_cases/test-case.json', '-mrl', '3']
        valid_campsites = self.solver.main()
        self.assertEqual(2, len(valid_campsites))
        self.assertEqual('Rickety Cabin', valid_campsites[0].name)
        self.assertEqual('Cabin in the Woods', valid_campsites[1].name)
    
    def test_reservation_solver_returns_correct_campsites_for_matts_test_case_and_default_minimum_reservation_length(self):
        sys.argv = ['reservation_solver.py', 'test_modules/test_cases/matts_test_case.json']
        valid_campsites = self.solver.main()
        self.assertEqual(3, len(valid_campsites))
        self.assertEqual('Comfy Cabin', valid_campsites[0].name)
        self.assertEqual('Rickety Cabin', valid_campsites[1].name)
        self.assertEqual('Cabin in the Woods', valid_campsites[2].name)

    def test_reservation_solver_does_not_return_campsite_when_search_entirely_inside_reservation(self):
        sys.argv = ['reservation_solver.py', 'test_modules/test_cases/search_in_reservation.json']
        valid_campsites = self.solver.main()
        self.assertEqual(0, len(valid_campsites))

    def test_reservation_solver_does_not_return_campsite_when_reservation_entirely_in_search(self):
        sys.argv = ['reservation_solver.py', 'test_modules/test_cases/reservation_in_search.json']
        valid_campsites = self.solver.main()
        self.assertEqual(0, len(valid_campsites))

    def test_reservation_solver_does_not_return_campsite_when_search_equals_reservation(self):
        sys.argv = ['reservation_solver.py', 'test_modules/test_cases/search_equals_reservation.json']
        valid_campsites = self.solver.main()
        self.assertEqual(0, len(valid_campsites))
    
    def test_reservation_solver_does_not_return_campsite_when_end_of_search_overlaps_beginning_of_reservation(self):
        sys.argv = ['reservation_solver.py', 'test_modules/test_cases/end_of_search_and_beginning_of_reservation_overlap.json']
        valid_campsites = self.solver.main()
        self.assertEqual(0, len(valid_campsites))

    def test_reservation_solver_does_not_return_campsite_when_beginning_of_search_overlaps_end_of_reservation(self):
        sys.argv = ['reservation_solver.py', 'test_modules/test_cases/beginning_of_search_and_end_of_reservation_overlap.json']
        valid_campsites = self.solver.main()
        self.assertEqual(0, len(valid_campsites))

if __name__ == '__main__':
    unittest.main()