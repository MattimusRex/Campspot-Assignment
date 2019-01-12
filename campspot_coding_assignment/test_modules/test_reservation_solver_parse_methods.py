import unittest
from datetime import date
import reservation_solver

class TestReservationSolverParseMethods(unittest.TestCase):
    def setUp(self):
        self.data = {}
        search = {"startDate":"2018-01-02", "endDate":"2018-02-03"}
        campsites = [{"id":1, "name":"Campsite 1"}, {"id":2, "name":"Campsite 2"}]
        reservations = [{"campsiteId":1, "startDate":"2018-01-15", "endDate":"2018-01-18"},
                        {"campsiteId":1, "startDate":"2018-01-19", "endDate":"2018-01-27"}, 
                        {"campsiteId":2, "startDate":"2018-11-11", "endDate":"2018-11-16"},
                        {"campsiteId":2, "startDate":"2018-11-19", "endDate":"2018-11-27"}]
        self.data["search"] = search
        self.data["campsites"] = campsites
        self.data["reservations"] = reservations

        self.bad_keys = {}
        self.bad_keys["searh"] = search
        self.bad_keys["campsies"] = campsites
        self.bad_keys["reservatons"] = reservations

        self.bad_inner_keys = {}
        search = {"startate":"2018-01-02", "endDate":"2018-02-03"}
        campsites = [{"id":1, "nme":"Campsite 1"}, {"id":2, "name":"Campsite 2"}]
        reservations = [{"campsiteId":1, "startDate":"2018-01-15", "endDate":"2018-01-18"},
                        {"campsited":1, "startDate":"2018-01-19", "endDate":"2018-01-27"}, 
                        {"campsiteId":2, "startDate":"2018-11-11", "endDate":"2018-11-16"},
                        {"campsiteId":2, "startDate":"2018-11-19", "endDate":"2018-11-27"}]
        self.bad_inner_keys["search"] = search
        self.bad_inner_keys["campsites"] = campsites
        self.bad_inner_keys["reservations"] = reservations

        self.solver = reservation_solver.ReservationSolver()

    def test_parse_search_returns_correct_values(self):
        search = self.solver._parse_search(self.data)
        start_date = date.fromisoformat('2018-01-02')
        end_date = date.fromisoformat('2018-02-03')
        print(search.start_date)
        self.assertEqual(start_date, search.start_date)
        self.assertEqual(end_date, search.end_date)

    def test_parse_search_returns_key_error_with_bad_key(self):
        with self.assertRaises(KeyError): self.solver._parse_search(self.bad_keys)

    def test_parse_search_returns_key_error_with_bad_inner_key(self):
        with self.assertRaises(KeyError): self.solver._parse_search(self.bad_inner_keys)

    def test_parse_campsites_returns_correct_values(self):
        campsites = self.solver._parse_campsites(self.data)
        self.assertEqual(2, len(campsites))
        campsite_1 = campsites[1]
        campsite_2 = campsites[2]
        self.assertEqual('Campsite 1', campsite_1.name)
        self.assertEqual('Campsite 2', campsite_2.name)

    def test_parse_campsites_returns_key_error_with_bad_key(self):
        with self.assertRaises(KeyError): self.solver._parse_campsites(self.bad_keys)

    def test_parse_campsites_returns_key_error_with_bad_inner_key(self):
        with self.assertRaises(KeyError): self.solver._parse_campsites(self.bad_inner_keys)

    def test_parse_reservations_returns_correct_values(self):
        reservations = self.solver._parse_reservations(self.data)
        self.assertEqual(4, len(reservations))
        start_date = date.fromisoformat('2018-01-19')
        end_date = date.fromisoformat('2018-11-27')
        self.assertEqual(1, reservations[0].campsite_id)
        self.assertEqual(start_date, reservations[1].start_date)
        self.assertEqual(end_date, reservations[3].end_date)

    def test_parse_reservations_returns_key_error_with_bad_key(self):
        with self.assertRaises(KeyError): self.solver._parse_reservations(self.bad_keys)
            
    def test_parse_reservations_returns_key_error_with_bad_inner_key(self):
        with self.assertRaises(KeyError): self.solver._parse_reservations(self.bad_inner_keys)


if __name__ == '__main__':
    unittest.main()