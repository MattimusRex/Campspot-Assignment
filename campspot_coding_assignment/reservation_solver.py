import sys
import argparse
import json
from datetime import date
from modules import search as Search
from modules import reservation as Reservation
from modules import campsite as Campsite

class ReservationSolver:
    # search: a Search that we want to find valid campsites for.
    # campsites: a list of Campsites to search
    # minimum_reservation: the smallest reservation length in days that a campsite is willing to accept
    # returns: a list of valid campsites
    def get_valid_campsites(self, search, campsites, minimum_reservation):
        valid_campsites = []
        #check request against each campsite
        for campsite in campsites:
            if self._check_campsite(campsite, search, minimum_reservation):
                valid_campsites.append(campsite)
        
        return valid_campsites

    # campsite: a Campsite to search
    # search: the Search we want to find campsites for
    # minimum_reservation: the smallest reservation length in days that a campsite is willing to accept
    # returns: True or False if the campsite can be booked for the search
    def _check_campsite(self, campsite, search, minimum_reservation):
        for reservation in campsite.reservations:
            #search range must be entirely before or entirely after reservation range
            #a gap of 0 is ok (two reservations back to back)
            #a gap >= the minimum reservation is ok (can be filled be another reservation)
            #anything less than the minimum reservation that isn't 0 can't be filled and is invalid
            start_gap = (reservation.start_date - search.end_date).days - 1
            end_gap = (search.start_date - reservation.end_date).days - 1
            if (start_gap != 0 and start_gap < minimum_reservation) and (end_gap != 0 and end_gap < minimum_reservation):
                return False 
        
        return True
    
    # json_data: a dictionary created from json file
    # returns: a Search object
    def _parse_search(self, json_data):
        try:
            search_json_data = json_data['search']
        except KeyError:
            raise KeyError('Error in reading search json data.')
        
        try:
            start_date = search_json_data['startDate']
            end_date = search_json_data['endDate']
        except KeyError:
            raise KeyError('Error in reading start date or end date under search json data.')

        return Search.Search(start_date, end_date)

    # json_data: a dictionary created from json file
    # returns: a dictionary of Campsites
    def _parse_campsites(self, json_data):
        campsites = {}
        try:
            campsite_json_data = json_data['campsites']
        except KeyError:
            raise KeyError('Error in reading campsite json data.')
        
        for item in campsite_json_data:
            try:
                campsite_id = int(item['id'])
                name = item['name']
            except KeyError:
                raise KeyError('Error in reading id or name for campsite json data.')
            
            campsite = Campsite.Campsite(campsite_id, name)
            campsites[campsite.id] = campsite

        return campsites

    # json_data: a dictionary created from json file
    # returns: a list of Reservations
    def _parse_reservations(self, json_data):
        reservations = []
        try:
            reservation_json_data = json_data['reservations']
        except KeyError:
            raise KeyError('Error in reading reservation json data.')
    
        for item in reservation_json_data:
            try:
                campsite_id = int(item['campsiteId'])
                start_date = item['startDate']
                end_date = item['endDate']
            except KeyError:
                raise KeyError('Error in reading campsite id, start date, or end date for reservation json data.')
            
            reservation = Reservation.Reservation(campsite_id, start_date, end_date)
            reservations.append(reservation)
        
        return reservations

def main():
    parser = argparse.ArgumentParser(description='Find valid reservations with the gap rule based on minimum reservation length.')
    parser.add_argument('input_file', help='The filename with extension of your json file.')
    parser.add_argument('-mrl', '--minimum_reservation_length', 
                        help='The minimum reservation length in days for this campground as an integer. Defaults to 2.',
                        type=int, default=2, choices=range(1, 4))
    args = parser.parse_args()
    
    try:
        with open(args.input_file, 'r') as input_file:
            json_data = json.load(input_file)
    except IOError:
        raise IOError('File does not exist, could not be opened, or could not be read.')

    minimum_reservation = args.minimum_reservation_length

    solver = ReservationSolver()
    search = solver._parse_search(json_data)
    campsites = solver._parse_campsites(json_data)
    reservations = solver._parse_reservations(json_data)
    for reservation in reservations:
        try:
            campsites[reservation.campsite_id].add_reservation(reservation)
        except KeyError:
            raise KeyError('Reservation with an invalid campsite id.')

    #build list of campsites from dictionary to make ReservationSolver easier to use elsewhere
    return solver.get_valid_campsites(search, [campsites[site] for site in campsites], minimum_reservation)

if __name__ == '__main__':
    valid_campsites = main()
    if len(valid_campsites) == 0:
        print("No valid campsite found for given data.")
    else:
        for site in valid_campsites:
            print(site.name)